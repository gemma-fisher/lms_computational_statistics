# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics


# Exercise 1:

# 1. Simulate a fair coin toss, and compute probability of getting heads in both cases.
# Hint: Use a Bernoulli distribution

# 2. Simulate a fair dice roll, and compute probability of getting a 3 in both cases.
# Hint: Use a Uniform distribution

# 3. Compute the Binomial probability of:
    # i) Getting 5 heads in 10 flips of a coin.
    # ii) Getting 3 times a 6 in 10 rolls of dice.
    # iii) Passing an (A, B, C) exam answering randomly.

# 4. Compute the Poisson probability of:
    # i) Observing 3 cancer patients in a hospital over a week, with observed historical average 5.
    # ii) Observing 5 or less patients in the same hospital over same tame, with same average.
    # iii) Observing more than 5 patients in the same hospital over same tame, with same average.



# Import libraries ............................................................

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from math import comb, exp, factorial, sqrt
from scipy import stats



# Bernoulli events ............................................................

print("\nBernoulli events: Coin toss simulation")

def bernoulli_probability(x, p):
    """
    Calculate the Bernoulli probability of success (x=1) or failure (x=0)
    with a probability of success p.
    """
    if x == 1: # success
        return p
    elif x == 0: # failure
        return 1 - p
    else:
        raise ValueError("x must be 0 (failure) or 1 (success)")

# Probability of success (1) in a coin flip
x = 1; p = 1/2
p_success_manual = bernoulli_probability(x, p)
p_success_scipy = stats.bernoulli.pmf(x, p)
print(f"\nProbability of heads (success) (manual): {p_success_manual}")
print(f"Probability of heads (success) (scipy): {p_success_scipy}")

# Probability of failure (0) in a coin flip
x = 0; p = 1/2
p_failure_manual = bernoulli_probability(x, p)
p_failure_scipy = stats.bernoulli.pmf(x, p)
print(f"\nProbability of tails (failure) (manual): {p_failure_manual}")
print(f"Probability of tails (failure) (scipy): {p_failure_scipy}")



# Uniform events ..............................................................

print("\nUniform events: Dice roll simulation")

def uniform_probability(x, a, b):
    """
    Calculate the probability of observing value x in a discrete
    uniform distribution over [low, high].
    """
    if a <= x <= b:
        return 1 / (b - a + 1) # equal probability for all faces
    else:
        return 0

# Probability of getting a 6 in a fair dice roll
x = 6; a = 1; b = 6
p_6_manual = uniform_probability(x, a, b)
p_6_scipy = stats.randint.pmf(x, a, b + 1)
print(f"\nProbability of rolling a 6 (manual): {p_6_manual}")
print(f"Probability of rolling a 6 (scipy): {p_6_scipy}")

# Probability of getting a 3 in a fair dice roll
x = 3; a = 1; b = 6
p_3_manual = uniform_probability(x, a, b)
p_3_scipy = stats.randint.pmf(x, a, b + 1)
print(f"\nProbability of rolling a 3 (manual): {p_3_manual}")
print(f"Probability of rolling a 3 (scipy): {p_3_scipy}")



# Binomial events .............................................................

print("\nBinomial events")

def binomial_probability(x, n, p):
    """
    Calculate the binomial probability of getting k successes in n trials
    with a probability of success p.
    """
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

# Probability of 5 heads in 10 flips of a coin
x = 5; n = 10; p = 1/2
p_manual = binomial_probability(x, n, p)
p_scipy = stats.binom.pmf(x, n, p)
print(f"\nProbability of {x} heads in {n} coin tosses: {p_manual}")
print(f"Probability of {x} heads in {n} coin tosses: {p_scipy}")

# Probability of 3 times a 6 in 10 rolls of dice
x = 3; n = 10; p = 1/6
p_manual = binomial_probability(x, n, p)
p_scipy = stats.binom.pmf(x, n, p)
print(f"\nProbability of {x} 6s in {n} dice rolls: {p_manual}")
print(f"Probability of {x} 6s in {n} dice rolls: {p_scipy}")

# Probability of passing an (A, B, C) exam answering randomly
x = 5; n = 10; p = 1/3
p_manual = binomial_probability(x, n, p)
p_scipy = stats.binom.pmf(x, n, p)
print(f"\nProbability of {x} 5 questions out of {n}: {p_manual}")
print(f"Probability of {x} 5 questions out of {n}: {p_scipy}")



# Poisson events ..............................................................

print("\nPoisson events")

def poisson_probability(x, lmbda):
    """
    Calculate the probability of observing k events in a Poisson distribution
    with rate parameter lmbda.
    """
    return (lmbda ** x) * exp(-lmbda) / factorial(x)

# Probability of 3 cancer patients with average 5
x = 3; lmbda = 5
p_manual = poisson_probability(x, lmbda)
p_scipy = stats.poisson.pmf(x, lmbda)
print(f"\nProbability of {x} cancer patients with average {lmbda}: {p_manual}")
print(f"Probability of {x} cancer patients with average {lmbda}: {p_scipy}")

# Probability of 5 or less patients, with same average
x = 5; lmbda = 5
p_manual = stats.poisson.pmf(0, lmbda) + stats.poisson.pmf(1, lmbda) + stats.poisson.pmf(2, lmbda) + stats.poisson.pmf(3, lmbda) + stats.poisson.pmf(4, lmbda) + stats.poisson.pmf(5, lmbda)
p_scipy = stats.poisson.cdf(x, lmbda)
print(f"\nProbability of observing {x} or less cancer patients with average {lmbda}: {p_manual}")
print(f"Probability of observing {x} or less cancer patients with average {lmbda}: {p_scipy}")

# Probability of more than 5 patients, with same average
x = 5; lmbda = 5
p_manual = 1 - p_manual
p_scipy = 1 - p_scipy
print(f"\nProbability of observing more than {x} cancer patients with average {lmbda}: {p_manual}")
print(f"Probability of observing more than {x} cancer patients with average {lmbda}: {p_scipy}")
