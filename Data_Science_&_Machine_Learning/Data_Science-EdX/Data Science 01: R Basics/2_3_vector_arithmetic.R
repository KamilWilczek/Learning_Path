murders$state[which.max(murders$population)]
max(murders$population)

heights <- c(69, 62, 66, 70, 70, 73, 67, 73, 67, 70)
heights * 2.54
mean(heights)
heights - 69

# The name of the state with the maximum population is found by doing the following
murders$state[which.max(murders$population)]

# how to obtain the murder rate
murder_rate <- murders$total / murders$population * 100000

# ordering the states by murder rate, in decreasing order
murders$state[order(murder_rate, decreasing=TRUE)]