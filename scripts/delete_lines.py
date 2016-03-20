import re
import numpy as np

#filename = 'C:\Users\marina\Desktop\seq148.psi'
def sigmoid(filename):
    """ 
    first remove the lines and perform the sigmoid
    """
    with open(filename,'r') as fid:
        lines = fid.read().splitlines()
    
    lines = [row.split()[2:22] for row in lines[3:-6]]
    
    matrix = np.array(lines, dtype=float)
    matrix_sig = 1/(1 + np.exp(-matrix))
    return matrix_sig
    
filename = '/home/mio/my-git-repos/Project_Scilifelab/datasets/new_final_dssp.txt'

with open(filename, 'r') as fid:
    lines = fid.read().splitlines()
    
sequence = {}
for line in range(0,int(len(lines)),3):
    sequence[lines[line]] = (lines[line+1], lines[line+2])     
    
    
filename = '/home/mio/my-git-repos/Project_Scilifelab/datasets/cdhit_random.txt'

with open(filename,'r') as fid:
    clusters = []
    clust = []
    line = fid.readline() #diavasa cluster[0]
    line = fid.readline() #diavazw 1o entry cluster
    while line:
        if '>Cluster' in line:
            clusters.append(clust)
            clust = []
        else:
            match = re.search(r'(>.+)\.\.\.', line) 
            clust.append(match.group(1))
        line = fid.readline()
    clusters.append(clust)   

psi_folder = '/home/mio/my-git-repos/Project_Scilifelab/datasets/test_deletelines'  
for clus in clusters:
    matrix = []
    feat = ''
    for seq in clus:
        filename = psi_folder + seq[1:] + '.psi'
        matrix.append(sigmoid(filename))
        feat += sequence[seq][1]
        matrix = np.concatenate(matrix)
        
    with open(seq[1:] + 'output.txt', 'w') as fid:
        for j, row in enumerate(matrix):
            ft = '1' if feat[j]=='S' else '-1'
            fid.write(ft)
            for n in enumerate(row):
                fid.write(' %d:%.4f' % n)
            fid.write('/n')


