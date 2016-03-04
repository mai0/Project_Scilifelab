file1 = '/home/mio/my-git-repos/Project_Scilifelab/results/groups/group0234.txt'
file2 = '/home/mio/Desktop/svm_light/outfile0234.out'

f1 = open(file1,'r')
fi_1 = f1.read().splitlines()
f2 = open(file2,'r')
fi_2 = f2.read().splitlines()
ev = open('evaluation0234.txt','w')

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
ev.write('num_tn' + str(TN) + '\n')
ev.write('num_fp' + str(FP) + '\n')
ev.write('num_tp' + str(TP) + '\n')
ev.write('num_Fn' + str(FN) + '\n')