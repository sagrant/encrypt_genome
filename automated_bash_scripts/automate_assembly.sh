#assembly_control.sh 
#automates assmebly process to generate control assemblies 


concat1=~/encrypt_genome/concat_1.fastq
concat2=~/encrypt_genome/concat_2.fastq

output_dir=/home/sagrant/encrypt_genome/SPAdes-3.15.4-Linux/bin/concat_spades_out/

(cd ./SPAdes-3.15.4-Linux/bin && exec ./spades.py -1 $concat1 -2 $concat2 -o $output_dir)
./minimap2/minimap2 -ax sr $output_dir/contigs.fasta $concat1 $concat2 > concat.sam



