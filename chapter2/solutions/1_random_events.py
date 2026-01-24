# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics


# Exercise 1:

# 1. Simulate a fair coin toss, and compute probability of getting heads in both cases.
    # Hint: Use a Bernoulli distribution.
    # Define a function that computes a Bernoulli probability.
    # Compare with stats.bernoulli.pmf().

# 2. Simulate a fair dice roll, and compute probability of getting a 3 in both cases.
    # Hint: Use a Uniform distribution.
    # Define a function that computes a Uniform probability.
    # Compare with stats.randint.pmf().

# 3. Compute the Binomial probability of:
    # i) Getting 5 heads in 10 flips of a coin.
    # ii) Getting 3 times a 6 in 10 rolls of dice.
    # iii) Passing an (A, B, C) exam answering randomly.
    # Define a function that computes a Binomial probability.
    # Compare with stats.binom.pmf().

# 4. Compute the Poisson probability of:
    # i) Observing 3 cancer patients in a hospital over a week, with observed historical average 5.
    # ii) Observing 5 or less patients in the same hospital over same tame, with same average.
    # iii) Observing more than 5 patients in the same hospital over same tame, with same average.
    # Define a function that computes a Poisson probability.
    # Compare with stats.poisson.cdf() and stats.poisson.cdf().



# Import libraries ............................................................

import numpy as np
from math import comb, exp, factorial
from scipy import stats



# Bernoulli events ............................................................

print("\nBernoulli events: Coin toss simulation")

# Compute Bernoulli probability
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
p_success_manual = bernoulli_probability(1, 1/2)
p_success_scipy = stats.bernoulli.pmf(1, 1/2)
print(f"\nProbability of heads (manual): {p_success_manual}")
print(f"Probability of heads (scipy): {p_success_scipy}")

# Probability of failure (0) in a coin flip
p_failure_manual = bernoulli_probability(0, 1/2)
p_failure_scipy = stats.bernoulli.pmf(0, 1/2)
print(f"\nProbability of tails (manual): {p_failure_manual}")
print(f"Probability of tails (scipy): {p_failure_scipy}")



# Uniform events ..............................................................

print("\nUniform events: Dice roll simulation")

# Compute Uniform probability
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
p_6_manual = uniform_probability(6, 1, 6)
p_6_scipy = stats.randint.pmf(6, 1, 7)
print(f"\nProbability of rolling a 6 (manual): {p_6_manual}")
print(f"Probability of rolling a 6 (scipy): {p_6_scipy}")

# Probability of getting a 3 in a fair dice roll
p_3_manual = uniform_probability(3, 1, 6)
p_3_scipy = stats.randint.pmf(3, 1, 7)
print(f"\nProbability of rolling a 3 (manual): {p_3_manual}")
print(f"Probability of rolling a 3 (scipy): {p_3_scipy}")



# Binomial events .............................................................

print("\nBinomial events")

# Compute Binomial probability
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

# Compute Poisson probability
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
print(f"\nProbability of {x} or less cancer patients with average {lmbda}: {p_manual}")
print(f"Probability of {x} or less cancer patients with average {lmbda}: {p_scipy}")

# Probability of more than 5 patients, with same average
x = 5; lmbda = 5
p_manual = 1 - p_manual
p_scipy = 1 - p_scipy
print(f"\nProbability of more than {x} cancer patients with average {lmbda}: {p_manual}")
print(f"Probability of more than {x} cancer patients with average {lmbda}: {p_scipy}")
