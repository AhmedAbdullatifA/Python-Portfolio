# SF Salaries Exercise 

import pandas as pd



# Q1 : Load the dataset
df = pd.read_csv("Salaries.csv")



# Q2 : Check the head of the DataFrame.
print("Head of DataFrame:")
print(df.head(),  "\n")
#output:
# Head of DataFrame:
#    Id       EmployeeName  ...         Agency  Status
# 0   1     NATHANIEL FORD  ...  San Francisco     NaN
# 1   2       GARY JIMENEZ  ...  San Francisco     NaN
# 2   3     ALBERT PARDINI  ...  San Francisco     NaN
# 3   4  CHRISTOPHER CHONG  ...  San Francisco     NaN
# 4   5    PATRICK GARDNER  ...  San Francisco     NaN



# Q3 : Check the info of the DataFrame.
print("DataFrame Info:")
print(df.info(), "\n")
#output:
# DataFrame Info:
#       Column            Non-Null Count   Dtype
# ---  ------            --------------   -----
#  0   Id                148654 non-null  int64
#  1   EmployeeName      148654 non-null  object
#  2   JobTitle          148654 non-null  object
#  3   BasePay           148045 non-null  float64
#  4   OvertimePay       148650 non-null  float64
#  5   OtherPay          148650 non-null  float64
#  6   Benefits          112491 non-null  float64
#  7   TotalPay          148654 non-null  float64
#  8   TotalPayBenefits  148654 non-null  float64
#  9   Year              148654 non-null  int64
#  10  Notes             0 non-null       float64
#  11  Agency            148654 non-null  object
#  12  Status            0 non-null       float64
# dtypes: float64(8), int64(2), object(3)
# memory usage: 14.7+ MB



# Q4 : What is the average BasePay ?
print("Average BasePay:")
print(df["BasePay"].mean(), "\n")
#output: 
# Average BasePay:
# 66325.44884050643



# Q5 : What is the highest amount of OvertimePay in the dataset ?
print("Highest OvertimePay:")
print(df["OvertimePay"].max(), "\n")
#output: 
# Highest OvertimePay:
# 245131.88



# Q6 : What is the job title of JOSEPH DRISCOLL ?
print("Job title of JOSEPH DRISCOLL:")
print(df[df["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"], "\n")
#output: 
# JOB title of JOSEPH DRISCOLL:
# 24    CAPTAIN, FIRE DEPARTMENT
#Name: JobTitle, dtype: object



# Q7 : How much does JOSEPH DRISCOLL make (including benefits)?
print("TotalPayBenefits of JOSEPH DRISCOLL:")
print(df[df["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"], "\n")
#output:
# TotalPayBenefits of JOSEPH DRISCOLL:
# 24    270324.91
# Name: TotalPayBenefits, dtype: float64



# Q8 : What is the name of highest paid person (including benefits)?
print("Highest paid person:")
print(df[df["TotalPayBenefits"] == df["TotalPayBenefits"].max()], "\n")
# output:
# Highest paid person:
#        Id       EmployeeName  ...         Agency  Status
# 0       1     NATHANIEL FORD  ...  San Francisco     NaN



# Q9 : What is the name of lowest paid person (including benefits)?
print("Lowest paid person:")
print(df[df["TotalPayBenefits"] == df["TotalPayBenefits"].min()], "\n")
# output:  
# Lowest paid person:
#        Id EmployeeName  ...         Agency  Status
# 148653  148654  FREEZER, AIR  ...  San Francisco     NaN



# Q10 : What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print("Average BasePay per Year:")
print(df.groupby("Year").agg(
    average_basepay = ("BasePay","mean")
).reset_index(), "\n")
# output:
# Average BasePay per Year:
#    Year  average_basepay
# 0  2011      63564.384916
# 1  2012      65436.406857
# 2  2013      66599.690476
# 3  2014      66564.421497



# Q11 : How many unique job titles are there?
print("Unique Job Titles:")
print(df["JobTitle"].nunique(), "\n")
# output: 
# Unique Job Titles:
# 2159



# Q12 : What are the top 5 most common jobs?
print("Top 5 most common jobs:")
print(df["JobTitle"].mode(), "\n")
# output:
# Top 5 most common jobs:
# JobTitle
# Transit Operator                7036
# Special Nurse                   4389
# Registered Nurse                3736
# Public Svc Aide-Public Works    2518
# Police Officer 3                2421

############### OR   
print(df["JobTitle"].value_counts()[0:5], "\n")
# output:
# JobTitle
# Transit Operator                7036
# Special Nurse                   4389
# Registered Nurse                3736
# Public Svc Aide-Public Works    2518
# Police Officer 3                2421



# Q13 : How many Job Titles were represented by only one person in 2013? 
# (e.g. Job Titles with only one occurence in 2013?)
print("Single-occurrence Job Titles in 2013:")
print(sum(df[df["Year"] == 2013]["JobTitle"].value_counts() == 1), "\n")
# output: 
# Single-occurrence Job Titles in 2013:
# 202



# Q14 : How many people have the word Chief in their job title? 
# (This is pretty tricky)
print("People with 'Chief' in Job Title:")
print(df[df["JobTitle"].str.contains("Chief", case=False)].shape[0], "\n")
# output: 
# People with 'Chief' in Job Title:
# 627

    

# Q15 : Is there a correlation between length of the Job Title string and Salary?


df["JobTitleLength"] = df["JobTitle"].apply(len)
print("Correlation:")
print(df[["JobTitleLength", "TotalPayBenefits"]].corr() , "\n")
# => No correlation.
# output:
# Correlation:
#                       JobTitleLength  TotalPayBenefits
#   JobTitleLength          1.000000         -0.036878
#   TotalPayBenefits       -0.036878          1.000000
