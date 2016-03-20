import re
from random import shuffle


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

filename = '/home/mio/my-git-repos/Project_Scilifelab/datasets/new_final_dssp.txt'
with open(filename, 'r') as fid:
    lines = fid.read().splitlines()
    
sequence = {}
for line in range(0,int(len(lines)),3):
    sequence[lines[line]] = (lines[line+1], lines[line+2])        

filename = 'cluster_sequence.txt'
with open(filename, 'w') as fid:
    clust_seq = []
    for i,clust in enumerate(clusters):
        fid.write('>Cluster %d\n' %i)
        seq = ''
        feat = ''
        for c in clust:
            seq += sequence[c][0]
            feat += sequence[c][1]
        fid.write('%s\n' % seq)
        fid.write('%s\n' % feat)
        clust_seq.append((seq,feat))


shuffle(clust_seq)
aminos = ['A','C','D','E','F','G','H','I','K','L','M','N',
          'P','Q','R','S','T','U','V','W','Y']
finish = len(clust_seq)/6
sixth = len(clust_seq)/6
start = 0
for j in range(6):
    with open ('group_%d.txt' % j, 'w') as tr:
        for seq,feat in clust_seq[start:finish]:
            for s,f in zip(seq,feat):
                if f == 'S':
                    nl = '1 '
                else:
                    nl = '-1 '
                b = ['%d:%s' % (i+1,1) if s==a else '%d:%s' % (i+1,0) 
                     for i,a in enumerate(aminos)]
                nl = nl + ' '.join(b)
                tr.write(nl + '\n')
    start = finish
    finish = finish + sixth