#!/usr/bin/env python3 
import argparse
import numpy as np
import pandas as pd
import allel

'''
Question: how many SNP positions are the same (shared) between individuals? 
Input: concatenated VCF file
Output: CSV file with sample IDs and all of their respective positions 
'''

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--vcfFile') #input VCF

args = parser.parse_args()

class sharedPos():

    def __init__(self, vcf):
        self.vcf = vcf

    def numSamples(self):
        sharedPosList = []
        uniquePos = []
        for pos, ppl in self.vcf.itertuples(index = False):
            if '.' in ppl:
                continue
            elif len(ppl) > 1: #more than one sample is associated with one position
                sharedPosList.append([pos, ppl])
            elif len(ppl) == 1: #only one person is associated with a position
                uniquePos.append([pos, ppl])
        return sharedPosList, uniquePos
    
    def findShared(self, matchList):
        match1 = 0
        match2 = 0
        match3 = 0
        match4 = 0
        match5 = 0
        match6 = 0
        match7 = 0
        match8 = 0
        for pos, sampleList in matchList: 
            if 'sub1' in sampleList: 
                match1 += 1
            if 'sub2' in sampleList: 
                match2 += 1
            if 'sub3' in sampleList: 
                match3 += 1
            if 'sub4' in sampleList: 
                match4 += 1
            if 'sub5' in sampleList: 
                match5 += 1
            if 'sub6' in sampleList: 
                match6 += 1
            if 'sub7' in sampleList: 
                match7 += 1
            if 'sub8' in sampleList: 
                match8 += 1
            else: 
                continue
        return match1, match2, match3, match4, match5, match6, match7, match8

    def groupSNPs(self, snpList):
        SNPdf = pd.DataFrame(snpList, dtype = 'str')
        gb = SNPdf.groupby(SNPdf.iloc[:,1], as_index = False)
        return gb


def main():

    callset = allel.read_vcf(args.vcfFile, fields = '*')

    positions = pd.Series(callset['variants/POS'].flatten())
    people = callset['variants/ID']

    vcfDf = pd.DataFrame([positions, people]).T.rename(columns = {0: 'POS', 1: 'ID'})
    vcfDf['ID'] = vcfDf['ID'].str.split(';')

    shared = sharedPos(vcfDf)

    sharedList, SNPpositions = shared.numSamples()

    val1, val2, val3, val4, val5, val6, val7, val8 = shared.findShared(sharedList)
    
    groupedSamples = shared.groupSNPs(SNPpositions)

    ind1 = groupedSamples.get_group("['sub1']")
    ind2 = groupedSamples.get_group("['sub2']")
    ind3 = groupedSamples.get_group("['sub3']")
    ind4 = groupedSamples.get_group("['sub4']")
    ind5 = groupedSamples.get_group("['sub5']")
    ind6 = groupedSamples.get_group("['sub6']")
    ind7 = groupedSamples.get_group("['sub7']")
    ind8 = groupedSamples.get_group("['sub8']")

    valDict = {'Sample1': [val1, len(ind1)], 'Sample2': [val2, len(ind2)], 'Sample3': [val3, len(ind3)], 'Sample4': [val4, len(ind3)], \
        'Sample5': [val5, len(ind5)], 'Sample6': [val6, len(ind6)], 'Sample7': [val7, len(ind7)], 'Sample8': [val8, len(ind8)]}

    sharedPosDf = pd.DataFrame.from_dict(valDict, orient = 'index').rename(columns = {0: 'Shared Positions', 1: 'Unique Positions'})

    with open('/home/sagrant/encrypt_genome/shared_positions.csv', 'w') as outFile: 
        sharedPosDf.to_csv(outFile, index = False)

if __name__ == "__main__":
    main()
