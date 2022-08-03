import os
from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi
import util.ir_util as ir_util
import math 

def loader():
    path_dict = {}
    lines = open("./z_config.txt","r", encoding="utf8").readlines()
    for line in lines:
        line = line.replace("\n","")
        tokens = line.split("=",2)
        label = tokens[0]
        path = tokens[1]
        path_dict[label] = path
    return path_dict

path_dict = loader()
bugs_path = path_dict["query_path"]
function_path = path_dict["function_path"]
gtfs_path = path_dict["gtf_path"]
irbl_path = path_dict["irbl_path"]

repos = os.listdir(bugs_path)

mrr_bm = 0
map_bm = 0
target_bug_num = 0
target_repo_num = 0
for repo in repos:
    versions = os.listdir(bugs_path+repo+"\\")
    project_bug_num = 0
    for version in versions:
        methods = os.listdir(function_path+repo+"\\"+version+"\\python_pp\\")
        if len(methods) == 0:
            continue
        method_corpus = []
        method_id_list = []
        lengths = []
        max_length = 0
        min_length = 99999
        for method in methods:
            file_id = method.split(".")[0]
            contents = ' '.join(open(function_path+repo+"\\"+version+"\\python_pp\\"+method, "r", encoding="utf8").readlines()).replace("\n"," ")
            method_corpus.append(contents)
            method_id_list.append("python-"+file_id)
        tokenized_corpus = [doc.split(" ") for doc in method_corpus]
        bm25_model = BM25Okapi(tokenized_corpus)

        bugs = os.listdir(bugs_path+repo+"\\"+version+"\\")
        for bug in bugs:
            if os.path.exists(gtfs_path+repo+"\\"+version+"\\"+bug+".txt") is False:
                continue
            query = ' '.join(open(bugs_path+repo+"\\"+version+"\\"+bug+"\\query_base-desc.txt", "r", encoding="utf8").readlines()).replace("\n","")
            query_sum = ' '.join(open(bugs_path+repo+"\\"+version+"\\"+bug+"\\query_base-sum.txt", "r", encoding="utf8").readlines()).replace("\n","")
            query = query + " "+query_sum
            query = query.strip()
            if os.path.exists(gtfs_path+repo+"\\"+version+"\\"+bug+"_method.txt") is False:
                continue
            lines = open(gtfs_path+repo+"\\"+version+"\\"+bug+"_method.txt", "r", encoding="utf8").readlines()
            gtf_list = []
            for line in lines:
                line = line.replace("\n","")
                if len(line) < 3:
                    continue
                gtf_list.append(line)

            if os.path.exists(irbl_path+"\\"+repo+"\\"+version+"\\"+bug+"\\mth_sim\\") is False:
                os.makedirs(irbl_path+"\\"+repo+"\\"+version+"\\"+bug+"\\mth_sim\\")

            if len(gtf_list) == 0:
                continue

            bm25_sim_scores = ir_util.retrieval_bm25(bm25_model, method_id_list, query)
            bm25_top_rank, bm25_rr, bm25_ap, _, _  = ir_util.evaluation(bm25_sim_scores, gtf_list, len(method_corpus), 100000)

            print(repo, version, bug, len(gtf_list),bm25_rr, bm25_ap)

            f = open(irbl_path+"\\"+repo+"\\"+version+"\\"+bug+"\\mth_sim\\python_bm25.txt", "w", encoding="utf8")
            for file_id in bm25_sim_scores.keys():
                f.write(file_id+"\t"+str(bm25_sim_scores[file_id])+"\n")
            f.close()
            
            mrr_bm += bm25_rr
            map_bm += bm25_ap

            target_bug_num += 1
            project_bug_num += 1

                
    if project_bug_num > 0:
        target_repo_num += 1

    print(target_repo_num, target_bug_num, project_bug_num)
    print(mrr_bm/target_bug_num,map_bm/target_bug_num)
