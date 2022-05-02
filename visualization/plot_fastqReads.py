#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

'''
Plot number of reads shared between people in concatenated paired-end FASTQ files.
'''

inFile = '/home/sagrant/encrypt_genome/data/shared_reads.csv'

with open(inFile, 'r') as file: 
    df = pd.read_csv(file, usecols = [0], squeeze = True, engine = 'c')

print(df)
data = df.values
fig, ax = plt.subplots()
plt.hist(data, bins = 20, color = 'black', log = True, zorder = 20)

ax.set_yticks([10e5, 10e6, 10e7, 10e8])
ax.set_xticks([1, 2, 3, 4, 5, 6])
ax.tick_params(axis = 'both', which = 'both', length = 1)
ax.set_ylabel('Shared Reads (#)')
ax.set_xlabel('People (#)')

plt.grid(b = True, which = 'minor', axis = 'both', zorder = 10)
plt.yticks([10e5, 10e6, 10e7, 10e8])

plt.title('Number of Shared Reads in Merged FASTQ File')
plt.show() #view figure
#plt.savefig('shared_reads_fastq.png', dpi = 600) #uncomment to save figure 
