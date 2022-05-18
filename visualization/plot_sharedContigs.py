#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

'''
Plot number of reads shared between people in concatenated paired-end FASTQ files.
'''

class plotShared():
    
    def __init__(self, s):
        self.contigSeries = s

    def plotHist(self):
        fig, ax = plt.subplots()
        plt.hist(self.contigSeries, log = True, density = True, color = 'black', zorder = 20)
        ax.set_ylabel('Contigs (#)')
        ax.set_xlabel('People (#)')

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
        ax.tick_params(axis = 'both', which = 'both', length = 1)

        plt.xlim(0.8, 8.7)
        plt.grid(b = True, which = 'minor', axis = 'both', zorder = 10)
        plt.title('Number of Shared Contigs in Merged Assembly')
        plt.show()

def main():
    
    inFile = '/home/sagrant/encrypt_genome/data/shared_contigs.csv'

    with open(inFile, 'r') as file: 
        df = pd.read_csv(file, usecols = [0], squeeze = True, engine = 'c')

    contigData = df.values[1:-1]
    graph = plotShared(contigData)
    plotShared.plotHist(graph)
if __name__ == "__main__":
    main()