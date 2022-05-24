#!/usr/bin/env python3 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import pandas as pd

'''
Plot mismatched reads in the concatenated-individual assemblies vs. individual assmeblies
Input: CSV with counts of mismatched reads from six SAM files 
'''


class plotControl():

    def __init__(self, cArray, eArray):
        self.mapped = cArray
        self.errors = eArray

    def visualize(self): 
        width1 = 0.20
        xVals = np.array([1,2])
        
        fig, ax = plt.subplots()

        bar1 = plt.bar(xVals, self.mapped, width = width1, color = 'blue')
        bar2 = plt.bar(xVals + width1, self.errors, width = width1, color = 'red')
        
        ax.set_yticks([0, 1])
        ax.set_xticks([1.0, 2.0, 3.0])
        plt.ylim(0, 4)
        plt.xlim(0, 4)
        plt.show()    

def main():
    inFile = '/home/sagrant/encrypt_genome/data/assembly_control.csv'

    with open(inFile, 'r') as file:
        df = pd.read_csv(file)

    corrArray = df.iloc[:,2].values
    errArray = df.iloc[:,3].values

    vis = plotControl(corrArray, errArray)
    plotControl.visualize(vis)

if __name__ == "__main__":
    main()