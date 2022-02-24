library(gtools)
library(tidyverse)

set.seed(16, sample.kind = "Rounding")
n_tests <- 10000
avg_tests <- 20.9
sd_tests <- 5.7
act_scores <- rnorm(n_tests, avg_tests, sd_tests)

### Question 1a ###
mean(act_scores)


### Question 1b ###
sd(act_scores)


### Question 1c ###
sum(act_scores >= 36)


### Question 1d ###
# prob <- sum(act_scores >= 30)/10000
mean(act_scores > 30)


### Question 1e ###
mean(act_scores <= 10)



### Question 2 ###
x <- 1:36
f_x <- dnorm(x, 20.9, 5.7)
data.frame(x, f_x) %>%
  ggplot(aes(x, f_x)) +
  geom_line()


### Question 3 ###
z_scores <- (act_scores - mean(act_scores))/sd(act_scores)
mean(z_scores)
sd(z_scores)

### Question 3a ###
mean(z_scores > 2)


### Question 3b ###
2*sd(act_scores) + mean(act_scores)


### Question 3c ###
qnorm(.975, mean(act_scores), sd(act_scores))


### Question 4 ###
cdf <- sapply(1:36, function (x){
  mean(act_scores <= x)
})


### Question 4a ###
min(which(cdf >= .95))


### Question 4b ###
qnorm(.95, 20.9, 5.7)


### Question 4c ###
p <- seq(0.01, 0.99, 0.01)
sample_quantiles <- quantile(act_scores, p)
names(sample_quantiles[max(which(sample_quantiles < 26))])


### Question 4d ###
p <- seq(0.01, 0.99, 0.01)
sample_quantiles <- quantile(act_scores, p)
theoretical_quantiles <- qnorm(p, 20.9, 5.7)
qplot(theoretical_quantiles, sample_quantiles) + geom_abline()



                