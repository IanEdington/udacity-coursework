# Read and Subset Data

getwd()
setwd("/Users/ian/Dropbox/dev/udacity/EDA/lesson2")

statesInfo <- read.csv('stateData.csv')
subset(statesInfo, state.region == 1)
statesInfo[statesInfo$state.region == 1, ]

str(statesInfo)
 