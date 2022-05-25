#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches

'''
Plot histogram displaying how many people share identical SNPs at the same position
Input: CSV with counts of shared SNPs  
'''

class shareSNP():

    def __init__(self, df):
        self.shareDf = df

    def visualize(self): 
        vals = self.shareDf.iloc[:,0].values
        fig, ax = plt.subplots()

        n, Nbins, patch = plt.hist(vals, log = True, color = 'black', zorder = 10)#, density = True)

        xtiks = [(Nbins[idx+1] + value)/2 for idx, value in enumerate(Nbins[:-1])]
        plt.xticks(xtiks)

        ax.set_ylabel('Positions (#)')
        ax.set_xlabel('Unique Variants (#)')
        ax.tick_params(axis = 'both', which = 'both', length = 1)
        plt.grid(b = True, which = 'minor', axis = 'both', zorder = 10)

        ax.set_xticks([1.15, 2.05, 2.95])
        ax.set_xticklabels(['1', '2', '3'])

        plt.xlim(0.9, 3.2)
        plt.title('Number of Positions with Unique Variants')
        plt.show()


def main():
    inFile = '/home/sagrant/encrypt_genome/data/shared_SNPs.csv'

    with open(inFile, 'r') as file:
        df = pd.read_csv(file)

    plotShared = shareSNP(df)
    plotShared.visualize()

if __name__ == "__main__":
    main()