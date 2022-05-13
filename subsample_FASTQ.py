import argparse
import random
import itertools
import numpy as np

'''
Input: any amount of paired-end FASTQ files
Output: FASTQ files subsampled to 300,000,000 reads'''

parser = argparse.ArgumentParser()

parser.add_argument('-i1', '--filename1') #forward strand
parser.add_argument('-i2', '--filename2') #reverse strand
parser.add_argument('-fq1', '--outFile_1') #forward strands concatenated and subsampled
parser.add_argument('-fq2', '--outFile_2') #reverse strands concatenated and subsampled

args = parser.parse_args()


def process(file):
    fullFq = []
    with open(file, 'r') as fileContent:
        for idx, line in enumerate(fileContent): #for loop to store each ID, read, and quality score in nested list 
            if idx % 4 == 0: 
                subsampleLines = []
                subsampleLines.append(line)
            elif idx % 3 == 0: 
                subsampleLines.append(line)
            elif idx % 2 == 0:
                subsampleLines.append(line)
            elif idx % 1 == 0:
                subsampleLines.append(line)
            fullFq.append(subsampleLines)
            

    random.seed(42)
    randomFq = random.sample(fullFq, 30000000) #subsample to 30,000,000 reads 
    compileFq = list(itertools.chain(*randomFq))
    return compileFq


def main():
          
    processFq1 = process(args.filename1)
    processFq2 = process(args.filename2)

    fq1 = np.asarray(processFq1).flatten()
    fq2 = np.asarray(processFq2).flatten()

    #write concatenated paired end FASTQs to new file
    with open(args.outFile_1, 'w') as out1:
        out1.write(''.join(fq1))

    with open(args.outFile_2, 'w') as out2:
        out2.write(''.join(fq2))

if __name__ == "__main__":
    main()