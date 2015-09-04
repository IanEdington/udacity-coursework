# what's the working directory
getwd()
# Set working dir to lesson dir
setwd("~/Dropbox/dev/udacity/EDA/lesson2")
# Read in reddit.csv into dataframe
reddit <- read.csv('reddit.csv')
# explore the data
str(data)
str(reddit)
levels(reddit$age)
?factor(reddit)
table(reddit$employment.status)
summary(reddit)

### Understanding lists
alist <- list(name="Yo", 4, foo=c(3,8,9))
alist
alist[[3]]
alist[[5]] <- 'Numb'
alist$numb <- "nonumb"
alist

### NaN, NA, and NULL

alist$null <- NULL
alist[[8]] <- NULL
alist$nan <- NaN
alist$na <- NA
alist$null
alist

### ploting the age.range of the members of reddit
library(ggplot2)
levels(reddit$age.range)
qplot(data = reddit, x = age.range)
# OH NO: the age.range isn't displaying properly
# make the age.range ordered
reddit$age.range <- ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))
# alternative solution
reddit$age.range <- factor(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"), ordered = T)
levels(reddit$age.range)
# plot again with ordered factors
qplot(data = reddit, x = age.range)
### using the same technique for income.range
reddit$income.range <- ordered(reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999", "$40,000 - $49,999", "$50,000 - $69,999", "$70,000 - $99,999", "$100,000 - $149,999", "$150,000 or more"))
qplot(data = reddit, x = income.range)
levels(reddit$income.range)


### find other variables that could be factored
head(reddit, 1)
