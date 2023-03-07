# load necessary packages
library(dplyr)
library(tidyr)
library(stringr)

# create fake data
set.seed(123) # for reproducibility
df <- data.frame(
  id = 1:10,
  gender = sample(c("male", "fem"), 10, replace = TRUE),
  age = sample(18:65, 10, replace = TRUE),
  income = round(runif(10, min = 20000, max = 100000), -3),
  education = sample(c("high school", "bachelor", "master"), 10, replace = TRUE),
  marital_status = sample(c("single", "married", "divorced"), 10, replace = TRUE)
)

# view the first few rows of the data
df
# check for missing values
is.na(df)
any(is.na(df))

# consistent data
df$gender <- gsub("male", "m", df$gender)
df$gender <- gsub("fem", "f", df$gender)



df



# education -> encoding categorical data
df$education <- ifelse(df$education == "high school", 1,
                       ifelse(df$education == "bachelor", 2, 3))
df

# normalize age, income and education

df$age <- scale(df$age)
df$income <- scale(df$income)
df$education <- scale(df$education)

df


# create one-hot encoding for the "gender" variable
df$is_male <- ifelse(df$gender == "male", 1, 0)
df$is_female <- ifelse(df$gender == "female", 1, 0)


df








# remove the "gender", "id", "marital status" variable
df <- subset(df, select = -gender)
df <- subset(df, select = -id)
df <- subset(df, select = -marital_status)









# New table
df_children <- data.frame(has_children = sample(c(TRUE, FALSE), 10, replace = TRUE))

df_children


# Data integration

df <- cbind(df,df_children)
df$has_children <- ifelse(df$has_children == "TRUE", 1, 0)

df







