codes <- c(380,124,818)
country <- c("italy", "canada", "egypt")
codes <- c(italy=380, canada=124, egypt=818)
codes
codes <- c("italy"=380, "canada"=124, "egypt"=818)
names(codes)
seq(1,10)
seq(1,10,2)
1:10
codes[2]
codes[c(1,3)]
codes[1:2]
codes["canada"]
codes[c("egypt", "italy")]


# We may create vectors of class numeric or character with the concatenate function
codes <- c(380, 124, 818)
country <- c("italy", "canada", "egypt")

# We can also name the elements of a numeric vector
# Note that the two lines of code below have the same result
codes <- c(italy = 380, canada = 124, egypt = 818)
codes <- c("italy" = 380, "canada" = 124, "egypt" = 818)

# We can also name the elements of a numeric vector using the names() function
codes <- c(380, 124, 818)
country <- c("italy","canada","egypt")
names(codes) <- country

# Using square brackets is useful for subsetting to access specific elements of a vector
codes[2]
codes[c(1,3)]
codes[1:2]

# If the entries of a vector are named, they may be accessed by referring to their name
codes["canada"]
codes[c("egypt","italy")]




x <- c(1, "canada", 3)
x
class(x)
x <- 1:5
y <- as.character(x)
y
x <- c("1","b","3")
as.numeric(x)
