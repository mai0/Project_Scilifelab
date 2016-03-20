import math

file1 = '/home/mio/Desktop/resulst_svm/multiple/kernel_0/group_53210_psi_total.txt'
file2 = '/home/mio/Desktop/resulst_svm/multiple/kernel_2/opt1/outfile_multi_t2_opt1_total'

f1 = open(file1,'r')
fi_1 = f1.read().splitlines()
f2 = open(file2,'r')
fi_2 = f2.read().splitlines()
ev = open('evaluation.txt','w')

TN = 0
FP = 0
TP = 0
FN = 0
#result1 = [list(l1.rstrip()) for l1 in fi_1]
#result2 = [list(l2.rstrip()) for l2 in fi_2]
#zipa = zip(result1,result2)

for l1,l2 in zip(fi_1,fi_2):
        if l1[0] == '-' and l2[0] == '-':
            TN = TN + 1
            ev.write('tn' + '\n')
        if l1[0] == '-' and l2[0] != '-':
            FP = FP + 1
            ev.write('fp' + '\n')
        if l1[0] != '-' and l2[0] != '-':
            TP = TP + 1
            ev.write('tp' + '\n')
        if l1[0] != '-' and l2[0] == '-':
            FN = FN + 1
            ev.write('fn' + '\n')
ev.write('num_TN=' + str(TN) + '\n')
ev.write('num_FP=' + str(FP) + '\n')
ev.write('num_TP=' + str(TP) + '\n')
ev.write('num_FN=' + str(FN) + '\n')

mcc = (TP*TN - FP*FN) / math.sqrt( (TP + FP)*(TP + FN)*(TN + FN)*(TN + FN) )
#print mcc
ev.write('MCC=' + str(mcc) + '\n')
accuracy = (TP+TN)/float(TP+TN+FP+FN)
ev.write('accuracy=' + str(accuracy) + '\n')
#print accuracy
sensitivity = TP/float(TP+FN)
specificity = TN/float(TN+FP)
ev.write('sensitivity=' + str(sensitivity) + '\n')
ev.write('specificity=' + str(specificity) + '\n')