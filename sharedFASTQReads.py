#!/usr/bin/env python3
import pandas as pd 
import argparse
import pyfastx


'''
Question: How many reads are identical in the concatenated FASTQ file?
Input: paired-end concatenated FASTQ files
Output: CSV file with counts of each read'''


parser = argparse.ArgumentParser()

parser.add_argument('-fq1', '--file1') #concatenated forward FASTQ
parser.add_argument('-fq2', '--file2') #concatenated reverse FASTQ
parser.add_argument('-o', '--output') #csv with reads, counts of each read

args = parser.parse_args()


class readCount():

    def __init__(self, FASTQ):
        self.dfList = FASTQ

    def callReads(self):
        readDf = pd.DataFrame(self.dfList).rename(columns = {0: 'ID', 1: 'Sequence'})
        gb = readDf.groupby('ID') #group reads by the person's FASTQ it is associated with
        counts = []
        #for loop to drop duplicate reads within each group --> only count duplicate reads between samples
        for name, group in gb: 
            noDups = group.drop_duplicates(subset = ['Sequence', 'ID'], keep = 'first')
            counts.append(noDups)
            
        countReads = pd.concat(counts)
        vCounts = countReads.value_counts(subset = 'Sequence') #get counts of each read 
        return vCounts

def main():

    dfList = []
    for id, seq, qual in pyfastx.Fastq(args.file1, build_index = False):
        splitID1 = id.partition('.')[0].rstrip()
        dfList.append([splitID1, seq])

    for id, seq, qual in pyfastx.Fastq(args.file2, build_index = False): 
        splitID2 = id.partition('.')[0].rstrip()
        dfList.append([splitID2, seq])

    reads = readCount(dfList) 
    groups = reads.callReads()

    #write raw values to CSV file 
    with open(args.output, 'w') as test: 
        groups.to_csv(test, index = False)


if __name__ == "__main__":
    main()