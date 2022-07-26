import os
import json
import datetime


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

files_path = path_dict["file_path"]
methods_path = path_dict["function_path"]
bugs_path = path_dict["bug_path"]
gtfs_path = path_dict["gtf_path"]
repos = os.listdir(bugs_path)
target_bug_num = 0
target_repo_num = 0
for repo in repos:
    versions = os.listdir(bugs_path+repo+"\\")
    project_bug_num = 0
    for version in versions:
        if os.path.exists(gtfs_path+repo+"\\"+version+"\\") is False:
            os.makedirs(gtfs_path+repo+"\\"+version+"\\")
        bugs = os.listdir(bugs_path+repo+"\\"+version+"\\")
        files = os.listdir(methods_path+repo+"\\"+version+"\\")
        
        files_dict = {}
        files_dict_by_name = {}
        files_name_set= set()

        methods_dict = {}
        methods_dict_by_name = {}
        methods_name_set= set()
        for file in files:
            if file.endswith(".txt") is False:
                continue
            lang = file.replace("KeyMap.txt", "").lower()

            files_path = methods_path+repo+"\\"+version+"\\"+file
            f = open(files_path, "r", encoding="utf8")
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n","")
                if line.find("|") == -1:
                    continue
                tokens = line.split("|")
                file_id = tokens[0]
                file_name = tokens[1].lower().replace("\\\\","\\")
                files_dict[file_id] = file_name
                files_name_set.add(file_name)
                files_dict_by_name[file_name] = file_id

                method_id = file_id+"|"+tokens[2]
                method_name = file_name+"|"+tokens[3].lower()
                methods_dict[method_id] = method_name
                methods_name_set.add(method_name)
                methods_dict_by_name[method_name] = method_id
        for bug in bugs:                      
            bug_path = bugs_path+repo+"\\"+version+"\\"+bug
            contents = None
            with open(bug_path, 'r', encoding ="utf8") as j:
                contents = json.loads(j.read())
            
            bug_id = bug.replace(".json","")
            changed_files = contents['commit']['changed_files']
            file_type_set = set()            
            buggy_methods_ids = set()
            for changed_file in changed_files:
                change_type = contents['commit']['changed_files'][changed_file]['file_change_type']
                if change_type != "MODIFY":
                    continue
                original_file_name = contents['commit']['changed_files'][changed_file]['file_old_name'].lower()                
                if original_file_name not in files_name_set:
                    continue
                hunks =  contents['commit']['changed_files'][changed_file]["hunks"]
                for hunk in hunks:
                    isMethod = contents['commit']['changed_files'][changed_file]["hunks"][hunk]["Ismethod"]
                    if isMethod == 1:
                        method_name = contents['commit']['changed_files'][changed_file]["hunks"][hunk]["method_info"]["method_name"].lower()
                        method_identifier = original_file_name+"|"+method_name        
                        if method_identifier in methods_name_set:
                            buggy_methods_ids.add(methods_dict_by_name[method_identifier].split("|")[1])                            
                            
            print(bug_id, buggy_methods_ids)
            print(repo, version, bug, buggy_methods_ids)
            if len(buggy_methods_ids) == 0:
                continue
            f = open(gtfs_path+repo+"\\"+version+"\\"+bug_id+"_method.txt", "w", encoding="utf8")
            for buggy_mth_id in buggy_methods_ids:
                f.write("python-"+buggy_mth_id+"\n")
            f.close()
            target_bug_num += 1
            project_bug_num += 1
    if project_bug_num > 0:
        target_repo_num += 1
print(target_repo_num, target_bug_num,project_bug_num)


