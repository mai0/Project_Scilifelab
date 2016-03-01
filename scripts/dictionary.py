filename = '/home/mio/my-git-repos/Project_Scilifelab/datasets/new_final_dssp.txt'
with open(filename, 'r') as fid:
    lines = fid.read().splitlines()
    
dict = {}
for line in range(0,int(len(lines)),3):
    dict[lines[line]] = (lines[line+1], lines[line+2])