# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 3: Hypothesis testing (I)



# Exercise 1:

# 1. Simulate a Gaussian density with mean value mu=0 and standard deviation std=1 

# 2. Define a function that manually implements the Gaussian density

# 3. Check with Scipy implementation

# 4. Compute confidence intervals



# Import libraries ................................................................................

library(ggplot2)
library(pracma)

# To install practical mathematical tools library `pracma` in the terminal
# install.packages("pracma")



# Gaussian distribution ...........................................................................
cat("\nGaussian distribution\n")

# Gaussian probability density function
gaussian_density <- function(x, mu, sigma) {
    #
    # Gaussian probability density function
    # with mean value mu and standard deviation sigma
    #
    (1 / (sqrt(2 * pi) * sigma)) * exp(-(x - mu)^2 / (2 * sigma^2))
}


# Create a even-spaced grid of x and compute Gaussian density
x <- seq(-5, 5, length.out = 1000)

# Prepare Gaussian for plot
mu <- 0; sigma <- 1
fx_manual <- dnorm(x, mu, sigma)
fx_stats  <- dnorm(x, mu, sigma)

# Plot Gaussian distribution
df_plot <- data.frame(x = x, fx = fx_manual)

ggplot(df_plot, aes(x = x, y = fx)) +
    geom_line() +
    geom_vline(xintercept = mu, linetype = "dashed") +
    labs(x = "x", y = "f(x)", title = "Gaussian Distribution") +
    xlim(-5, 5) +
    theme_bw()



# Calculating probability
x1 <- 1; x2 <- 2; mu <- 1; sigma <- 2
# Calculating probability
x1 <- 1; x2 <- 2
x_interval <- seq(x1, x2, length.out = 1000)
y_interval <- gaussian_density(x_interval, mu, sigma)
p_manual <- trapz(x_interval, y_interval)
p_scipy  <- pnorm(x2, mu, sigma) - pnorm(x1, mu, sigma)
cat(sprintf("\nProbability of finding x between %d and %d: %f\n", x1, x2, p_manual))
cat(sprintf("Probability of finding x between %d and %d: %f\n", x1, x2, p_scipy))


# Calculating probability
x1 <- -2; x2 <- 2; mu <- 1; sigma <- 2
x_interval <- seq(x1, x2, length.out = 1000)
y_interval <- gaussian_density(x_interval, mu, sigma)
p_manual <- trapz::trapz(x_interval, y_interval)
p_scipy  <- pnorm(x2, mu, sigma) - pnorm(x1, mu, sigma)
cat(sprintf("\nProbability of finding x between %d and %d: %f\n", x1, x2, p_manual))
cat(sprintf("Probability of finding x between %d and %d: %f\n", x1, x2, p_scipy))


# Calculating probability
x1 <- -5; x2 <- 5; mu <- 1; sigma <- 2
x_interval <- seq(x1, x2, length.out = 1000)
y_interval <- gaussian_density(x_interval, mu, sigma)
p_manual <- trapz(x_interval, y_interval)
p_scipy  <- pnorm(x2, mu, sigma) - pnorm(x1, mu, sigma)
cat(sprintf("\nProbability of finding x between %d and %d: %f\n", x1, x2, p_manual))
cat(sprintf("Probability of finding x between %d and %d: %f\n", x1, x2, p_scipy))



# Confidence intervals ............................................................................
cat("\nConfidence intervals\n")

# Calculating probability of (-1sigma, 1sigma) 68% CI
mu <- 1; sigma <- 2
probability <- pnorm(mu + sigma, mu, sigma) - pnorm(mu - sigma, mu, sigma)
cat(sprintf("\n68%% CI: %f\n", probability))

# Calculating probability of (-2sigma, 2sigma) 95% CI
probability <- pnorm(mu + 2 * sigma, mu, sigma) - pnorm(mu - 2 * sigma, mu, sigma)
cat(sprintf("95%% CI: %f\n", probability))

# Calculating probability of (-3sigma, 3sigma) 99% CI
probability <- pnorm(mu + 3 * sigma, mu, sigma) - pnorm(mu - 3 * sigma, mu, sigma)
cat(sprintf("99%% CI: %f\n", probability))
