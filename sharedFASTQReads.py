#!/usr/bin/env python3
import pandas as pd 
import argparse
import numpy as np
import pyfastx


'''sharedFASTQReads.py --> answers: How many reads are identical in the concatenated FASTQ file?
input: paired end concatenated FASTQ files
output: CSV file with counts of each read'''


parser = argparse.ArgumentParser()

parser.add_argument('-fq1', '--file1') #concatenated forward FASTQ
parser.add_argument('-fq2', '--file2') #concatenated reverse FASTQ
parser.add_argument('-o', '--output') #csv with reads, counts of each read

args = parser.parse_args()


class readCount():
    '''
    Input: FASTQ file 
    Returns: CSV file with each read and # times read appears in FASTQ
    '''

    def __init__(self, FASTQ):
        self.dfList = FASTQ

    def callReads(self):
        '''
        Input: merged FASTQ file 
        Output: Dataframe with each read and count of each read 
        '''
        readDf = pd.DataFrame(self.dfList).rename(columns = {0: 'ID', 1: 'Sequence'})
        gb = readDf.groupby('ID')
        counts = []
        for name, group in gb: 
            noDups = group.drop_duplicates(subset = ['Sequence', 'ID'], keep = 'first')
            counts.append(noDups)
            
        countReads = pd.concat(counts)
        vCounts = countReads.value_counts(subset = 'Sequence')
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

    with open(args.output, 'w') as test: #write raw values to CSV file 
        groups.to_csv(test, index = False)


if __name__ == "__main__":
    main()