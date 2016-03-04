input_dir=~/my-git-repos/Project_Scilifelab/datasets/psiblast/
for i in $input_dir/*.txt ; do
	blastpgp -j 3 -d /home/mio/Desktop/uniref_90/uniref90.fasta -i ${i} -o "${i/.txt}".blastpgp -Q "${i/.txt}".psi 
done

