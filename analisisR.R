library(readr)

library(readr)
data1 <- read_csv("~/Desktop/Git/Caos/osc15-EST-01.csv")
View(osc15_EST_01)
head(data1)
data1$...5 <- NULL
data1$...6 <- NULL 
data1$...7 <- NULL 
data1$...8 <- NULL 
data1
head(data1)
summary(data1)
