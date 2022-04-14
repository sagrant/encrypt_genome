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
    Returns: plot where X = number of people read was found in, and 
    Y = number of times a repeated read was found in X people 
    '''

    def __init__(self, FASTQ):
        self.dfList = FASTQ

    def callReads(self):
        '''
        Input: merged FASTQ file 
        Output: Dataframe with each read and count of each read 
        '''
        readDf = pd.DataFrame(self.dfList).rename(columns = {0: 'id', 1: 'sequence'})
        #seqs = readDf.iloc[:,1]
        # dups = seqs.duplicated()  DUPS ARE PRESENT
        # counter = 0
        # for d in dups: 
        #     if d == True:
        #         print(d)
        #         break
        #gb = readDf.groupby('sequence').agg({'sequence': 'nunique'})#.reset_index()
        gb = readDf.groupby(['id', 'sequence'])['sequence'].count() #NEXT TRY SIZE AND COUNT /SEE IF THERE ARE DUPS BETWEEN SAMPLES
        # print(readDf)
        #gb = readDf.value_counts(subset=['id', 'sequence'], sort = False)
        print(gb)  
        print(max(gb))
        return gb

def main():

    dfList = []
    for id, seq, qual in pyfastx.Fastq(args.file1, build_index = False):
        splitID1 = id.partition('.')[0].rstrip()
        dfList.append([splitID1, seq])

    for id, seq, qual in pyfastx.Fastq(args.file2, build_index = False): #OMIT TO SAVE TIME DO NOT FORGET TO UNCOMMENT LATER 
        splitID2 = id.partition('.')[0].rstrip()
        dfList.append([splitID2, seq])

    reads = readCount(dfList) 
    groups = reads.callReads()

    with open(args.output, 'w') as test: #write raw values to CSV file 
        groups.to_csv(test, index = False)


if __name__ == "__main__":
    main()