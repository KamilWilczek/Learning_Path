options(digits = 3)    # report 3 significant digits
library(tidyverse)
library(titanic)

titanic <- titanic_train %>%
  select(Survived, Pclass, Sex, Age, SibSp, Parch, Fare) %>%
  mutate(Survived = factor(Survived),
         Pclass = factor(Pclass),
         Sex = factor(Sex))



# A faceted plot is useful for comparing the distributions of males and 
# females for A. Each sex has the same general shape with two modes at the 
# same locations, though proportions differ slightly across ages and there are 
# more males than females.

## "Females and males had the same general shape of age distribution."
titanic %>%
  ggplot(aes(Age, fill = Sex)) +
  geom_density(alpha = 0.2) +
  facet_grid(Sex ~ .)

# A stacked density plot with count on the y-axis is useful for answering B, 
# C and D. The main mode is around age 25 and a second smaller mode is around 
# age 4-5. There are more males than females as indicated by a higher total 
# area and higher counts at almost all ages. With count on the y-axis, it is 
#clear that more males than females are age 40.

## "The age distribution was bimodal, with one mode around 25 years of age and a second smaller mode around 5 years of age."
## "There were more females than males."
## "The count of males of age 40 was higher than the count of females of age 40."
titanic %>%
  ggplot(aes(Age, y = ..count.., fill = Sex)) +
  geom_density(alpha = 0.2, position = "stack")

# A plot filled by sex with alpha blending helps reveal the answers to E, F 
# and G. There is a higher proportion of females than males below age 17, 
# a higher proportion of males than females for ages 18-35, approximately the 
# same proportion of males and females age 35-55, and a higher proportion of 
# males over age 55. The oldest individuals are male.

## "The proportion of males age 18-35 was higher than the proportion of females age 18-35."
## "The proportion of females under age 17 was higher than the proportion of males under age 17."
## "The oldest passengers were female."
titanic %>%
  ggplot(aes(Age, fill = Sex)) +
  geom_density(alpha = 0.2)



params <- titanic %>%
  filter(!is.na(Age)) %>%
  summarize(mean = mean(Age), sd = sd(Age))

p <- titanic %>% filter(!is.na(Age)) %>%
  ggplot(aes(sample = Age)) +
  geom_qq(dparams = params) +
  geom_abline()
p

b <- titanic %>%
  ggplot(aes(x = Survived, fill = Sex)) +
  geom_bar(position = position_dodge())
b


#plot 1 - survival filled by sex
titanic %>%
  ggplot(aes(Survived, fill = Sex)) +
  geom_bar()
# plot 2 - survival filled by sex with position_dodge
titanic %>%
  ggplot(aes(Survived, fill = Sex)) +
  geom_bar(position = position_dodge())
#plot 3 - sex filled by survival
titanic %>%
  ggplot(aes(Sex, fill = Survived)) +
  geom_bar()

# Question 5: Survival by Age
titanic %>%
  ggplot(aes(x=Age, y = ..count.., fill = Survived)) +
  geom_density(alpha = 0.2)

# Question 6: Survival by Fare
titanic %>% 
  filter(Fare > 0) %>%
  ggplot(aes(Survived, Fare)) +
  geom_boxplot(aplha=0.2) +
  scale_y_continuous(trans="log2") + 
  geom_point(show.legend = FALSE) + 
  geom_jitter()

# Question 7: Survival by Passenger Class
# barplot of passenger class filled by survival
titanic %>%
  ggplot(aes(Pclass, fill = Survived)) +
  geom_bar() +
  ylab("Proportion")
# barplot of passenger class filled by survival with position_fill
titanic %>%
  ggplot(aes(Pclass, fill = Survived)) +
  geom_bar(position = position_fill()) +
  ylab("Proportion")
# Barplot of survival filled by passenger class with position_fill
titanic %>%
  ggplot(aes(Survived, fill = Pclass)) +
  geom_bar(position = position_fill()) +
  ylab("Proportion")

# Question 8: Survival by Age, Sex and Passenger Class
titanic %>%
  ggplot(aes(x = Age, y = ..count.., fill = Survived)) +
  geom_density(alpha = 0.2) +
  facet_grid(Pclass ~ Sex)
