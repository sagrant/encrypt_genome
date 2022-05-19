#!/bin/bash
#automate_alignment.sh 
#automates alignment for all eight people

set -e #exit immediately if anything returns non-zero status

# genome=~/encrypt_genome/human_g1k_v37.fasta
genome=~/dna_privacy/human_g1k_v37.fasta


#for fq1 in ~/encrypt_genome/*_1.fastq
# for fq1 in ~/dna_privacy/*_1.fastq
#     do
#     #print filenames as we iterate through (probably not necessary for final draft)
#     base=$(basename $fq1 _1.fastq)
#     echo "base name is $base"
#     #use base variable to access input files 
#     # fq1=~/encrypt_genome/${base}_1.fastq
#     # fq2=~/encrypt_genome/${base}_2.fastq
#     fq1=~/dna_privacy/${base}_1.fastq
#     fq2=~/dna_privacy/${base}_2.fastq
#     #output files 
#     # sam=~/encrypt_genome/${base}.aligned.sam
#     # bam=~/encrypt_genome/${base}.aligned.bam
#     # sorted_bam=~/encrypt_genome/${base}.aligned.sorted.bam
#     # raw_bcf=~/encrypt_genome/${base}_raw.bcf
#     # variants=~/encrypt_genome/${base}_variants.vcf
#     # final_variants=~/encrypt_genome/${base}_final_variants.vcf 
#     sam=~/dna_privacy/${base}.aligned.sam
#     bam=~/dna_privacy/${base}.aligned.bam
#     sorted_bam=~/dna_privacy/${base}.aligned.sorted.bam
#     raw_bcf=~/dna_privacy/${base}_raw.bcf
#     variants=~/dna_privacy/${base}_variants.vcf
#     final_variants=~/dna_privacy/${base}_final_variants.vcf 

#     ./minimap2/minimap2 -ax sr -t 40 $genome $fq1 $fq2 > $sam
#     ./samtools-1.15.1/samtools view -S -b $sam > $bam
#     ./samtools-1.15.1/samtools sort -o $sorted_bam $bam
#     ./samtools-1.15.1/samtools index $sorted_bam
#     ./bcftools-1.15.1/bcftools mpileup -O b -o $raw_bcf -f $genome $sorted_bam
#     ./bcftools-1.15.1/bcftools call --ploidy 2 -m -v -o $variants $raw_bcf 
#     ./bcftools-1.15.1/misc/vcfutils.pl varFilter $variants > $final_variants

#TRY: 
    ./bcftools-1.15.1/bcftools annotate $final_variants --set-id ${base} -o ${base}.ids.vcf
    ./bcftools-1.15.1/bcftools view *.ids.vcf -Oz -o ${base}.vcf.gz
    ./bcftools-1.15.1/bcftools index ${base}.vcf.gz 
    
    done

./bcftools-1.15.1/bcftools index *.vcf.gz 
./bcftools-1.15.1/bcftools merge *vcf.gz -o concat.vcf 

# working:
# ./bcftools-1.15.1/bcftools annotate sub1_final_variants.vcf --set-id 'sub1' -o sub1_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub2_final_variants.vcf --set-id 'sub2' -o sub2_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub3_final_variants.vcf --set-id 'sub3' -o sub3_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub4_final_variants.vcf --set-id 'sub4' -o sub4_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub5_final_variants.vcf --set-id 'sub5' -o sub5_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub6_final_variants.vcf --set-id 'sub6' -o sub6_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub7_final_variants.vcf --set-id 'sub7' -o sub7_0.vcf
# ./bcftools-1.15.1/bcftools annotate sub8_final_variants.vcf --set-id 'sub8' -o sub8_0.vcf


# echo "working w sub1"
# ./bcftools-1.15.1/bcftools view sub1_0.vcf -Oz -o sub1.vcf.gz
# echo "working w sub2"
# ./bcftools-1.15.1/bcftools view sub2_0.vcf -Oz -o sub2.vcf.gz
# echo "working w sub3"
# ./bcftools-1.15.1/bcftools view sub3_0.vcf -Oz -o sub3.vcf.gz
# echo "working w sub4"
# ./bcftools-1.15.1/bcftools view sub4_0.vcf -Oz -o sub4.vcf.gz
# echo "working w sub5"
# ./bcftools-1.15.1/bcftools view sub5_0.vcf -Oz -o sub5.vcf.gz
# echo "working w sub6"
# ./bcftools-1.15.1/bcftools view sub6_0.vcf -Oz -o sub6.vcf.gz
# echo "working w sub7"
# ./bcftools-1.15.1/bcftools view sub7_0.vcf -Oz -o sub7.vcf.gz
# echo "working w sub8"
# ./bcftools-1.15.1/bcftools view sub8_0.vcf -Oz -o sub8.vcf.gz

# echo "index"
# ./bcftools-1.15.1/bcftools index sub1.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub2.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub3.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub4.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub5.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub6.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub7.vcf.gz 
# ./bcftools-1.15.1/bcftools index sub8.vcf.gz 

# echo "merge"
# ./bcftools-1.15.1/bcftools merge *vcf.gz -o concat.vcf 