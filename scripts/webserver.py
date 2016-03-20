import numpy as np
import subprocess


Uniref = '/home/mio/Desktop/uniref_90/uniref90.fasta'
SVMdir = '/home/mio/Desktop/svm_light/'
SVModel = '/home/mio/Desktop/hope_final/multi_seq2/multi_model_final_opt2'


def main(input_sequence):
    """
    input_sequence is a file that the user provides
    """
    # First step: Psi-blast the given sequence
    blastpgp = 'blastpgp -a 3 -j 3 -d {database} -i Inputs/{filename} \
                -o BlastPGP/{filename}.blastpgp -Q PSI/{filename}.psi \
                &> Logs/{filename}.log'.format(database=Uniref, filename=input_sequence)
    subprocess.call(blastpgp)
    
    # Second Step: Prepare SVM input
    psifile = 'PSI/%s.psi' % input_sequence
    sequence, matrix = sigmoid(psifile)
    svm_input = '/tmp/svm_input'  # maybe add some salt...
    with open(svm_input, 'w') as svm:
        for row in matrix:
            svm.write('0')  # Feature to predict (not known!)
            for i, val in enumerate(row[1:]):
                svm.write(' %d:%f' % (i+1, val))
            svm.write('\n')
    
    # Third Step: Classify using SVM
    outfile = 'tmp/%s.out' % input_sequence
    svmclassify = '{SVMdir}/svm_classify {SVMinput} {model} {output}'
    subprocess.call(svmclassify.format(SVMdir=SVMdir, SVMinput=svm_input,
                                    model=SVModel, output=outfile))
    
    # Fourth Step: Write Results
    results = 'Results/%s.txt' % input_sequence
    with open(outfile, 'r') as fid, open(results, 'w') as res:
        features = ['-' if row[0] == '-' else 'S' for row in fid]
        res.write(''.join(sequence) + '\n')
        res.write(''.join(features) + '\n')


def sigmoid(psifile):
    with open(psifile, 'r') as fid:
        lines = fid.read().splitlines()
        lines = [row.split() for row in lines[3:-6]]

    nrows = len(lines)
    sequence = [row[1] for row in lines]
    matrix = np.array([row[2:22] for row in lines], dtype=float)
    matrix_sig = 1/(1 + np.exp(-matrix))
    
    conservation = np.array([row[-2] for row in lines], dtype=float) / 4.32
    conservation.shape = (nrows, 1)
    
    matrix_final = np.concatenate((np.zeros((nrows, 1)), matrix_sig, conservation), axis = 1)
    
    return sequence, matrix_final

