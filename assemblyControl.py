#!/usr/bin/env python3 
import argparse
import numpy as np
import pandas as pd

'''
Question: are there more or fewer mismatched reads in individual-concatenated assemblies 
vs. individual assemblies on their own?
Input: SAM files resulting from SPAdes assemblies
 - sample1 individual assembly
 - sample5 individual assembly 
 - sample6 individual assembly
 - sample1 aligned to concat contigs
 - sample5 aligned to concat contigs
 - sample6 aligned to concat contigs 
Output: counts of asterisks (aka unmapped reads) in each SAM file'''

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--filename', nargs = '+') #input SAM files 
parser.add_argument('-o', '--output_file_1') #CHANGE TO DIRECT FILE WRITE !

args = parser.parse_args()

def parseSAM(sam):
    dataList = []
    for line in sam:
        if not line.startswith('@'):
            splitLine = line.split('\t')
            dataList.append([splitLine[0], splitLine[2]]) # choose which fields you want in df (2 = contigs)
    return dataList


class control():

    def __init__(self, data):
        self.dataList = data 

    def counter(self, names):
        NODEcount = 0
        MISScount = 0
        nodes = []
        missed = []
        for ref, contig in self.dataList:
            if contig.startswith('NODE'):
                NODEcount += 1
            elif contig.startswith('*'):
                MISScount += 1

        nodes.append(NODEcount)
        missed.append(MISScount)

        return nodes, missed

    def calculate(self, num, total):
        temp = []
        npnum = np.asarray(num, dtype = np.int64)
        for x in npnum:
            frac = x/total
            npFrac = np.append(temp, frac)
        flatFrac = npFrac.flatten()
        return flatFrac


def main():
    nameList = []
    countList = []
    for samFile in args.filename: 
        with open(samFile, 'r') as sam: 
            nameList.append(sam.name)
            dataList = parseSAM(sam)

        dataCount = control(dataList)

        nodes, missed = dataCount.counter(nameList)

        total = sum(nodes + missed)
        xNodes = dataCount.calculate(nodes, total) 
        xMissed = dataCount.calculate(missed, total)
    
        countList.append([nodes, missed, xNodes, xMissed, total])

    countDf = pd.DataFrame(countList, index = nameList).rename(columns = {0:'CORRECT MAP', 1:'ERROR', 2: 'FRACTION CORR', 3: 'FRACTION MISSED', 4: 'TOTAl'})

    with open('/home/sagrant/encrypt_genome/data/assembly_control.csv', 'w') as controlOut:
        countDf.to_csv(controlOut, index = False)

if __name__ == "__main__":
    main()