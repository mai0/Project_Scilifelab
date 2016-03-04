import math


filename = '/home/mio/Desktop/blast-2.2.26/verynew.txt'
    
with open(filename, 'r') as fid, open('input.txt', 'w') as probab:
    for row in fid:
    for r in row.split():
        #print r
        varia = float(1/((1 + math.exp(-float(r)))))
        r = varia