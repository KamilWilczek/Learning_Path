library(tidyverse)

### Question 1a ###
# What is the probability of guessing correctly for one question?
p <- 1/5 # one correct choice of 5 options
p

### Question 1b ###
# What is the expected value of points for guessing on one question?
a <- 1
b <- -0.25
mu <- a*p + b*(1-p)
mu

### Question 1c ###
# What is the expected score of guessing on all 44 questions?
n <- 44
n*mu

### Question 1d ###
# What is the standard error of guessing on all 44 questions?
sigma <- sqrt(n) * abs(b-a) * sqrt(p*(1-p))
sigma

### Question 1e ###
# Use the Central Limit Theorem to determine the probability that a guessing student scores 8 points or higher on the test.
1-pnorm(8, mu, sigma)

### Question 1f ###
# Set the seed to 21, then run a Monte Carlo simulation of 10,000 students guessing on the test.
# What is the probability that a guessing student scores 8 points or higher?
set.seed(21, sample.kind = "Rounding")
B <- 10000
n <- 44
p <- 0.2
tests <- replicate(B, {
  X <- sample(c(1, -0.25), n, replace = TRUE, prob = c(p, 1-p))
  sum(X)
})
mean(tests >= 8)


### Question 2a ###
# Suppose that the number of multiple choice options is 4 and that there 
# is no penalty for guessing - that is, an incorrect question gives a score of 0.

# What is the expected value of the score when guessing on this new test?
p <- 1/4
a <- 1
b <- 0
n <- 44
mu <- n * a*p + b*(1-p)
mu


### Question 2b ###
# Consider a range of correct answer probabilities p <- seq(0.25, 0.95, 0.05) 
# representing a range of student skills.

# What is the lowest p such that the probability of scoring over 35 exceeds 80%?
p <- seq(0.25, 0.95, 0.05)
exp_val <- sapply(p, function(x){
  mu <- n * a*x + b*(1-x)
  sigma <- sqrt(n) * abs(b-a) * sqrt(x*(1-x))
  1-pnorm(35, mu, sigma)
})

min(p[which(exp_val > 0.8)])


### Question 3a ###
# What is the expected value of the payout for one bet?
p <- 5/38
a <- 6
b <- -1
mu <- a*p + b*(1-p)
mu

### Question 3b ###
# What is the standard error of the payout for one bet?
sigma <- abs(b-a) * sqrt(p*(1-p))
sigma

### Question 3c ###
# What is the expected value of the average payout over 500 bets?
(6*5/38 + -1*(1 - 5/38))
mu
# same as after one bet, because after 500 best it is stil same prob for bet

### Question 3d ###
# What is the standard error of the average payout over 500 bets?
n <- 500
sigma/sqrt(n)

### Question 3e ###
# What is the expected value of the sum of 500 bets?
n*mu

### Question 3f ###
# What is the standard error of the sum of 500 bets?
sqrt(n) * sigma

### Question 3g ###
# Use pnorm() with the expected value of the sum and standard error of the sum 
# to calculate the probability of losing money over 500 bets.
pnorm(0, n*mu, sqrt(n)*sigma)
