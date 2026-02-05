# Import libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import t, ttest_1samp

print("All libraries successfully imported")

# Read control and mutant data

print("\nReading data:")

# Read csv data with pandas library
df_control = pd.read_csv("exercises/data/exp_control.csv")
df_mutant = pd.read_csv("exercises/data/exp_mutant1.csv")
print("\nControl expression:\n", df_control.head())
print("Control format: ", type(df_control))
print("Mutant expression:\n", df_mutant.head())
print("Mutant format: ", type(df_mutant))

# Extract data as numpy dnarray
control_expr = df_control["avg_expression"].values
mutant_expr = df_mutant["avg_expression"].values
print("\nControl expression:\n", control_expr[:5])
print("Control format: ", type(control_expr))
print("Mutant expression:\n", mutant_expr[:5])
print("Mutant format: ", type(mutant_expr))

# Visualise data 

# Plot as histogram 
plt.figure(figsize = (8, 5))
plt.hist(control_expr, bins = 30, label = "Control", alpha = 0.5, edgecolor = "black", linewidth = 0.8)
plt.hist(mutant_expr, bins = 30, label = "Mutant", alpha = 0.5, edgecolor = "black", linewidth = 0.8)
plt.axvline(np.mean(control_expr), linestyle = "--", linewidth = 2, label = "Control mean")
plt.axvline(np.mean(mutant_expr), linestyle = "--", linewidth = 2, label = "Mutant mean")
plt.xlabel("Average expression")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, alpha = 0.3)
plt.savefig("Control_vs_mutant_histogram.png")

# Compute sample mean and variance of our sample 
# H0: mean(control) = mean(mutant)
# H1: mean(control) > mean(mutant)

# Prepare for computing t-statistic
mu = np.mean(control_expr)

# Sample mean and std from our mutant
xbar = np.mean(mutant_expr)
n = len(control_expr)
s = np.std(mutant_expr, ddof = 1)
se = s / np.sqrt(n)
print("\nExpected value (mu control): ", mu)
print ("Sample mean (xbar mutant): ", xbar)
print ("standard error: ", se)

# One sample t-test (manually)
# t_obs = (mu - xbar) / se
# p_value = t.cdf(tobs)

# One sample t-test (spicy)
# t_obs
# p_value
ttest_1samp(mu, xbar)