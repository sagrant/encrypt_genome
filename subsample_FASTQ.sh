#!/bin/bash
#automates assmebly process of subsampling FASTQ files

python3 subsample_FASTQ.py -i1 sample1_1.fastq -i2 sample1_2.fastq -fq1 sub1_1.fastq -fq2 sub1_2.fastq
python3 subsample_FASTQ.py -i1 sample2_1.fastq -i2 sample2_2.fastq -fq1 sub2_1.fastq -fq2 sub2_2.fastq
python3 subsample_FASTQ.py -i1 sample3_1.fastq -i2 sample3_2.fastq -fq1 sub3_1.fastq -fq2 sub3_2.fastq
python3 subsample_FASTQ.py -i1 sample4_1.fastq -i2 sample4_2.fastq -fq1 sub4_1.fastq -fq2 sub4_2.fastq
python3 subsample_FASTQ.py -i1 sample5_1.fastq -i2 sample5_2.fastq -fq1 sub5_1.fastq -fq2 sub5_2.fastq
python3 subsample_FASTQ.py -i1 sample6_1.fastq -i2 sample6_2.fastq -fq1 sub6_1.fastq -fq2 sub6_2.fastq
python3 subsample_FASTQ.py -i1 sample7_1.fastq -i2 sample7_2.fastq -fq1 sub7_1.fastq -fq2 sub7_2.fastq
python3 subsample_FASTQ.py -i1 sample8_1.fastq -i2 sample8_2.fastq -fq1 sub8_1.fastq -fq2 sub8_2.fastq

cat sub1_1.fastq sub2_1.fastq sub3_1.fastq sub4_1.fastq sub5_1.fastq sub6_1.fastq sub7_1.fastq sub8_1.fastq > concat_1.fastq
cat sub1_2.fastq sub2_2.fastq sub3_2.fastq sub4_2.fastq sub5_2.fastq sub6_2.fastq sub7_2.fastq sub8_2.fastq > concat_2.fastq

python3 sharedFASTQReads.py -fq1 concat_1.fastq -fq2 concat_2.fastq -o shared_reads.csv 

