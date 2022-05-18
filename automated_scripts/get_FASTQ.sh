#!/bin/bash
#automates assmebly process of downloading FASTQ files

wget=/usr/bin/wget

FASTQ1_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1044320/ERR1044320_1.fastq.gz'
FASTQ1_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1044320/ERR1044320_2.fastq.gz'
FASTQ2_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/001/ERR1044331/ERR1044331_1.fastq.gz'
FASTQ2_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/001/ERR1044331/ERR1044331_2.fastq.gz'
FASTQ3_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/005/ERR1044655/ERR1044655_1.fastq.gz'
FASTQ3_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/005/ERR1044655/ERR1044655_2.fastq.gz'
FASTQ4_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1044680/ERR1044680_1.fastq.gz'
FASTQ4_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1044680/ERR1044680_2.fastq.gz'
FASTQ5_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/008/ERR1044778/ERR1044778_1.fastq.gz'
FASTQ5_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/008/ERR1044778/ERR1044778_2.fastq.gz'
FASTQ6_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/002/ERR1044972/ERR1044972_1.fastq.gz'
FASTQ6_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/002/ERR1044972/ERR1044972_2.fastq.gz'
FASTQ7_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1045020/ERR1045020_1.fastq.gz'
FASTQ7_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1045020/ERR1045020_2.fastq.gz'
FASTQ8_1='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1045040/ERR1045040_1.fastq.gz'
FASTQ8_2='ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR104/000/ERR1045040/ERR1045040_2.fastq.gz'

wget --output-document sample1_1.fastq.gz $FASTQ1_1
wget --output-document sample1_2.fastq.gz $FASTQ1_2
wget --output-document sample2_1.fastq.gz $FASTQ2_1
wget --output-document sample2_2.fastq.gz $FASTQ2_2
wget --output-document sample3_1.fastq.gz $FASTQ3_1
wget --output-document sample3_2.fastq.gz $FASTQ3_2
wget --output-document sample4_1.fastq.gz $FASTQ4_1
wget --output-document sample4_2.fastq.gz $FASTQ4_2
wget --output-document sample5_1.fastq.gz $FASTQ5_1
wget --output-document sample5_2.fastq.gz $FASTQ5_2
wget --output-document sample6_1.fastq.gz $FASTQ6_1
wget --output-document sample6_2.fastq.gz $FASTQ6_2
wget --output-document sample7_1.fastq.gz $FASTQ7_1
wget --output-document sample7_2.fastq.gz $FASTQ7_2
wget --output-document sample8_1.fastq.gz $FASTQ8_1
wget --output-document sample8_2.fastq.gz $FASTQ8_2

gunzip *.gz

