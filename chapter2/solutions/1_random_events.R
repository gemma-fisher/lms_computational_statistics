# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics


# Exercise 1:

# 1. Simulate a fair coin toss, and compute probability of getting heads in both cases.
    # Hint: Use a Bernoulli distribution.
    # Define a function that computes a Bernoulli probability.
    # Compare with dbinom(size = 1).

# 2. Simulate a fair dice roll, and compute probability of getting a 3 in both cases.
    # Hint: Use a Uniform distribution.
    # Define a function that computes a Uniform probability.
    # Compare with dunif().

# 3. Compute the Binomial probability of:
    # i) Getting 5 heads in 10 flips of a coin.
    # ii) Getting 3 times a 6 in 10 rolls of dice.
    # iii) Passing an (A, B, C) exam answering randomly.
    # Define a function that computes a Binomial probability.
    # Compare with dbinom(size = n).

# 4. Compute the Poisson probability of:
    # i) Observing 3 cancer patients in a hospital over a week, with observed historical average 5.
    # ii) Observing 5 or less patients in the same hospital over same tame, with same average.
    # iii) Observing more than 5 patients in the same hospital over same tame, with same average.
    # Define a function that computes a Poisson probability.
    # Compare with dpois() and ppois().



# Import libraries ............................................................

library(stats)



# Bernoulli events ............................................................

cat("\nBernoulli events: Coin toss simulation\n")

# Compute Bernoulli probability
bernoulli_probability <- function(x, p) {

    # Calculate the Bernoulli probability of success (x=1) or failure (x=0)
    # with a probability of success p.

    if (x == 1) { # success
        return(p)
    } else if (x == 0) { # failure
        return(1 - p)
    } else {
        stop("x must be 0 (failure) or 1 (success)")
    }
}

# Probability of success (1) in a coin flip
p_success_manual <- bernoulli_probability(1, 1/2)
p_success_scipy <- dbinom(1, size = 1, prob = 1/2)
cat("\nProbability of heads (manual):", p_success_manual, "\n")
cat("Probability of heads (scipy):", p_success_scipy, "\n")

# Probability of failure (0) in a coin flip
p_failure_manual <- bernoulli_probability(1, 1/2)
p_failure_scipy <- dbinom(0, size = 1, prob = 1/2)
cat("\nProbability of tails (manual):", p_failure_manual, "\n")
cat("Probability of tails (scipy):", p_failure_scipy, "\n")



# Uniform events ..............................................................

cat("\nUniform events: Dice roll simulation\n")

# Compute Uniform probability
uniform_probability <- function(x, a, b) {
    
    # Calculate the probability of observing value x in a discrete
    # uniform distribution over [low, high].
    
    if (a <= x && x <= b) {
        return(1 / (b - a + 1)) # equal probability for all faces
    } else {
        return(0)
    }
}

# Probability of getting a 6 in a fair dice roll
p_6_manual <- uniform_probability(6, 1, 6)
p_6_scipy <- dunif(6, min = 1 - 0.5, max = 6 + 0.5)
cat("\nProbability of rolling a 6 (manual):", p_6_manual, "\n")
cat("Probability of rolling a 6 (scipy):", p_6_scipy, "\n")

# Probability of getting a 3 in a fair dice roll
p_3_manual <- uniform_probability(3, 1, 6)
p_3_scipy <- dunif(3, min = 1 - 0.5, max = 6 + 0.5)
cat("\nProbability of rolling a 3 (manual):", p_3_manual, "\n")
cat("Probability of rolling a 3 (scipy):", p_3_scipy, "\n")



# Binomial events .............................................................

cat("\nBinomial events\n")

# Compute Binomial probability
binomial_probability <- function(x, n, p) {
    
    # Calculate the binomial probability of getting k successes in n trials
    # with a probability of success p.
    
    return(choose(n, x) * (p ^ x) * ((1 - p) ^ (n - x)))
}

# Probability of 5 heads in 10 flips of a coin
x <- 5; n <- 10; p <- 1/2
p_manual <- binomial_probability(x, n, p)
p_scipy <- dbinom(x, n, p)
cat("\nProbability of", x, "heads in", n, "coin tosses:", p_manual, "\n")
cat("Probability of", x, "heads in", n, "coin tosses:", p_scipy, "\n")

# Probability of 3 times a 6 in 10 rolls of dice
x <- 3; n <- 10; p <- 1/6
p_manual <- binomial_probability(x, n, p)
p_scipy <- dbinom(x, n, p)
cat("\nProbability of", x, "6s in", n, "dice rolls:", p_manual, "\n")
cat("Probability of", x, "6s in", n, "dice rolls:", p_scipy, "\n")

# Probability of passing an (A, B, C) exam answering randomly
x <- 5; n <- 10; p <- 1/3
p_manual <- binomial_probability(x, n, p)
p_scipy <- dbinom(x, n, p)
cat("\nProbability of", x, "5 questions out of", n, ":", p_manual, "\n")
cat("Probability of", x, "5 questions out of", n, ":", p_scipy, "\n")



# Poisson events ..............................................................

cat("\nPoisson events\n")

# Compute Poisson probability
poisson_probability <- function(x, lambda) {
    
    # Calculate the probability of observing k events in a Poisson distribution
    # with rate parameter lambda.
    
    return((lambda ^ x) * exp(-lambda) / factorial(x))
}

# Probability of 3 cancer patients with average 5
x <- 3; lambda <- 5
p_manual <- poisson_probability(x, lambda)
p_scipy <- dpois(x, lambda)
cat("\nProbability of", x, "cancer patients with average", lambda, ":", p_manual, "\n")
cat("Probability of", x, "cancer patients with average", lambda, ":", p_scipy, "\n")

# Probability of 5 or less patients, with same average
x <- 5; lambda <- 5
p_manual <- dpois(0, lambda) + dpois(1, lambda) + dpois(2, lambda) +
            dpois(3, lambda) + dpois(4, lambda) + dpois(5, lambda)
p_scipy <- ppois(x, lambda)
cat("\nProbability of", x, "or less cancer patients with average", lambda, ":", p_manual, "\n")
cat("Probability of", x, "or less cancer patients with average", lambda, ":", p_scipy, "\n")

# Probability of more than 5 patients, with same average
x <- 5; lambda <- 5
p_manual <- 1 - p_manual
p_scipy <- 1 - p_scipy
cat("\nProbability of more than", x, "cancer patients with average", lambda, ":", p_manual, "\n")
cat("Probability of more than", x, "cancer patients with average", lambda, ":", p_scipy, "\n")
