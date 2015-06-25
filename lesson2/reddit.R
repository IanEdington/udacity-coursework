# what's the working directory
getwd()
# Set working dir to lesson dir
setwd("~/Dropbox/dev/udacity/EDA/lesson2")
# Read in reddit.csv into dataframe
reddit <- read.csv('reddit.csv')
# explore the data
str(data)
str(reddit)
factor(reddit)
table(reddit$employment.status)
summary(reddit)

### ploting the age.range of the members of reddit
library(ggplot2)
levels(reddit$age.range)
qplot(data = reddit, x = age.range)
# OH NO: the age.range isn't displaying properly
# make the age.range ordered
reddit$age.range <- ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))
# alternative solution
reddit$age.range <- factor(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"), ordered = T)
# plot again with ordered factors
qplot(data = reddit, x = age.range)
### using the same technique for income.range
reddit$income.range <- ordered(reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999", "$40,000 - $49,999", "$50,000 - $69,999", "$70,000 - $99,999", "$100,000 - $149,999", "$150,000 or more"))
qplot(data = reddit, x = income.range)
levels(reddit$income.range)
