import math

filename = '/home/mio/Desktop/blast-2.2.26/verynew.txt'

with open(filename, 'r') as fid, open('SVMinput.txt', 'w') as svm:     # open('input.txt', 'w') as probab:
    for row in fid:
        for i,n in enumerate(row.split()):
            n = (1/(1 + math.exp(-float(n))))
            new_row = ['%d:%f' % (i+1, n)]
            svm.write(' '.join(new_row) + '\n')

"""
with open(filename, 'r') as fid, open('SVMinput.txt', 'w') as svm:
    for row in fid:
        new_row = ['%d:%s' % (i+1, n) for i, n in enumerate(row.split())]
        svm.write(' '.join(new_row) + '\n')"""