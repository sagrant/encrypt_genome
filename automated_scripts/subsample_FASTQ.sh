#!/bin/bash
#automates assmebly process of subsampling FASTQ files

python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample1_1.fastq -i2 sample1_2.fastq -fq1 sub1_1.fastq -fq2 sub1_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample2_1.fastq -i2 sample2_2.fastq -fq1 sub2_1.fastq -fq2 sub2_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample3_1.fastq -i2 sample3_2.fastq -fq1 sub3_1.fastq -fq2 sub3_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample4_1.fastq -i2 sample4_2.fastq -fq1 sub4_1.fastq -fq2 sub4_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample5_1.fastq -i2 sample5_2.fastq -fq1 sub5_1.fastq -fq2 sub5_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample6_1.fastq -i2 sample6_2.fastq -fq1 sub6_1.fastq -fq2 sub6_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample7_1.fastq -i2 sample7_2.fastq -fq1 sub7_1.fastq -fq2 sub7_2.fastq
python3 /home/sagrant/encrypt_genome/subsample_FASTQ.py -i1 sample8_1.fastq -i2 sample8_2.fastq -fq1 sub8_1.fastq -fq2 sub8_2.fastq

mkdir original_samples/
mv sample1_1.fastq original_samples/
mv sample1_2.fastq original_samples/
mv sample2_1.fastq original_samples/
mv sample2_2.fastq original_samples/
mv sample3_1.fastq original_samples/
mv sample3_2.fastq original_samples/
mv sample4_1.fastq original_samples/
mv sample4_2.fastq original_samples/
mv sample5_1.fastq original_samples/
mv sample5_2.fastq original_samples/
mv sample6_1.fastq original_samples/
mv sample6_2.fastq original_samples/
mv sample7_1.fastq original_samples/
mv sample7_2.fastq original_samples/
mv sample8_1.fastq original_samples/
mv sample8_2.fastq original_samples/

cat sub1_1.fastq sub2_1.fastq sub3_1.fastq sub4_1.fastq sub5_1.fastq sub6_1.fastq sub7_1.fastq sub8_1.fastq > concat_1.fastq
cat sub1_2.fastq sub2_2.fastq sub3_2.fastq sub4_2.fastq sub5_2.fastq sub6_2.fastq sub7_2.fastq sub8_2.fastq > concat_2.fastq


python3 /home/sagrant/encrypt_genome/sharedFASTQReads.py -fq1 concat_1.fastq -fq2 concat_2.fastq 

mv concat_1.fastq /home/sagrant/dna_privacy/SPAdes-3.15.4-Linux/bin
mv concat_2.fastq /home/sagrant/dna_privacy/SPAdes-3.15.4-Linux/bin