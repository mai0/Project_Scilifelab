import math

filename = '/home/mio/Desktop/blast-2.2.26/verynew.txt'
SVMinput = 'svm_input.txt'
def sigmoid(x):
    return (1/(1 + math.exp(-float(x))))
    
with open(filename, 'r') as fid, open(SVMinput, 'w') as svm:
    for row in fid:
        new_row = ['%d:%s' % (i+1, sigmoid(r)) for i, r in enumerate(row.split())]
        svm.write(' '.join(new_row) + '\n')