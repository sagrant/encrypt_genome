#!/usr/bin/env python3
import pandas as pd
import numpy as np
import allel
import argparse 

'''
Question: are SNPs at shared positions idenitical between people?
Input: concatenated VCF file 
Output: counts of SNPs that are identical between people, at identical positions
'''

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--filename') #input VCF file 

args = parser.parse_args()


def main():
    callset = allel.read_vcf(args.filename, fields='*')

    positions = pd.Series(callset['variants/POS'].flatten())
    variants = callset['variants/ALT']

    varDf = pd.DataFrame(variants).rename(columns = {0: 'alt1', 1: 'alt2', 2: 'alt3'}) #(pos and alt)
    df = pd.concat([positions, varDf], axis = 1).rename(columns = {0: 'pos'}) #(pos and alt)
    gb = df.groupby('pos').nunique() #(pos and alt)

    with open('/home/sagrant/encrypt_genome/data/shared_SNPs.csv') as SNPsOut:
        gb.to_csv(SNPsOut, index = False)

if __name__ == "__main__":
    main()