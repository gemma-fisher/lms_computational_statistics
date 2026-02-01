# Introduction to Computational Statistics
# Jesús Urtasun Elizari: MRC LMS 2026
# Chapter 3: Hypothesis testing (I)



# Exercise 2:

# 1. Read control and mutant expression data from the data/ directory

# 2. Plot both distributions as a histogram

# 3. Compute manually a one-sample t-statistic, and a P-value by computing the cumulative probabiltiy of the t distribution

# 4. Compare with scipy implementation: Use the stats.ttest_1samp library



# Import libraries ................................................................................

library(ggplot2)



# Load data .......................................................................................
cat("\nLoading data\n")

# Read csv data
df_control <- read.csv("data/exp_control.csv")
df_mutant1 <- read.csv("data/exp_mutant1.csv")

# Extract values as numeric vector
control_expr <- df_control$avg_expression
mutant1_expr <- df_mutant1$avg_expression



# Visual inspection: histogram ....................................................................

df_plot <- data.frame(
    value = c(control_expr, mutant1_expr),
    group = rep(c("Control", "Mutant"), c(length(control_expr), length(mutant1_expr)))
)

ggplot(df_plot, aes(x = value, fill = group)) +
    geom_histogram(position = "identity", bins = 30, alpha = 0.5, color = "black") +
    geom_vline(xintercept = mean(control_expr), linetype = "dashed", size = 1) +
    geom_vline(xintercept = mean(mutant1_expr), linetype = "dashed", size = 1) +
    labs(x = "Average expression", y = "Frequency") +
    theme_bw()



# Hypothesis testing (manual implementation) .................................................

# H0: mean(control) = mean(mutant)
# H1: mean(control) > mean(mutant)
mu <- mean(control_expr)
xbar <- mean(mutant1_expr)
s <- sd(mutant1_expr)
n <- length(mutant1_expr)
se <- s / sqrt(n)
cat(sprintf("\nExpected value (mu control) = %.3f\n", mu))
cat(sprintf("Sample mean (xbar mutant) = %.3f\n", xbar))
cat(sprintf("Standard error = %.3f\n", se))

# Manual t-statistic
t_stat <- (xbar - mu) / (s / sqrt(n))
df <- n - 1

# One-sided p-value using t distribution
p_value_manual <- 1 - pt(t_stat, df)
cat("\nOne-sample t-test: compare sample mean to expected value (manual)\n")
cat(sprintf("t statistic = %.3f\n", t_stat))
cat(sprintf("p-value = %.4e\n", p_value_manual))



# Hypothesis testing (Scipy implementation) .................................................

t_test <- t.test(mutant1_expr, mu = mu)

# Convert to one-sided p-value
p_value_one_sided <- if (t_test$statistic > 0) t_test$p.value / 2 else 1
cat("\nOne-sample t-test: compare sample mean to expected value (R)\n")
cat(sprintf("t statistic = %.3f\n", t_test$statistic))
cat(sprintf("p-value = %.4e\n", p_value_one_sided))



# Interpret result (significance level 0.05) ......................................................
alpha <- 0.05
if (p_value_manual < alpha) {
    cat("\np-value < significance threshold: Reject H0:\nExpression in mutant significantly different from expression in control.\n")
} else {
    cat("\np-value > significance threshold: Accept H0:\nNo evidence of expression in mutant significantly different than in control.\n")
}
