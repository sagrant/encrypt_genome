#!/usr/bin/env python3 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import pandas as pd

'''
Plot number of positions shared among eight people in concatenated VCF file 
Input: CSV with number of times a position is shared between more than one person 
'''

class plotPositions():

    def __init__(self, posDf):
        self.posDf = posDf

    def graph(self):
        vals = self.posDf.iloc[:,0].values
        fig, ax = plt.subplots()
        plt.hist(vals, log= True, bins = 15, color = 'black', zorder = 20)
        ax.set_ylabel('Positions (#)')
        ax.set_xlabel('People (#)')
        plt.grid(b = True, which = 'minor', axis = 'both', zorder = 10)
        plt.title('Number of Positions Shared Between People')
        plt.show()

def main():
    #inFile = '/home/sagrant/encrypt_genome/data/shared_positions.csv'
    inFile = 'shared_positions.csv'

    with open(inFile, 'r') as file: 
        df = pd.read_csv(file)

    plotPos = plotPositions(df)
    plotPositions.graph(plotPos)


if __name__ == "__main__":
    main()