# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics



# Exercise 3: 

# 1. Read expression data from RNA-seq experiment.

# First column represents the gene Ensembl ID.

# Samples labelled '200uM' were grown in 200 micro-molar environment, the control condition.
# Samples labelled '3uM' were grown in 3 micro-molar environment, the deprived condition.
# All samples are labelled 'SL_', indicating they were grown in serum. There are three replicates per each group, labelled '_rep1', '_rep2', '_rep3'.

# Each replicate has one column only, storing raw counts. Counts represent the number reads, i.e. the number of times a transcription of that gene was detected.
# Do not average per replicates, just concatenate / "pool" them with the '.flatten()' function.

# 2. Implement manual computation of mean, median, variance and std.

# 3. Compare with numpy / scipy implementation.

# 4. Compute log transformed counts log(counts + 1) for clear visualization.

# 5. Plot data as a box plot, violin and histogram, and plot summary statistics on top of the histogram.



# Import libraries ............................................................



# Load RNA-seq ................................................................



# Compute mean value ..........................................................



# Compute variance ............................................................



# Compute median ..............................................................



# Compute std .................................................................



# Plot RNA-seq data ...........................................................
