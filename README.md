# Project_Scilifelab

The aim of the Project_Scilifelab is to develop a predictor for b-sheets of a globular protein, based on SVM, by using evolutionary information (PSI-BLAST)

The folder 'script' contains:
  - groupsi.py: It extracts the features of the single sequence from the given dataset and it creates the groups for the cross          validation. It also modifies the matrix from PSI-BLAST to convert it to SVM input and it assigns the feature for any amino acid. As in single sequence, it creates also the groups for the cross validation.
  - run_psiblast.sh: the command to run the PSI-BLAST
  - results_svm: In this folder there is for each occasion (multiple / single sequence) the outfiles and the models from SVM, as well the scripts for the calculation of ROC curve and MCC, sensitivity, specificity, accuracy
  - webserver.py: the script to be used for the webserver creation

The folder 'datasets' contains:
  - new_final_dssp.txt: It is the given dataset corrected, without wrong letters or question marks
  - cdhit_random.txt: It is the resulted file from CD-hit with the clusters
  - psiblast_final: The result for the PSI-BLAST  

The folder 'results' contains:
  - multi_seq2: contains the outfiles and models from SVM (for the PSI-BLAST sequences), with the groups for cross validation
  - single_seq2:  contains the outfiles and models from SVM, with the groups for cross validation
