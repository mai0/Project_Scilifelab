from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
#import sklearn
#import random

def roccurve(prediction_file, actual_file):
    with open(prediction_file, 'r') as f1, open(actual_file, 'r') as f2:
        prediction = map(float, f1.read().splitlines())
        data = [int(line.split()[0]) for line in f2]
        
    mpreds, mlabels = zip(*sorted(zip(prediction, data)))

    return mlabels, mpreds
    #false_positive_rate, true_positive_rate, thresholds = roc_curve(mlabels, mpreds)
    #roc_auc = auc(false_positive_rate, true_positive_rate)
     

file_kernel_0 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_2/default/outfile_multi_t2_total'
file_real_k0 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_0/group_53210_psi_total.txt'
mlabels, mpreds = roccurve(file_kernel_0,file_real_k0)
false_positive_rate, true_positive_rate, thresholds = roc_curve(mlabels, mpreds)
roc_auc0 = auc(false_positive_rate, true_positive_rate)

file_kernel_1 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_2/opt1/outfile_multi_t2_opt1_total'
file_real_k1 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_0/group_53210_psi_total.txt'
ml1, mp1 = roccurve(file_kernel_1,file_real_k1)
fpr1, tpr1, t1 = roc_curve(ml1,mp1)
roc_auc1 = auc(fpr1, tpr1)

file_kernel_2 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_2/opt2/outfile_multi_t2_opt2_total'
file_real_k2 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_0/group_53210_psi_total.txt'
ml2, mp2 = roccurve(file_kernel_2,file_real_k2)
fpr2, tpr2, t2 = roc_curve(ml2,mp2)
roc_auc2 = auc(fpr2, tpr2)
    
file_kernel_3 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_2/opt3/outfile_multi_t2_opt3_total'
file_real_k3 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_0/group_53210_psi_total.txt'
ml3, mp3 = roccurve(file_kernel_3,file_real_k3)
fpr3, tpr3, t3 = roc_curve(ml3,mp3)
roc_auc3 = auc(fpr3, tpr3)

file_kernel_4 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_2/opt4/outfile_multi_t2_opt4_total'
file_real_k4 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/kernel_0/group_53210_psi_total.txt'
ml4, mp4 = roccurve(file_kernel_4,file_real_k4)
fpr4, tpr4, t4 = roc_curve(ml4,mp4)
roc_auc4 = auc(fpr4, tpr4)

file_kernel_5 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/outfile_multi_final.out'
file_real_k5 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/multiple/group_psi_4.txt'
ml5, mp5 = roccurve(file_kernel_5,file_real_k5)
fpr5, tpr5, t5 = roc_curve(ml5,mp5)
roc_auc5 = auc(fpr5, tpr5)
    
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b', label='RBF default')
plt.plot(fpr1, tpr1, 'g', label='optimization 1')
plt.plot(fpr2, tpr2, 'r', label='optimization 2')
plt.plot(fpr3, tpr3, 'y', label='optimization 3')
plt.plot(fpr4, tpr4, 'm', label='optimization 4')
plt.plot(fpr5, tpr5, 'c', label='final model')
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'k--')
plt.axis([-0.1, 1.2, -0.1, 1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
