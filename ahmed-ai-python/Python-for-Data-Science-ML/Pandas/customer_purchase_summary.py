# 🟡 Customer Spending Report
# 🧩 Problem Name:
# Customer Purchase Summary
# 📄 Description:
# Given transactions DataFrame:
# Group by customer.
# Calculate:
# total spending
# average purchase
# number of transactions
# the diffrence between the high and low value 

import numpy as np
import pandas as pd


def customer_purchase_summary(df):

    """
    Given transactions DataFrame: 
    Group by customer.
    Calculate:
    total spending
    average purchase
    number of transactions
    the diffrence between the high and low value 
    """

    # Checking if its DataFrame or not
    if not isinstance(df, pd.DataFrame) :
        df = pd.DataFrame(df)

    # do the requrments :
    summary = df.groupby("Customer").agg(
    total_spending=("Amount", "sum"),
    average_purchase=("Amount", "mean"),
    num_transactions=("Amount", "count"),
    range_spending=("Amount", lambda x: x.max() - x.min())
    )
    
    return summary


# Create Data

# Create random dataset
np.random.seed(42)  # for reproducibility

# Generate 50 random transactions 
d = {
    "Customer": np.random.choice(["Ahmed", "Mohammed", "Omar", "Hazem", "Noha"], 50),
    "Amount": np.random.randint(1, 1000, 50)  # random spending between 1–1000
}


df = pd.DataFrame(d)


if __name__ == "__main__":
    print(customer_purchase_summary(df))


# output =>    
#           total_spending  average_purchase  num_transactions  range_spending
# Customer
# Ahmed               2984        426.285714                 7             677
# Hazem               8297        638.230769                13             915
# Mohammed            4929        492.900000                10             877
# Noha                4697        469.700000                10             716
# Omar                5813        581.300000                10             921

