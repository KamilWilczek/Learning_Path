############# Sampling Model Parameters and Estimates #########################
## Code: Function for taking a random draw from a specific urn
# The dslabs package includes a function for taking a random draw of size n
# from the urn described in the video:
library(tidyverse)
library(dslabs)
ds_theme_set()
take_poll(25)    # draw 25 beads