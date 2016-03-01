filename = '/home/mio/Desktop/Project/Datasets/final_seq_no_3dline.txt'
with open(filename, 'r') as fid:
    lines = fid.read().splitlines()
count = 0
for line in range(0,int(len(lines)), 2):
    count = count + 1
    n = open("seq" + str(count) + ".txt", 'w')
    n.write(lines[0] + '\n' + lines[1] + '\n')
    