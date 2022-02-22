library(gtools)
library(tidyverse)

## Useful Information
# Permutations: # of combinations when order matters
#  formula: P_(k,n) = n!/(n-k)!
#   when n = group size, k = subset size
# Combinations: # of combinations when order does not matter
#  formula: (n k) = P_(k,n)/k! = n!/k!(n-k)!
#   when n = group size, k = subset size


####### QUESTION 1a #######
# In the 200m dash finals in the Olympics, 8 runners compete for 3 medals
#  (order matters). In the 2012 Olympics, 3 of the 8 runners were from Jamaica
#  and the other 5 were from different countries. The three medals were all
#  won by Jamaica (Usain Bolt, Yohan Blake, and Warren Weir).
str(permutations(8,3))

#_________________________
library(gtools)
medals <- permutations(8,3)
nrow(medals)
#_________________________


####### QUESTION 1b #######
# How many different ways can the three medals be distributed among the
#  3 runners from Jamaica?
str(permutations(3,3))

#_________________________
jamaica < permutations(3,3)
nrow(jamaica)
#_________________________


####### QUESTION 1c #######
# What is the probability that all three medals are won by Jamaica?
df <- combinations(8,3)
# 56 total combinations, only one with 1, 2, 3

#_________________________________
nrow(jamaica)/nrow(medals)
#_________________________________


####### QUESTION 1d #######
# Build runner countries and reset seed
runners <- c("Jamaica", "Jamaica", "Jamaica", "USA", "Ecuador", "Netherlands", "France", "South Africa")
set.seed(1)

# Run Monte Carlo 10k
B <- 10000
results <- replicate(B, {
  winners <- sample(runners, 3)
  (winners[1] %in% "Jamaica" & winners[2] %in% "Jamaica" & winners[3] %in% "Jamaica")
})
mean(results)


#______________________________________________________________________________
set.seed(1)
runners <- c("Jamaica", "Jamaica", "Jamaica", "USA", "Ecuador", "Netherlands", "France", "South Africa")
B <- 10000
all_jamaica <- replicate(B, {
  results <- sample(runners, 3)
  all(results == "Jamaica")
})
mean(all_jamaica)
#_____________________________________________________________________________

####### QUESTION 2a #######
# A restaurant manager wants to advertise that his lunch special offers
#  enough choices to eat different meals every day of the year. He doesn't
#  think his current special actually allows that number of choices, but wants
#  to change his special if needed to allow at least 365 choices.
# A meal at the restaurant includes 1 entree, 2 sides, and 1 drink. He
#  currently offers a choice of 1 entree from a list of 6 options, a choice of
#  2 different sides from a list of 6 options, and a choice of 1 drink from a
#  list of 2 options.
# How many meal combinations are possible with the current menu?

# Different meals = 6
# Different sides = 15
combinations(6,2)
# Different drink = 2
6*15*2
#_______________________________
6 * nrow(combinations(6,2)) * 2
#_______________________________

####### QUESTION 2b #######
# The manager has one additional drink he could add to the special.
# How many combinations are possible if he expands his original special
#  to 3 drink options?

6*15*3

#_______________________________
6 * nrow(combinations(6,2)) * 3
#_______________________________


####### QUESTION 2c #######
# How many meal combinations are there if customers can choose from
#  6 entrees, 3 drinks, and select 3 sides from the current 6 options?

combinations(6,3)
6*3*20

#_______________________________
6 * nrow(combinations(6,3)) * 3
#_______________________________

####### QUESTION 2d #######
# The manager is concerned that customers may not want 3 sides with their meal.
#  He is willing to increase the number of entree choices instead, but if he
#  adds too many expensive options it could eat into profits. He wants to know
#  how many entree choices he would have to offer in order to meet his goal.

# Write a function that takes a number of entree choices and returns the number
#  of meal combinations possible given that number of entree options, 3 drink
#  choices, and a selection of 2 sides from 6 options.
f <- function(entree){
  print(3*15*entree)
}

# Use sapply to apply the function to entree option counts ranging from 1 to 12.
# What is the minimum number of entree options required in order to generate more
#  than 365 combinations?
options <- seq(1:12)
sapply(options, f)

#_______________________________
library(tidyverse)

entree_choices <- function(x){
  x * nrow(combinations(6,2)) * 3
}

combos <- sapply(1:12, entree_choices)

data.frame(entrees = 1:12, combos = combos) %>%
  filter(combos > 365) %>%
  min(.$entrees)
#_______________________________


####### QUESTION 2e #######
# Write a function that takes a number of side choices and returns the number of
#  meal combinations possible given 6 entree choices, 3 drink choices, and a selection
#  of 2 sides from the specified number of side choices.
ff <- function(sides){
  3*6*nrow(combinations(sides,2))
}

# Use sapply to apply the function to side counts ranging from 2 to 12.
# What is the minimum number of side options required in order to generate
#  more than 365 combinations?
options <- 2:12
sapply(options, ff)
#_________________________________
side_choices <- function(x){
  6 * nrow(combinations(x, 2)) * 3
}

combos <- sapply(2:12, side_choices)

data.frame(sides = 2:12, combos = combos) %>%
  filter(combos > 365) %>%
  min(.$sides)
#___________________________________


####### QUESTION 3a/b/c #######
# How many groups are in the study?
esoph
nrow(esoph)

# How many cases are there?
all_cases <- sum(esoph$ncases)

# How many controls are there?
all_controls <- sum(esoph$ncontrols)


####### QUESTION 4a/b/c/d #######
# What is the probability that a subject in the highest alcohol consumption group
#  is a cancer case?
esoph %>% filter(alcgp == "120+") %>%
  summarize(sum_cases=sum(ncases), tot=sum(ncontrols) + sum(ncases), probability=sum_cases/tot)

#____________________________________________________
esoph %>%
  filter(alcgp == "120+") %>%
  summarize(ncases = sum(ncases), ncontrols = sum(ncontrols)) %>%
  mutate(p_case = ncases / (ncases + ncontrols)) %>%
  pull(p_case)
#____________________________________________________

# What is the probability that a subject in the lowest alcohol consumption group
#  is a cancer case?
esoph %>% filter(alcgp == "0-39g/day") %>%
  summarize(sum_cases=sum(ncases), tot=sum(ncontrols)+sum(ncases), probability=sum_cases/tot)

#________________________________________________________________
esoph %>%
  filter(alcgp == "0-39g/day") %>%
  summarize(ncases = sum(ncases), ncontrols = sum(ncontrols)) %>%
  mutate(p_case = ncases / (ncases + ncontrols)) %>%
  pull(p_case)
#________________________________________________________________

# Given that a person is a case, what is the probability that they smoke 10g or
#  more a day?
esoph %>% summarize(tot_cases = sum(ncases))
esoph %>% filter(tobgp != "0-9g/day") %>%
  summarize(smoking10_cases = sum(ncases))
122/200

#______________________________________________________________________________
tob_cases <- esoph %>%
  filter(tobgp != "0-9g/day") %>%
  pull(ncases) %>%
  sum()

tob_cases/all_cases
#______________________________________________________________________________

# Given that a person is a control, what is the probability that they smoke 10g or
#  more a day?
esoph %>% summarize(tot_cases = sum(ncontrols))
esoph %>% filter(tobgp != "0-9g/day") %>%
  summarize(smoking10_cases = sum(ncontrols))
450/975

#_____________________________________________________________________________
tob_controls <- esoph %>%
  filter(tobgp != "0-9g/day") %>%
  pull(ncontrols) %>%
  sum()

tob_controls/all_controls
#____________________________________________________________________________

####### QUESTION 5a/b/c/d #######
# For cases, what is the probability of being in the highest alcohol group?
esoph %>% filter(alcgp == "120+") %>%
  summarize(sum_cases=sum(ncases))
45/all_cases

#______________________________________________________________________________
high_alc_cases <- esoph %>%
  filter(alcgp == "120+") %>%
  pull(ncases) %>%
  sum()

p_case_high_alc <- high_alc_cases/all_cases
p_case_high_alc
#_____________________________________________________________________________


# For cases, what is the probability of being in the highest tobacco group?
esoph %>% filter(tobgp == "30+") %>%
  summarize(sum_cases=sum(ncases))
31/all_cases

#______________________________________________________________________________
high_tob_cases <- esoph %>%
  filter(tobgp == "30+") %>%
  pull(ncases) %>%
  sum()

p_case_high_tob <- high_tob_cases/all_cases
p_case_high_tob
#______________________________________________________________________________


# For cases, what is the probability of being in the highest alcohol group and
#  the highest tobacco group?
esoph %>% filter(alcgp == "120+" & tobgp =="30+") %>%
  summarize(sum_cases = sum(ncases))
10/all_cases

#______________________________________________________________________________
high_alc_tob_cases <- esoph %>%
  filter(alcgp == "120+" & tobgp == "30+") %>%
  pull(ncases) %>%
  sum()

p_case_high_alc_tob <- high_alc_tob_cases/all_cases
p_case_high_alc_tob
#______________________________________________________________________________



# For cases, what is the probability of being in the highest alcohol group or
#  the highest tobacco group?
esoph %>% filter(alcgp == "120+" | tobgp =="30+") %>%
  summarize(sum_cases = sum(ncases))
66/all_cases

#______________________________________________________________________________
p_case_either_highest <- p_case_high_alc + p_case_high_tob - p_case_high_alc_tob
p_case_either_highest
#______________________________________________________________________________


####### QUESTION 6a/b/c/d/e/f #######
# For controls, what is the probability of being in the highest alcohol group?
esoph %>% filter(alcgp == "120+") %>%
  summarize(contr_sum = sum(ncontrols), probability = contr_sum/all_controls)

#______________________________________________________________________________
high_alc_controls <- esoph %>%
  filter(alcgp == "120+") %>%
  pull(ncontrols) %>%
  sum()

p_control_high_alc <- high_alc_controls/all_controls
p_control_high_alc
#______________________________________________________________________________

# How many times more likely are cases than controls to be in the highest alcohol
#  group?
esoph %>% filter(alcgp == "120+") %>%
  summarize(contr_sum = sum(ncontrols), case_sum = sum(ncases),
            co_prob = contr_sum/all_controls, ca_prob = case_sum/all_cases,
            ratio = ca_prob/co_prob)

#______________________________________________________________________________
p_case_high_alc/p_control_high_alc
#______________________________________________________________________________

# For controls, what is the probability of being in the highest tobacco group?
esoph %>% filter(tobgp == "30+") %>%
  summarize(contr_sum = sum(ncontrols), probability = contr_sum/all_controls)

#_______________________________________________________________________________
high_tob_controls <- esoph %>%
  filter(tobgp == "30+") %>%
  pull(ncontrols) %>%
  sum()

p_control_high_tob <- high_tob_controls/all_controls
p_control_high_tob
#______________________________________________________________________________

# For controls, what is the probability of being in the highest alcohol group and
#  the highest tobacco group?
esoph %>% filter(tobgp == "30+" & alcgp == "120+") %>%
  summarize(contr_sum = sum(ncontrols), probability = contr_sum/all_controls)

#______________________________________________________________________________
high_alc_tob_controls <- esoph %>%
  filter(alcgp == "120+" & tobgp == "30+") %>%
  pull(ncontrols) %>%
  sum()

p_control_high_alc_tob <- high_alc_tob_controls/all_controls
p_control_high_alc_tob
#_______________________________________________________________________________

# For controls, what is the probability of being in the highest alcohol group or
#  the highest tobacco group?
esoph %>% filter(tobgp == "30+" | alcgp == "120+") %>%
  summarize(contr_sum = sum(ncontrols), probability = contr_sum/all_controls)

#______________________________________________________________________________
p_control_either_highest <- p_control_high_alc + p_control_high_tob - p_control_high_alc_tob
p_control_either_highest
#_______________________________________________________________________________


# How many times more likely are cases than controls to be in the highest alcohol
#  group or the highest tobacco group?
esoph %>% filter(alcgp == "120+" | tobgp == "30+") %>%
  summarize(contr_sum = sum(ncontrols), case_sum = sum(ncases),
            co_prob = contr_sum/all_controls, ca_prob = case_sum/all_cases,
            ratio = ca_prob/co_prob)

#_____________________________________________________________________________
p_case_either_highest/p_control_either_highest
#____________________________________________________________________________

