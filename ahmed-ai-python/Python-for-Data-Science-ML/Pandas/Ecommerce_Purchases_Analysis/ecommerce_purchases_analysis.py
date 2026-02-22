# Ecommerce Purchases

import pandas as pd


# Q1 : Read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.
eco = pd.read_csv("EcommercePurchases")



# Q2 : Check the head of the DataFrame.
print("Head of DataFrame:")
print(eco.head(), "\n")
# Output:
# Head of DataFrame:
#                                              Address    Lot  ... Language Purchase Price
# 0  16629 Pace Camp Apt. 448\nAlexisborough, NE 77...  46 in  ...       el          98.14
# 1  9374 Jasmine Spurs Suite 508\nSouth John, TN 8...  28 rn  ...       fr          70.73
# 2                   Unit 0065 Box 5052\nDPO AP 27450  94 vE  ...       de           0.95
# 3              7780 Julia Fords\nNew Stacy, WA 45798  36 vm  ...       es          78.04
# 4  23012 Munoz Drive Suite 337\nNew Cynthia, TX 5...  20 IE  ...       es          77.82



# Q3 : How many rows and columns are there?
print(f"The number of columns is : {len(eco.columns)}")
print(f"the number of rows is : {len(eco["Address"])}","\n")
# output :
# The number of columns is 14
# and the number of rows is 10000



# Q4 : What is the average Purchase Price?
print("The average Purchase Price is :")
print(eco["Purchase Price"].mean(),"\n")
# output : 
# The average Purchase Price is :
# 50.347302



# Q5 : What were the highest and lowest purchase prices?
print(f"The highest purchase prices is : {eco['Purchase Price'].max()}")
print(f"and the lowest purchase prices is : {eco['Purchase Price'].min()}","\n")
# output :
# The highest purchase prices is : 99.99
# and the lowest purchase prices is : 0.0



# Q6 : How many people have English 'en' as their Language of choice on the website?
print("The number of people have English 'en' as their " \
f"Language of choice on the website is : {len(eco[eco['Language'] == "en"])}","\n")
# output :
# The number of people have English 'en' as their Language of choice on the website is : 1098 



# Q7 : How many people have the job title of "Lawyer" ?
n = (eco['Job'] == 'Lawyer').sum()
print(f"The number people have the job title of Lawyer is : {n}", "\n")
# output : 
# The number people have the job title of Lawyer is : 30



# Q8 : How many people made the purchase during 
# the AM and how many people made the purchase during PM ?
num_am = len(eco[eco['AM or PM'] == 'AM'].value_counts())
num_pm = len(eco[eco['AM or PM'] == 'PM'].value_counts())
print(f"The number of people made the purchase during AM is :{num_am}")
print(f"and the number of people made the purchase during PM is :{num_pm}", "\n")
# output : 
# The number of people made the purchase during AM is :4932
# and the number of people made the purchase during PM is :5068



# Q9 : What are the 5 most common Job Titles?
top = eco.groupby("Job").agg(
    count_value = ("Job","count") 
).sort_values(by = "count_value" , ascending = False).reset_index()
print(f"the 5 most common Job Titles are : \n{top.head(5)}", "\n")
# output : 
# the 5 most common Job Titles are :
#                                  Job  count_value
# 0      Interior and spatial designer           31
# 1                             Lawyer           30
# 2                  Social researcher           28
# 3                Designer, jewellery           27
# 4  Research officer, political party           27



# Q10 : Someone made a purchase that came from Lot: "90 WT" 
# , what was the Purchase Price for this transaction?
wt_90 = eco[eco["Lot"] == "90 WT"]["Purchase Price"]
print(f"the Purchase Price for this transaction came from Lot : 90 WT is \n{wt_90}", "\n")
# output : 
# the Purchase Price for this transaction came from Lot : 90 WT is
# 513    75.1
# Name: Purchase Price, dtype: float64



# Q11 : What is the email of the person with 
# the following Credit Card Number: 4926535242672853
email_card = eco[eco['Credit Card'] == 4926535242672853] ['Email']
print(f"the email of the person with \
the following Credit Card Number: 4926535242672853 is : \n{email_card}", "\n")
# output :
# the email of the person with the following Credit Card Number: 4926535242672853 is : 
# 1234    bondellen@williams-garza.com
# Name: Email, dtype: object


# Q12 : How many people have American Express as their Credit Card Provider 
# and made a purchase above $95
var = eco[(eco["CC Provider"] == "American Express") & (eco["Purchase Price"] >=95)]
print(f"The number of people who have American Express as their Credit Card \n\
Provider and made a purchase above$95 is : {len(var)}", "\n")
# output : 
# The number of people who have American Express as their Credit Card 
# Provider and made a purchase above$95 is : 39


# Q13 : Hard: How many people have a credit card that expires in 2025?
expires_at_2025 = eco[eco['CC Exp Date'].str.contains("/25",case=False)]['CC Exp Date']
print(f"The number of people have a credit card that expires in 2025 is : {len(expires_at_2025)}", "\n")
# output :
# The number of people have a credit card that expires in 2025 is : 1033



# Q14 : Hard: What are the top 5 most popular email providers/hosts 
# (e.g. gmail.com, yahoo.com, etc...)
eco["Hosts"] = eco["Email"].apply(lambda x : x[x.find('@')+1:])
top_5_email = eco.groupby("Hosts").agg(
    count_value = ("Hosts","count")
).sort_values(by = "count_value" , ascending =False).reset_index()
print(top_5_email.head(5), "\n")
# output : 
#          Hosts  count_value
# 0   hotmail.co         1638
# 1     yahoo.co         1616
# 2     gmail.co         1605
# 3     smith.co           42
# 4  williams.co           37











