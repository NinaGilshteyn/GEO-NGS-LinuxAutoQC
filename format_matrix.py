Written by Nina Gilshteyn, M.S.

import pandas as pd
import argparse

import numpy as np

from scipy.io import mmread




### The GEO accession number is the common component of the file name for the gene features, cell barcodes, and count matrix. 
### This code loops through the  .mtx files in the directory 
### the full filename for 

parser = argparse.ArgumentParser(description = 'input filename')
parser.add_argument('filename', help = 'dfname in directory')
args = parser.parse_args()

    
file = args.filename

print(file)

### read in matrix
df = mmread(file)

### modify file name to have the GEO assec

#_matrix.mtx 


basename = file[:-11]
barcodes_ = basename + '_barcodes.tsv'
gens = basename + '_genes.tsv'
#print(df.head(3))


### read in matrix
df = mmread(file)
### read in barcodes and geens 

genes = pd.read_csv(gens, sep = '\t', header = None)
#genes1 = genes.iloc[:1]
#genes2 = genes.iloc[:2]

print(genes.head(3))
#print(genes1.head(3))
#print(genes2.head(3))

genes.columns = ['transcriptID', 'GeneName']

### optional if there are duplicate names
#genes['transcriptID-GeneName'] = genes['transcriptID'] + '-' + genes['GeneName']

barcodes = pd.read_csv(barcodes_, sep = '\t', header = None)
barcodes.columns=['barcodes']

df = df.toarray()
df = pd.DataFrame(df,index=genes['transcriptID-GeneName'], columns=barcodes['barcodes'])


print(df.head(3))
newfile = file[:-4]
print(newfile)
print('transposed data')

df = df.T
print(df.head(3))
df.to_csv(f'{newfile}_df.csv')
genes.to_csv(f'{newfile}_genes.csv')


