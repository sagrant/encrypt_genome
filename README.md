# encrypt_genome

As high throughput genomic sequencing has exploded in popularity, many labs using third party sequencing companies leave their data vulnerable to exploitation. Computational encryption has been proposed in the past, but no method has resolved this issue yet [1]. Our goal is to create a cheap and easy protocol where this data can be encrypted on a molecular level. 

With this protocol, we encrypt DNA from multiple individuals. Genomic DNA is fragmented and pooled, sequenced on the HiSeq Illumina platform, where each read is indexed with a unique barcode. The pooled DNA  cannot be linked to any specific individual. A separate whitelist is built from the identifying barcodes that serves as a key to decrypt the genomic pool. This whitelist can be sequenced cheaply, on the MiSeq Illumina platform. The pooled DNA and the whitelist are split between parties, preventing either agency from taking advantage of this information. 

<img width="902" alt="image" src="https://github.com/user-attachments/assets/ff446f74-95f7-462f-9dc7-4884081d2182" />

To support this method, I conducted a bioinformatics thought experiment to establish that the pool of fragmented DNA cannot be pieced back together. 

1. Grishin, Dennis, Kamal Obbad, and George M. Church. “Data Privacy in the Age of Personal Genomics.” Nature Biotechnology 37, no. 10 (October 2019): 1115–17. https://doi.org/10.1038/s41587-019-0271-3.
