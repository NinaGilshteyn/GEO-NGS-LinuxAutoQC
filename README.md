# GEO-NGS-LinuxAutoDataProcessing

Automated bash and Python pipeline for reformatting raw scRNA-seq data downloaded from [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/) into analysis-ready CSV files — eliminating the manual formatting overhead before downstream ScanPy analysis.

**Demo:** [ninagilshteyn.github.io/GEO-NGS-LinuxAutoDataProcessing](https://ninagilshteyn.github.io/GEO-NGS-LinuxAutoDataProcessing)

---

## Overview

When downloading scRNA-seq datasets from NCBI GEO, data typically arrives as a set of sparse matrix files in the standard 10x Genomics format:

- `matrix.mtx` — sparse count matrix
- `barcodes.tsv` — cell barcode identifiers
- `features.tsv` — gene feature names

Manually reformatting these files for each sample is tedious and error-prone, especially when working with many datasets. This pipeline automates the entire process: looping through each matrix file, submitting a job on the Hoffman2 HPC cluster, and converting each set of `.mtx` / `.tsv` files into a single, labeled `.csv` file with genes as columns and cells as rows.

---

## Repository structure

```
GEO-NGS-LinuxAutoDataProcessing/
├── bash_loop_submitter.sh   # Loops through matrix files and submits a job for each
├── format_mtx.sh            # Job script: sets up conda environment and runs the Python script
├── format_matrix.py         # Converts .mtx + .tsv files into a labeled .csv
├── index.html               # Demo page
└── LICENSE
```

---

## File descriptions

### `bash_loop_submitter.sh`
The entry point. Iterates over all `matrix.mtx` files in the working directory and submits a separate HPC job for each one via `format_mtx.sh`, passing the matrix file path as a variable.

### `format_mtx.sh`
The job script submitted to the Hoffman2 cluster. Specifies compute requirements, creates a conda environment, and calls `format_matrix.py` with the matrix file variable passed in from `bash_loop_submitter.sh`.

### `format_matrix.py`
The core processing script. Takes the matrix file path as input, resolves the corresponding `barcodes.tsv` and `features.tsv` file paths from the same directory, loads the sparse matrix, assembles a labeled data frame, transposes it so that genes are columns and cells are rows, and exports the result as a `.csv` file.

---

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/NinaGilshteyn/GEO-NGS-LinuxAutoDataProcessing.git
cd GEO-NGS-LinuxAutoDataProcessing
```

### 2. Organize your GEO data
Place your downloaded GEO sample directories in your working directory. Each sample folder should contain:
```
matrix.mtx
barcodes.tsv
features.tsv
```

### 3. Run the submitter
```bash
bash bash_loop_submitter.sh
```
This will loop through each `matrix.mtx` file and submit a job to the Hoffman2 cluster for each one. Each job will produce a `.csv` file in the same directory as the input files.

---

## Requirements

- Hoffman2 HPC cluster (UCLA) or compatible SLURM environment
- Conda
- Python 3
- ScanPy
- Standard 10x Genomics GEO download format (`matrix.mtx`, `barcodes.tsv`, `features.tsv`)

---

## Output

For each input sample, the pipeline produces a single `.csv` file where:
- **Rows** = cells (barcodes)
- **Columns** = genes (features)

This format is directly importable into ScanPy, R, or any downstream analysis tool.

---

## Author

**Nina Gilshteyn, M.S.**  
Bioinformatics Specialist & Post-Graduate Researcher, Deeds Lab — UCLA  
[ninagilshteyn.github.io](https://ninagilshteyn.github.io) · [github.com/NinaGilshteyn](https://github.com/NinaGilshteyn)
