filename = '/home/mio/my-git-repos/Project_Scilifelab/datasets/new_final_dssp.txt'
new_file = 'text.txt'
data = {}
aminos = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','U','V','W','Y']

with open(filename, 'r') as fid, open(new_file,'w') as p:
    lines = fid.read().splitlines()
    nline = ['%d:%s' % (i+1,a) for i,a in enumerate(aminos)]
    p.write('# ' + ' '.join(nline) + '\n')
    while lines:
        features = lines.pop()
        sequence = lines.pop()
        name = lines.pop()[1:]  # skip '>'
        newline = []
        for aa,ft in zip(sequence,features):
            if ft == 'S':
                nl = '1 '
            else:
                nl = '-1 '
            b = ['%d:%s' % (i+1,1) if aa==a else '%d:%s' % (i+1,0) 
                 for i,a in enumerate(aminos)]
            nl = nl + ' '.join(b)
            newline.append(nl)
        p.write('\n'.join(newline) + '\n')
