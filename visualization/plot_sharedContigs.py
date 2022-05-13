#!/usr/bin/env python3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

'''
Plot number of reads shared between people in concatenated paired-end FASTQ files.
'''

inFile = '/home/sagrant/encrypt_genome/data/shared_contigs.csv'
#inFile = 'shared_contigs.csv'

with open(inFile, 'r') as file: 
    df = pd.read_csv(file, usecols = [0], squeeze = True, engine = 'c')

contigData = df.values[1:-1]

fig, ax = plt.subplots()
plt.hist(contigData, log = True, density = True, color = 'black', zorder = 20)

# ax.set_ylabel('Contigs (#)')
# ax.set_xlabel('People (#)')
# #ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
# ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
# ax.tick_params(axis = 'both', which = 'both', length = 1)

# plt.xlim(0.8, 8.7)
# plt.grid(b = True, which = 'minor', axis = 'both', zorder = 10)
# plt.title('Number of Shared Contigs in Merged Assembly')
plt.show()
#plt.savefig('shared_person2contig.png', dpi = 600)
#plt.savefig('shared_person2contig_lc.png', dpi = 600)
#plt.savefig('shared_person2contig_6merged.png', dpi = 600)