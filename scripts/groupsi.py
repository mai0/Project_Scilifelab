import re
import numpy as np
from random import shuffle, seed


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


def read_sequences(filename):
	"""
	Creates a dictionary with sequences as keys and tuples of aminochains and feautures as values.
	"""
	with open(filename, 'r') as fid:
		lines = fid.read().splitlines()

	sequence = {}
	for line in range(0,int(len(lines)),3):
		sequence[lines[line]] = (lines[line+1], lines[line+2])
	
	return sequence


def read_clusters(filename):
    """
    Reads a blast find and groups homologue sequences into lists and returns a list of these lists.
    """
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
    
    return clusters
    

def merge_clusters(path_to_files, clusters, Sequences):
    """
    Takes the clusters from read_clusters and creates a list with sequences, features and the sigmoid from psi values stored in 'path_to_files'.
    """
    uni_matrix = []
    for cluster in clusters:
        matrix = []
        cluster_features = ''
        cluster_sequence = ''
        for sequence in cluster:
            filename = psi_folder + sequence[1:] + '.psi'
            try:
                matrix.append(sigmoid(filename))
            except IOError:
                print 'cannot find file', filename
                continue
            cluster_features += Sequences[sequence][1]
            cluster_sequence += Sequences[sequence][0]
        if matrix:
            matrix = np.concatenate(matrix)
            uni_matrix.append((matrix, cluster_features,cluster_sequence))
    return uni_matrix


# Prepare
sequence_clusters = read_clusters('cdhit_random.txt')
Sequences = read_sequences('new_final_dssp.txt')
psi_folder = 'psiblast_final/'
Clusters = merge_clusters(psi_folder, sequence_clusters, Sequences)

# Randomize
seed(9)
shuffle(Clusters)

# Write PSI
start = 0
finish = len(Clusters)/6
step = len(Clusters)/6
for j in range(6):
    Matrix = []
    Features = ''
    for matrix, features, sequences in Clusters[start:finish]:
        Matrix.append(matrix)
        Features += features
    Matrix = np.concatenate(Matrix)
    
    with open('group_psi_%d.txt' % j, 'w') as group:
        for ft, row in zip(Features, Matrix):
            group.write('1' if ft == 'S' else '-1')
            for i, val in enumerate(row):
                group.write(' %d:%f' % (i+1, val))
            group.write('\n')
    
    start = finish
    finish += step

# Write signle model
start = 0
finish = len(Clusters)/6
step = len(Clusters)/6
aminos = 'A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V'.split()
for j in range(6):
    Sequence = ''
    Features = ''
    for matrix, features, sequences in Clusters[start:finish]:
        Sequence += sequences
        Features += features

    with open('group_single_%d.txt' % j, 'w') as group:
        for feat, seq in zip(Features, Sequence):
             group.write('1 ' if feat == 'S' else '-1 ')
             group.write(' '.join(('%d:1' % (i+1) if a == seq else '%d:0' % (i+1) for i, a in enumerate(aminos))))
             group.write('\n')
    
    start = finish
    finish += step
