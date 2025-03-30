# encrypt_genome

As high throughput genomic sequencing has exploded in popularity, many labs using third party sequencing companies leave their data vulnerable to exploitation. Computational encryption has been proposed in the past, but no method has resolved this issue yet [1]. Our goal is to create a cheap and easy protocol where this data can be encrypted on a molecular level. 

With this protocol, we encrypt DNA from multiple individuals. Genomic DNA is fragmented and pooled, sequenced on the HiSeq Illumina platform, and each read is indexed with a unique barcode. The pooled DNA  cannot be linked to any specific individual. A separate whitelist is built from the identifying barcodes, and this serves as a key to decrypt the genomic pool. This whitelist can be sequenced cheaply on the MiSeq Illumina platform. The pooled DNA and the whitelist are split between parties, preventing either agency from taking advantage of sensitive genomic information. 

<img width="902" alt="image" src="https://github.com/user-attachments/assets/ff446f74-95f7-462f-9dc7-4884081d2182" />

To support this method, I conducted a bioinformatics thought experiment to establish that the pool of fragmented DNA cannot be pieced back together. The aim was to see if it would be possible to assemble a person's genome if it were subsampled and mixed with genomic DNA of several individuals. This workflow mimics the wet lab workflow that was developed in parallel. See the flowchart below for a description of the entire workflow.

![dna_encryption_flowchart](https://github.com/user-attachments/assets/080e415c-64dd-444f-8cb1-d131eaa851c3)

Description of steps:
1. Subsample FASTQ. Start the workflow by downloading several publically available human genomes obtained with Whole Genome Sequencing (WGS). This python script subsamples these files to 300,000,000 reads. This step is repeated 8 times with 8 different FASTQ files.
2. The files generated by the first step are concatenated on the linux command line using the $cat command. At this point, sharedFASTQReads.py can be run to determine how many paired end reads are the same in this concatenated FASTQ file. 
3. The concatenated FASTQ is assembled with the SPAdes assembly software. 
4. Align the contigs output by SPAdes back to the concatenated FASTQ files with minimap2 software. This step generates a SAM file.
5. samtools and bcftools are used to process the minimap2 SAM file output. At this point, sharedContigs.py and assemblyControl.py can be run.
   5.a sharedContigs.py counts the number of identical contigs in the alignment.
   5.b assemblyControl.py is a script that supports a tangential test that was done to support this workflow. For this test, individual alignments are compared to concatenated alignments. An individual alignment refers to an alignment where only one individual's FASTQ reads are aligned to their own contigs. A concatenated alignment refers to an alignment where one individual's FASTQ reads are aligned to contigs generated by running SPAdes with a concatenated FASTQ file containing reads from multiple individuals. assemblyControl.py then compares the number of contigs that were successfully mapped to a read against those that were not mapped to anything. The null hypothesis for this test is that there is no significant difference in the number of unmapped contigs in individual versus concatenated alignments.
6. A Variant Call Format (VCF) file is generated using bcftools. The VCF file format is good for analyzing single nucelotide polymorphisms (SNPs). SNPs could potentially be used to idenitify individuals, so it is important to test if SNPs in the concatenated assembly could be used to decode our encryption scheme.
   6.a sharedPositions.py computes the number of identical SNP positions shared among individuals in the concatenated alignment.
   6.b sharedSNPs.py analyzes the genomic sequence at identical SNP positions and determines if those sequence substitutions or indels are unique enough to identify individuals from the concatenated alignment
   6.c positionDifferences.py compares the SNP positions across individuals to determine if distances between SNPs can be used to identify individuals from the concatenated alignment




1. Grishin, Dennis, Kamal Obbad, and George M. Church. “Data Privacy in the Age of Personal Genomics.” Nature Biotechnology 37, no. 10 (October 2019): 1115–17. https://doi.org/10.1038/s41587-019-0271-3.
