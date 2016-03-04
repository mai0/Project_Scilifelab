filename = '/home/mio/my-git-repos/Project_Scilifelab/datasets/final_seq_no_3dline.txt'
outdir = '/home/mio/my-git-repos/Project_Scilifelab/datasets/psiblast/'
with open(filename, 'r') as fid:
    lines = fid.read().splitlines()
count = 0
for line in range(0,int(len(lines)), 2):
    count = count + 1  
    myfile = outdir + lines[line][1:] + ".txt"
    #print myfile
    n = open(myfile, 'w')
    n.write(lines[line] + '\n' + lines[line + 1] + '\n')
    