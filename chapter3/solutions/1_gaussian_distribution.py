# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 3: Hypothesis testing (I)



# Exercise 1:

# 1. Simulate a Gaussian density with mean value mu=0 and standard deviation std=1 

# 2. Define a function that manually implements the Gaussian density

# 3. Check with Scipy implementation

# 4. Compute confidence intervals



# Import libraries ................................................................................

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import exp, factorial, sqrt, pi
from scipy import stats



# Gaussian distribution ...........................................................................
print("\nGaussian distribution")

# Gaussian probability density function
def gaussian_density(x, mu, sigma):
    """
    Gaussian probability density function
    with mean value mu and standard deviation sigma
    """
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-(x - mu)**2 / (2 * sigma**2))


# Create a even-spaced grid of x and compute Gaussian density
x = np.linspace(-5, 5, 1000)

# Prepare Gaussian for plot
mu, sigma = 0, 1
fx_manual = stats.norm.pdf(x, mu, sigma)
fx_stats = stats.norm.pdf(x, mu, sigma)

# Plot Gaussian distribution
plt.figure(figsize = (8, 5))
sns.lineplot(x = x, y = fx_manual, label = f"mu = {mu}, sigma = {sigma}")
plt.axvline(mu, linestyle = '--', label = 'mean')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-5, 5)
plt.grid(True, alpha = 0.3)
plt.title('Gaussian Distribution')
# plt.savefig("gaussian.png", dpi = 300, bbox_inches = "tight")
plt.show()

# Calculating probability
x1 = 1; x2 = 2; mu = 1; sigma = 2
# Calculating probability
x1 = 1; x2 = 2
x_interval = np.linspace(x1, x2, 1000)
y_interval = gaussian_density(x_interval, mu, sigma)
p_manual = np.trapz(y_interval, x_interval) # numpy 1.19 an earlier
# p_manual = np.trapezoid(y_interval, x_interval) # numpy 2.0 and after
p_scipy = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)
print(f"\nProbability of finding x between {x1} and {x2}: {p_manual}")
print(f"Probability of finding x between {x1} and {x2}: {p_scipy}")

# Calculating probability
x1 = -2; x2 = 2; mu = 1; sigma = 2
x_interval = np.linspace(x1, x2, 1000)
y_interval = gaussian_density(x_interval, mu, sigma)
p_manual = np.trapz(y_interval, x_interval) # numpy 1.19 an earlier
# p_manual = np.trapezoid(y_interval, x_interval) # numpy 2.0 and after
p_scipy = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)
print(f"\nProbability of finding x between {x1} and {x2}: {p_manual}")
print(f"Probability of finding x between {x1} and {x2}: {p_scipy}")

# Calculating probability
x1 = -5; x2 = 5; mu = 1; sigma = 2
x_interval = np.linspace(x1, x2, 1000)
y_interval = gaussian_density(x_interval, mu, sigma)
p_manual = np.trapz(y_interval, x_interval) # numpy 1.19 an earlier
# p_manual = np.trapezoid(y_interval, x_interval) # numpy 2.0 and after
p_scipy = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)
print(f"\nProbability of finding x between {x1} and {x2}: {p_manual}")
print(f"Probability of finding x between {x1} and {x2}: {p_scipy}")



# Confidence intervals ............................................................................
print("\nConfidence intervals")

# Calculating probability of (-1sigma, 1sigma) 68% CI
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability = stats.norm.cdf(mu + sigma, mu, sigma) - stats.norm.cdf(mu - sigma, mu, sigma)
print(f"\n68% CI: {probability}")

# Calculating probability of (-2sigma, 2sigma) 95% CI
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability = stats.norm.cdf(mu + 2 * sigma, mu, sigma) - stats.norm.cdf(mu - 2 * sigma, mu, sigma)
print(f"95% CI: {probability}")

# Calculating probability of (-3sigma, 3sigma) 99% CI
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability = stats.norm.cdf(mu + 3 * sigma, mu, sigma) - stats.norm.cdf(mu - 3 * sigma, mu, sigma)
print(f"99% CI: {probability}")
