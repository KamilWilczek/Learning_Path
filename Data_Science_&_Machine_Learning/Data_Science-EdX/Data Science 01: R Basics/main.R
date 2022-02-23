library(dslabs)
data(heights)
options(digits = 3) 

avg_height <- mean(heights$height)
ind <- heights$height > avg_height
sum(ind)

x <- heights$height > avg_height & heights$sex == "Female"
sum(x)
women <- heights$sex == "Female"
mean(women)

min_h <- min(heights$height)
match(min_h, heights$height)
heights$sex[match(min_h, heights$height)]

max_h <- max(heights$height)

x <- 50:82
sum(!(x %in% heights$height))

ht_cm <- heights$height * 2.54
ht_cm[18]
mean(ht_cm)
heights2 <- mutate(heights, ht_cm)

females <- filter(heights2, heights2$sex == "Female")
mean(females$ht_cm)


library(dslabs)
data(olive)
head(olive)
plot(olive$palmitic, olive$palmitoleic)

hist(olive$eicosenoic)

boxplot(olive$palmitic~olive$region)
