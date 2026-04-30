#!/bin/bash

# Written by Nina Gilshteyn, M.S.
# Loop through all *df.csv files and submit a job for each
for i in *mtx; do
  echo "Submitting job for $i"
  qsub -v VAR="$i" format_mtx.sh  #this tells the computer to use the $i within the  submit_job.sh since I am not using it directly in shell
done

