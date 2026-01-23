# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics



# Exercise 1:

# 1. Simulate a fair coin toss, then a biased one (P(H) = 0.7), and compute probability of getting heads in both cases.
# Hint: Use a Bernoulli distribution

# 2. Simulate a fair dice roll, then a biased one (P(H) = 0.6), and compute probability of getting a 6 in both cases.
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

n_sim = 100



# Bernoulli events ............................................................

print("\nBernoulli events: Coin toss simulation")

def bernoulli_probability(x, p):
    """
    Calculate the Bernoulli probability of success (x=1) or failure (x=0)
    with a probability of success p.
    """
    if x == 1:  # success
        return p
    elif x == 0:  # failure
        return 1 - p
    else:
        raise ValueError("x must be 0 (failure) or 1 (success)")

# Probability of success (1) in a coin flip
x = 1; p = 1/2
prob_success = bernoulli_probability(x, p)
prob_success_scipy = stats.bernoulli.pmf(x, p)
print(f"\nProbability of heads (success) (manual): {prob_success}")
print(f"Probability of heads (success) (scipy): {prob_success_scipy}")

# Probability of failure (0) in a coin flip
x = 0; p = 1/2
prob_failure = bernoulli_probability(x, p)
prob_failure_scipy = stats.bernoulli.pmf(x, p)
print(f"\nProbability of tails (failure) (manual): {prob_failure}")
print(f"Probability of tails (failure) (scipy): {prob_failure_scipy}")

# Simulation: fair vs biased coin
fair_coin = np.random.binomial(1, 0.5, n_sim)
biased_coin = np.random.binomial(1, 0.7, n_sim)
print(f"\nSimulated P(Heads), fair coin: {fair_coin.mean()}")
print(f"Simulated P(Heads), biased coin (p=0.7): {biased_coin.mean()}")



# Uniform events ..............................................................

print("\nUniform events: Dice roll simulation")

def uniform_probability(x, low, high):
    """
    Calculate the probability of observing value x in a discrete
    uniform distribution over [low, high].
    """
    if low <= x <= high:
        return 1 / (high - low + 1)
    else:
        return 0

# Fair dice (uniform)
fair_dice = np.random.randint(1, 7, n_sim)
simulated_prob_fair = (fair_dice == 6).mean()
theoretical_prob_fair = uniform_probability(6, 1, 6)
print(f"Simulated P(6), fair dice (randint): {simulated_prob_fair}")
print(f"Theoretical P(6), fair dice (uniform): {theoretical_prob_fair}")

# Biased dice: P(6) = 0.6, rest equally distributed
probs = [0.08, 0.08, 0.08, 0.08, 0.08, 0.6]
biased_dice = np.random.choice([1, 2, 3, 4, 5, 6], size=n_sim, p=probs)
simulated_prob_biased = (biased_dice == 6).mean()
print(f"Simulated P(6), biased dice (choice): {simulated_prob_biased}")
print(f"Theoretical P(6), biased dice: 0.6")



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
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability {x} heads in {n} coin tosses: {probability1}")
print(f"Probability {x} heads in {n} coin tosses: {probability2}")

# Probability of 3 times a 6 in 10 rolls of dice
x = 3; n = 10; p = 1/6
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability {x} 6s in {n} dice rolls: {probability1}")
print(f"Probability {x} 6s in {n} dice rolls: {probability2}")

# Probability of passing an (A, B, C) exam answering randomly
x = 5; n = 10; p = 1/3
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability {x} 5 questions out of {n}: {probability1}")
print(f"Probability {x} 5 questions out of {n}: {probability2}")



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
probability1 = poisson_probability(x, lmbda)
probability2 = stats.poisson.pmf(x, lmbda)
print(f"\nProbability {x} cancer patients with average {lmbda}: {probability1}")
print(f"Probability {x} cancer patients with average {lmbda}: {probability2}")

# Probability of 5 or less patients, with same average
x = 5; lmbda = 5
probability1 = stats.poisson.pmf(0, lmbda) + stats.poisson.pmf(1, lmbda) + stats.poisson.pmf(2, lmbda) + stats.poisson.pmf(3, lmbda) + stats.poisson.pmf(4, lmbda) + stats.poisson.pmf(5, lmbda)
probability2 = stats.poisson.cdf(x, lmbda)
print(f"\nProbability of observing {x} or less cancer patients with average {lmbda}: {probability1}")
print(f"Probability of observing {x} or less cancer patients with average {lmbda}: {probability2}")

# Probability of more than 5 patients, with same average
x = 5; lmbda = 5
probability1 = 1 - probability1
probability2 = 1 - probability2
print(f"\nProbability of observing more than {x} cancer patients with average {lmbda}: {probability1}")
print(f"Probability of observing more than {x} cancer patients with average {lmbda}: {probability2}")
