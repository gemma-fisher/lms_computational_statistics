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



# Bernoulli events ............................................................

print("\nBernoulli events: Coin toss simulation")

# Compute Bernoulli probability

# Probability of success (1) in a coin flip

# Probability of failure (0) in a coin flip



# Uniform events ..............................................................

print("\nUniform events: Dice roll simulation")

# Compute Uniform probability

# Probability of getting a 6 in a fair dice roll

# Probability of getting a 3 in a fair dice roll



# Binomial events .............................................................

print("\nBinomial events")

# Compute Binomial probability

# Probability of 5 heads in 10 flips of a coin

# Probability of 3 times a 6 in 10 rolls of dice

# Probability of passing an (A, B, C) exam answering randomly



# Poisson events ..............................................................

print("\nPoisson events")

# Compute Poisson probability

# Probability of 3 cancer patients with average 5

# Probability of 5 or less patients, with same average

# Probability of more than 5 patients, with same average
