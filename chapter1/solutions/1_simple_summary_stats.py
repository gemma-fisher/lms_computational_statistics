# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics



# Exercise 1:

# 1. Simulate 10 observations from a gaussian distribution.

# 2. Implement a manual computation of mean, median, variance and std.

# 3. Check calculation with numpy / scipy implementation.

# 4. Repeat with simulated data following an exponential and a uniform distribution.



# Import libraries ............................................................

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# Simulate data ...............................................................

# Random seed
np.random.seed(123)

# Simulate data
data = np.random.normal(loc = 5, scale = 2, size = 1000)
# data = np.random.uniform(low = 0, high = 10, size = 1000)
# data = np.random.exponential(scale = 2, size = 1000)
print(f"\nRandom data:\n{data}")
print(f"Data format: {type(data)}")
print(f"Data shape: {data.shape}")

# Plot histogram
plt.figure(figsize = (8, 5))
plt.hist(data, bins = 30, alpha = 0.5, edgecolor = "black", linewidth = 0.8)
plt.title("Histogram of simulated data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, alpha = 0.3)
# plt.savefig("data_histogram.png", dpi = 300, bbox_inches = "tight")
# plt.show()

# Plot data as box plot
plt.figure(figsize = (8, 5))
sns.boxplot(data)
plt.title("Box plot of simulated data")
plt.ylabel("Value")
plt.grid(True, alpha = 0.3)
# plt.savefig("data_box.png", dpi = 300, bbox_inches = "tight")
# plt.show()

# Plot data as violin plot
plt.figure(figsize = (8, 5))
sns.violinplot(data)
plt.title("Violin plot of simulated data")
plt.ylabel("Value")
plt.grid(True, alpha = 0.3)
# plt.savefig("data_violin.png", dpi = 300, bbox_inches = "tight")
# plt.show()



# Compute mean value ..........................................................

# Manual calculation
def compute_mean(data):
    
    return sum(data) / len(data)

# Check implementation
mean_manual = compute_mean(data)
mean_np = np.mean(data)
print("\nMean (manual):", mean_manual)
print("Mean (numpy):", mean_np)



# Compute variance ............................................................

# Manual calculation
def compute_var(data):

    mean_val = compute_mean(data)
    squared_diffs = [(x - mean_val) ** 2 for x in data]

    return sum(squared_diffs) / len(data) # population variance
    # return sum(squared_diffs) / (len(data) - 1)  # sample variance

# Check implementation
var_manual = compute_var(data)
var_np = np.var(data, ddof = 0) # population variance
# var_np = np.var(data, ddof = 1) # sample variance
print("\nVariance (manual):", var_manual)
print("Variance (numpy):", var_np)



# Compute median ..............................................................

# Manual calculation
def compute_median(data):

    # Sort data and find middle point
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2 # integer division, divide and round
    
    # Check if even / odd data
    if n % 2 == 0:
        return (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        return sorted_data[middle]

# Check implementation
median_manual = compute_median(data)
median_np = np.median(data)
print("\nMedian (manual):", median_manual)
print("Median (numpy):", median_np)



# Compute std .................................................................

# Manual calculation
def compute_std(data):

    var = compute_var(data)
    return var ** 0.5

# Check implementation
std_manual = compute_std(data)
std_np = np.std(data, ddof = 0)
print("\nStandard deviation (manual):", std_manual)
print("Standard deviation (numpy):", std_np)
