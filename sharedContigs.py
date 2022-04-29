#!/usr/bin/env python3
import pandas as pd
import numpy as np
import argparse

'''
Question: How many contigs are identical in the assembly?
Input: paired end concatenated FASTQ files
Output: CSV file with counts of each contig'''

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--filename1') #input sam file

args = parser.parse_args()

class countContigs():

    def __init__(self, df):
        self.contigDf = df 

    def process(self):
        samples = []
        for person, contigs in self.contigDf.itertuples(index = False):
            sampleName = person.partition('.')[0].rstrip()
            samples.append(sampleName)

        self.contigDf['People'] == samples

        gb = self.contigDf.groupby('Contig', as_index= True).nunique()
        gb.to_csv(args.outFile, index = False)
        return gb
    

def main():
    with open(args.filename1, 'r') as sam: 
        dataList = []
        for line in sam: 
            if not line.startswith('@'):
                splitLine = line.split('\t')
                dataList.append([splitLine[0], splitLine[2]]) # choose which fields you want in df 
        
        df = pd.DataFrame(dataList).rename(columns= {0: 'People', 1: 'Contig'})
    
    contigs = countContigs(df)
    groupContigs = contigs.process()

    with open('/home/sagrant/encrypt_genome/data/shared_contigs.csv', 'w') as out: 
        groupContigs.to_csv(out, index= False)


if __name__ == "__main__":
    main()