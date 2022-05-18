#!/usr/bin/env python3
import pandas as pd
import numpy as np
import argparse
import allel

'''
Question: how close are positions within each person? 
Input: concatenated VCF file
Output: CSV file with distances between SNPs for each person'''

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--vcfFile') #concat VCF file

args = parser.parse_args()


class parseDistance():

    def __init__(self, df):
        self.vcf = df

    def parse(self, sampleName):
        countPos = []
        for pos, ppl in self.vcf.itertuples(index = False): 
            if sampleName in ppl:
                countPos.append(pos)
        return countPos
    
    def getDifference(self, result):
        diff = pd.Series(result, dtype = 'int32').sort_values().diff()
        return diff 

def main():

    callset = allel.read_vcf(args.vcfFile, fields = '*')
    
    positions = pd.Series(callset['variants/POS'].flatten())
    samples = callset['variants/ID']

    vcfDf = pd.DataFrame([positions, samples]).T.rename(columns = {0:'Pos', 1: 'sampleIDs'})
    vcfDf['samples'] = vcfDf['sampleIDs'].str.split(';')
    vcfDf.drop('sampleIDs', axis = 1, inplace = True)
    
    posDifference = parseDistance(vcfDf)

    name1, name2, name3, name4, name5, name6, name7, name8 = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8']

    countDiff1 = posDifference.parse(name1)
    countDiff2 = posDifference.parse(name2)
    countDiff3 = posDifference.parse(name3)
    countDiff4 = posDifference.parse(name4)
    countDiff5 = posDifference.parse(name5)
    countDiff6 = posDifference.parse(name6)
    countDiff7 = posDifference.parse(name7)
    countDiff8 = posDifference.parse(name8)

    diffOut1 = posDifference.getDifference(countDiff1)
    diffOut2 = posDifference.getDifference(countDiff2)
    diffOut3 = posDifference.getDifference(countDiff3)
    diffOut4 = posDifference.getDifference(countDiff4)
    diffOut5 = posDifference.getDifference(countDiff5)
    diffOut6 = posDifference.getDifference(countDiff6)
    diffOut7 = posDifference.getDifference(countDiff7)
    diffOut8 = posDifference.getDifference(countDiff8)

    diffDf = pd.DataFrame([diffOut1, diffOut2, diffOut3, diffOut4, diffOut5, diffOut6, diffOut7, diffOut8]).T
    
    with open('/home/sagrant/encrypt_genome/data/position_diff.csv', 'w') as distanceOut: 
        diffDf.to_csv(distanceOut, index = False)

if __name__ == "__main__":
    main()