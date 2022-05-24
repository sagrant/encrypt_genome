#!/usr/bin/env python3 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import pandas as pd

'''
Plot difference between SNP positions for each person
Input: CSV with distances between positions for each person in the concatenated VCF 
'''

class plotDifferences():

    def __init__(self, df):
        self.posDf = df

    def graph(self):
        vals = self.posDf
        fig, ax = plt.subplots()
        fig = vals.boxplot(fontsize = 11, showmeans = True, color=dict(boxes='r', whiskers='r', medians='r', caps='r'),
             boxprops=dict(linestyle='-', linewidth=1.5),
             flierprops=dict(linestyle='-', linewidth=1.5),
             medianprops=dict(linestyle='-', linewidth=1.5),
             whiskerprops=dict(linestyle='-', linewidth=1.5),
             capprops=dict(linestyle='-', linewidth=1.5),
             showfliers=False, grid=True, rot=0,)
        plt.xlabel('Person', fontdict = {'fontsize' : 14})
        plt.ylabel('Position Differences', fontdict = {'fontsize' : 16})
        fig.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
        fig.set_xticklabels(['1','2', '3', '4', '5', '6', '7', '8'])
        plt.title('Distance Between Variant Positions', fontdict = {'fontsize' : 17})
        plt.show()

def main():
    inFile = '/home/sagrant/encrypt_genome/data/position_diff.csv'

    with open(inFile, 'r') as file:
        df = pd.read_csv(file)

    plotDiff = plotDifferences(df)
    plotDifferences.graph(plotDiff)

if __name__ == "__main__":
    main()