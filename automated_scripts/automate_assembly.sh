#!/bin/bash
#assembly_control.sh 
#automates assmebly process to generate control assemblies 

mkdir /home/sagrant/dna_privacy/SPAdes-3.15.4-Linux/bin/concat_spades_out
output_dir=~/home/sagrant/dna_privacy/SPAdes-3.15.4-Linux/bin/concat_spades_out

cd ./SPAdes-3.15.4-Linux/bin 
concat1=concat_1.fastq
concat2=concat_2.fastq

./spades.py -m 500 -t 40 -1 $concat1 -2 $concat2 -o $output_dir
cd ..
cd ..
./minimap2/minimap2 -ax sr -t 40 $output_dir/contigs.fasta $concat1 $concat2 > concat.sam


