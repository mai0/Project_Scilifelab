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
     

file_kernel_0 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_0/outfile_single_t0_total'
file_real_k0 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_0/group_53210_total.txt'
mlabels, mpreds = roccurve(file_kernel_0,file_real_k0)
false_positive_rate, true_positive_rate, thresholds = roc_curve(mlabels, mpreds)
roc_auc0 = auc(false_positive_rate, true_positive_rate)

file_kernel_1 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_1/outfile_single_t1_total'
file_real_k1 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_0/group_53210_total.txt'
ml1, mp1 = roccurve(file_kernel_1,file_real_k1)
fpr1, tpr1, t1 = roc_curve(ml1,mp1)
roc_auc1 = auc(fpr1, tpr1)

file_kernel_2 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_2/outfile_single_t2_total'
file_real_k2 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_0/group_53210_total.txt'
ml2, mp2 = roccurve(file_kernel_2,file_real_k2)
fpr2, tpr2, t2 = roc_curve(ml2,mp2)
roc_auc2 = auc(fpr2, tpr2)
    
file_kernel_3 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_3/outfile_single_t3_total'
file_real_k3 = 'C:/Users/marina/Desktop/resulst_svm-2016-03-19/resulst_svm/single/kernel_0/group_53210_total.txt'
ml3, mp3 = roccurve(file_kernel_3,file_real_k3)
fpr3, tpr3, t3 = roc_curve(ml3,mp3)
roc_auc3 = auc(fpr3, tpr3)
    
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b', label='linear')
plt.plot(fpr1, tpr1, 'g', label='polynomial')
plt.plot(fpr2, tpr2, 'r', label='RBF')
plt.plot(fpr3, tpr3, 'y', label='sigmoid')
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'k--')
plt.axis([-0.1, 1.2, -0.1, 1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
