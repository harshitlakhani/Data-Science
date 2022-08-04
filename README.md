# Project title 
Are Deep Learning-based Software bugs different than traditional bugs for bug localization? An empirical study.

# Motivation
Course project for The Process of Data Science

# Project Description
Developers need to know which files should be updated to repair an issue when a new bug report emerges. They may need to examine multiple source code files to identify the issue in a significant software project, which might be time-consuming and expensive. Based on initial bug reports for real-world open-source projects, contemporary IR-based algorithms efficiently locate relevant source code files. But bugs for testing and debugging differ for each subject system (e.g., programming language, application, software). Deep learning-related software bugs are more complex and challenging to debug than traditional bugs. In this paper, firstly, we plan to determine the performance difference between deep learning-based bugs and traditional software bugs using existing IR-based techniques for bug localization. Secondly, we intend to understand the impact of extrinsic and intrinsic bugs on deep learning software-based bugs and whether it correlates with bug localization performance. Lastly, to address the performance of deep learning-based software bugs for bug localization, we propose using a pre-trained language model to determine whether the performance improves compared to IR-based techniques.

# System Requirements
- Python 3.7 - (All the files from the source code are written in python hence .py file)
- PyTorch
- nltk
- kutils 0.3.0.
- gensim
- pyLDAvis
- PyNonpar
- Pingouin
- Tensorflow 2.8.0
- Keras 2.8.0
- Operating System: Windows 10 Home/ MacOS
- PC configuration: 16.0 GB RAM

# Installation details:
Install these packages using command prompt or using Google Colab/Calvert:

- pip install PyNonpar
- pip install Pingouin
- pip install kutils 0.3.0.
- pip install keras
- pip install Tensorflow
- pip install Python 3.7 - (All the files from the source code are written in python hence .py file)
- pip install PyTorch
- pip install nltk
- pip install gensim
- pip install pyLDAvis
- pip install bert
- pip install codeBert
- pip install rank-bm25

# Licensing Information
- The replication package has been used to verify efficiency of existing methodoligies
- IRBL for DLSW : <https://github.com/RosePasta/IRBL_for_DLSW>

# Steps to run
- Clone replication package
- Follow steps mentioned in the readme file to download repositories
- Make necessary changes to bring replication package in executable state
- Generate dataset and efficiency report of replication package
- Subsample dataset 
- For labelling extensic and intrensic bugs, run extrinsic_intrinsic.ipynb file in 'Extrensic-Intrensic bugs' folder to generate report with summary and descripition in csv format
- run codebert_evaluation.ipynb and bert_evaluation.ipynb file present in 'BERT and CodeBERT' folder to generate evaluation result
- Plotly <https://chart-studio.plotly.com/feed/> has been used to generate visualizations

# Contributor
- Sigma Jahan (sigma.jahan@dal.ca)
- Harshit Lakhani (harshit.lakhani@dal.ca)
- Sharad Kumar (sharad.kumar@dal.ca)
- Meghna Rupchandani (mg841071@dal.ca)
