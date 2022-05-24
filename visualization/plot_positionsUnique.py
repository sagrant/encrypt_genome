#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches

'''
Plot number of positions shared versus unique among eight people in concatenated VCF file 
Input: CSV with number of times a position is shared and number of times a position is unique for eight people
'''

class plotUnique():

    def __init__(self, df):
        self.posDf = df

    def parse(self):
        shared = self.posDf.iloc[:,0].values
        unique = self.posDf.iloc[:,1].values
        return shared, unique

    def graph(self, shareVales, uniqueValues):
        fig, ax = plt.subplots()
        xVals = np.arange(8)
        wdth = 0.25
        bar1 = ax.bar(xVals, shareVales, wdth, color = 'black', align='center', zorder = 20)
        bar2 = ax.bar(xVals + wdth, uniqueValues, wdth, color = 'green', align='center', zorder = 20)
        ax.set_ylabel('Positions (#)')
        ax.set_xlabel('Person')
        ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8'])
        plt.show()


def main():
    with open('/home/sagrant/encrypt_genome/data/unique_positions.csv', 'r') as inFile:
        df = pd.read_csv(inFile)

    Unique = plotUnique(df)
    sh, uq = Unique.parse()
    uniqueVsShared = Unique.graph(sh, uq)

if __name__ == "__main__":
    main()