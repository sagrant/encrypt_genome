import argparse
import random
import itertools
import numpy as np
import sys

'''
Input: any amount of paired-end FASTQ files
Output: FASTQ files subsampled to 300,000,000 reads'''

parser = argparse.ArgumentParser()

parser.add_argument('-i1', '--filename1') #forward strand
parser.add_argument('-i2', '--filename2') #reverse strand
parser.add_argument('-fq1', '--outFile_1') #forward strands merged and subsampled
parser.add_argument('-fq2', '--outFile_2') #reverse strands merged and subsampled

args = parser.parse_args()


class subsample():

    def __init__(self, file1, file2):
        self.content1 = file1
        self.content2 = file2

    def execute(self):
        compile1 = []
        compile2 = []
        #for loop to store ID, seq, and quality score of each read in nested list
        for line in range(0, len(self.content1), 4): 
            forward = self.content1[line: line+4]
            reverse = self.content2[line: line+4]
            compile1.append(forward)
            compile2.append(reverse)

        random.seed(42)
        random_1 = random.sample(compile1, 30000000) 
        random.seed(42)
        random_2 = random.sample(compile2, 30000000)
        combo1 = list(itertools.chain(*random_1))
        combo2 = list(itertools.chain(*random_2))
        return combo1, combo2 


def main():

    with open(args.filename1, 'r') as file_1:
        f1 = file_1.read()
        fastq1 = f1.split('\n')

    with open(args.filename2, 'r') as file_2: 
        f2 = file_2.read()
        fastq2 = f2.split('\n')
          
    process = subsample(fastq1, fastq2)
    combo1, combo2 = process.execute()

    #write concatenated paired end FASTQs to new file
    with open(args.outFile_1, 'w') as out1:
        out1.write('\n'.join(str(i) for i in combo1))

    with open(args.outFile_2, 'w') as out2:
        out2.write('\n'.join(str(i) for i in combo2))

    sys.exit()

if __name__ == "__main__":
    main()