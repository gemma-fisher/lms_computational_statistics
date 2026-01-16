# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics



# Exercise 2: 

# 1. Read expression data from EM-seq experiment. 

# First column represents the genome sequence coordinates, chr_start_end.

# Samples labelled '200uM' were grown in 200 micro-molar environment, the control condition.
# Samples labelled '3uM' were grown in 3 micro-molar environment, the deprived condition.
# There are two replicates per each group, labelled '_rep1' and '_rep2'.

# Each replicate has a column storing number of Cs (methylated prior to experiment, hence they remain as Cs through the EM-seq experiment).
# Each replicate has a column storing number of Ts (un-metylated, hence converted to Cs through the EM-seq experiment).

# 2. Compute methylation score s = nC / (nC + nT) per replicate individually, then average per replicate.

# 3. Implement manual computation of mean, median, variance and std.

# 4. Compare with numpy / scipy implementation.

# 5. Plot data as a box plot, violin and histogram, and plot summary statistics on top of the histogram.



# Import libraries ............................................................



# Load EM-seq .................................................................

# Read EM-seq data

# Compute methylation score

# Average scores for 3uM deprived

# Average scores for 200uM control



# Compute mean value ..........................................................

# Manual calculation

# Check implementation



# Compute variance ............................................................

# Manual calculation

# Check implementation



# Compute median ..............................................................

# Manual calculation

# Check implementation



# Compute std .................................................................

# Manual calculation

# Check implementation



# Plot data and summary statistics ............................................

# Prepare for plot

# Box plot

# Violin plot

# Prepare histogram

# Plot histogram
