Written by Nina Gilshteyn, M.S.

import pandas as pd
import argparse

import numpy as np

from scipy.io import mmread




### The GEO accession number is the common component of the file name for the gene features, cell barcodes, and count matrix. 
### This code loops through the  .mtx files in the directory 
### the full filename for matrix is read into this file because 
### that is what the bash loop iterates through. 


parser = argparse.ArgumentParser(description = 'input filename')
parser.add_argument('filename', help = 'dfname in directory')
args = parser.parse_args()

### this is the filename for the specific matrix file for the accession number    
file = args.filename


print(file)


### modify file name to have the GEO accession name for string modifcation

basename = file[:-11]  # removing the 'matrix.mtx' from the file name


## use the accession number stored in the basename string to the following
## strings to store the names of the others files into memory

barcodes_ = basename + '_barcodes.tsv'
gens = basename + '_genes.tsv'
#print(df.head(3))


### read in matrix
df = mmread(file)
########### read in barcodes and genes using the modified strings

genes = pd.read_csv(gens, sep = '\t', header = None)
print(genes.head(3))  # check how many columns there are before renaming them

genes.columns = ['transcriptID', 'GeneName']

### optional if there are duplicate names
#genes['transcriptID-GeneName'] = genes['transcriptID'] + '-' + genes['GeneName']



barcodes = pd.read_csv(barcodes_, sep = '\t', header = None)
barcodes.columns=['barcodes']


### combined the matrix, gene, and barcodes into one script

df = df.toarray()
df = pd.DataFrame(df,index=genes['transcriptID-GeneName'], columns=barcodes['barcodes'])

print(df.head(3))
newfile = file[:-4]
print(newfile)
print('transposed data')
df = df.T  # ensure the columns are genes and rows are cells
print(df.head(3))
df.to_csv(f'{newfile}_df.csv') # write formatted data onto disk 



