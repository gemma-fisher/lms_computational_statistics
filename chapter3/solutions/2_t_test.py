# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 3: Hypothesis testing (I)



# Exercise 2:

# 1. Read control and mutant expression data from the data/ directory

# 2. Plot both distributions as a histogram

# 3. Compute manually a one-sample t-statistic, and a P-value by computing the cumulative probabiltiy of the t distribution

# 4. Compare with scipy implementation: Use the stats.ttest_1samp library



# Import libraries ................................................................................

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import t, ttest_1samp



# Load data .......................................................................................
print("\nLoading data")

# Read csv data
df_control = pd.read_csv("data/exp_control.csv")
df_mutant1 = pd.read_csv("data/exp_mutant1.csv")

# Extract values as numpy ndarray
control_expr = df_control["avg_expression"].values
mutant1_expr = df_mutant1["avg_expression"].values



# Visual inspection: histogram ....................................................................

# Plot histogram
plt.figure(figsize = (8, 5))
plt.hist(control_expr, bins = 30, alpha = 0.5, label = "Control", edgecolor = "black", linewidth = 0.8)
plt.hist(mutant1_expr, bins = 30, alpha = 0.5, label = "Mutant", edgecolor = "black", linewidth = 0.8)
plt.axvline(np.mean(control_expr), linestyle = "--", linewidth = 2, label = "Control mean")
plt.axvline(np.mean(mutant1_expr), linestyle = "--", linewidth = 2, label = "Mutant mean")
plt.xlabel("Average expression")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, alpha = 0.3)
# plt.savefig("control_vs_mutant1_hist.png", dpi=300, bbox_inches="tight")
plt.show()



# Hypothesis testing (manual implementation) .................................................

# H0: mean(control) = mean(mutant)
# H1: mean(control) > mean(mutant)
mu = np.mean(control_expr)
xbar = np.mean(mutant1_expr)
s = np.std(mutant1_expr, ddof = 1)
n = len(mutant1_expr)
se = s / np.sqrt(n)
print(f"\nExpected value (mu control) = {mu:.3f}")
print(f"Sample mean (xbar mutant) = {xbar:.3f}")
print(f"Standard error = {se:.3f}")

# Manual t-statistic
t_stat = (xbar - mu) / (s / np.sqrt(n))
df = n - 1

# One-sided p-value using t distribution
p_value_manual = 1 - t.cdf(t_stat, df)
print("\nOne-sample t-test: compare sample mean to expected value (manual)")
print(f"t statistic = {t_stat:.3f}")
print(f"p-value = {p_value_manual:.4e}")



# Hypothesis testing (Scipy implementation) .................................................

t_stat_scipy, p_value_two_sided = ttest_1samp(mutant1_expr, popmean = mu)

# Convert to one-sided p-value
p_value_one_sided = p_value_two_sided / 2 if t_stat_scipy > 0 else 1
print("\nOne-sample t-test: compare sample mean to expected value (Scipy)")
print(f"t statistic = {t_stat_scipy:.3f}")
print(f"p-value = {p_value_one_sided:.4e}")



# Interpret result (significance level 0.05) ......................................................
alpha = 0.05
if p_value_manual < alpha:
    print("\np-value < significance threshold: Reject H0:\nExpression in mutant significantly different from expression in control.")
else:
    print("\np-value > significance threshold: Accept H0:\nNo evidence of expression in mutant significantly different than in control.")
