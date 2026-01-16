# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 1: Descriptive statistics



# Exercise 1:

# 1. Simulate 10 observations from a gaussian distribution.

# 2. Implement a manual computation of mean, median, variance and std.

# 3. Check calculation with numpy / scipy implementation.

# 4. Repeat with simulated data following an exponential and a uniform distribution.



# Import libraries ............................................................

library(ggplot2)
setwd("/Users/jurtasun/Desktop/courses/LMS/2026/lms_computational_statistics/chapter1/exercises")



# Simulate data ...............................................................

# Random seed
set.seed(123)

# Simulate data
data <- rnorm(n = 1000, mean = 5, sd = 2)
# data <- runif(n = 1000, min = 0, max = 10)
# data <- rexp(n = 1000, rate = 1/2)
cat("\nRandom data:\n"); print(data)
cat("Data format:", class(data), "\n")
cat("Data shape:", length(data), "\n")

df <- data.frame(value = data)

# Plot histogram
ggplot(df, aes(x = value)) + geom_histogram(bins = 30, fill = "steelblue", color = "black", alpha = 0.6) +
  labs(title = "Histogram of simulated data", x = "Value", y = "Frequency") + theme_bw()

# Plot data as box plot
ggplot(df, aes(x = "", y = value)) + geom_boxplot(fill = "steelblue") +
  labs(title = "Box plot of simulated data", y = "Value") + theme_bw()

# Plot data as violin plot
ggplot(df, aes(x = "", y = value)) + geom_violin(fill = "steelblue") +
  labs(title = "Violin plot of simulated data", y = "Value") + theme_bw()



# Compute mean value ..........................................................

compute_mean <- function(data) {
    
    sum(data) / length(data)
  
}

mean_manual <- compute_mean(data)
mean_r <- mean(data)
cat("\nMean (manual):", mean_manual, "\n")
cat("Mean (R):", mean_r, "\n")



# Compute variance ............................................................

compute_var <- function(data) {

    mean_val <- compute_mean(data)
    squared_diffs <- (data - mean_val)^2

    sum(squared_diffs) / length(data)
    
}

var_manual <- compute_var(data)
var_r <- var(data) * (length(data) - 1) / length(data)
cat("\nVariance (manual):", var_manual, "\n")
cat("Variance (R):", var_r, "\n")



# Compute median ..............................................................

compute_median <- function(data) {

    sorted_data <- sort(data)
    n <- length(sorted_data)
    middle <- n %/% 2
    
    if (n %% 2 == 0) {
        (sorted_data[middle] + sorted_data[middle + 1]) / 2
    } else {
        sorted_data[middle + 1]
    }
    
}

median_manual <- compute_median(data)
median_r <- median(data)
cat("\nMedian (manual):", median_manual, "\n")
cat("Median (R):", median_r, "\n")



# Compute std .................................................................

compute_std <- function(data) {

    compute_var(data) ^ 0.5
  
}

std_manual <- compute_std(data)
std_r <- sd(data) * sqrt((length(data) - 1) / length(data))
cat("\nStandard deviation (manual):", std_manual, "\n")
cat("Standard deviation (R):", std_r, "\n")
