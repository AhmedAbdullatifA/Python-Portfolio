# 🔴 Multi-Level Aggregation Engine
# 🧩 Problem Name:
# Hierarchical Sales Analysis
# 📄 Description:
# Group by region and product.
# Compute:
# total revenue
# average revenue
# count
# Sort by highest revenue within each region.

import numpy as np
import pandas as pd


def hierarchical_sales_analysis(df):

    """
    Group by region and product.
    Compute:
    total revenue
    average revenue
    count
    Sort by highest revenue within each region. 
    """

    # Checking if its DataFrame or not
    if not isinstance(df, pd.DataFrame) :
        df = pd.DataFrame(df)

    # do the requrments :
    summary = df.groupby(["Region", "product"]).agg(
    total_revenue=("Amount", "sum"),
    average_revenue=("Amount", "mean"),
    num_revenue=("Amount", "count")
    )
    
    return summary.sort_values(by=["Region", "total_revenue"], ascending=[True, False])


# Create Data

# Create random dataset
np.random.seed(42)  # for reproducibility

# Generate 30 random transactions 
d = {
    "Region": np.random.choice(["Cairo", "Helwan", "Giza", "Alex", "Madiaa"], 30),
    "product": np.random.choice(["Labtop", "Phone", "Tablet" , "TV" , "PC" , "PS4" , "PS5"], 30),
    "Amount": np.random.randint(500, 10000, 30)
}


df = pd.DataFrame(d)


if __name__ == "__main__":
    print(hierarchical_sales_analysis(df))


# output =>    
#                 total_revenue  average_revenue  num_revenue
# Region product
# Alex   TV               10746      5373.000000            2
#        Phone             8392      8392.000000            1
#        PS5               7481      3740.500000            2
#        Tablet            4343      4343.000000            1
#        Labtop            1516      1516.000000            1
#        PC                 661       661.000000            1
# Cairo  TV                9967      9967.000000            1
#        Labtop            8416      8416.000000            1
#        Phone             7363      7363.000000            1
# Giza   PC                9867      4933.500000            2
#        Phone             9029      9029.000000            1
#        PS5               8055      8055.000000            1
#        TV                8016      4008.000000            2
#        PS4               1275      1275.000000            1
# Helwan Phone             9768      9768.000000            1
#        TV                8369      8369.000000            1
#        PS5               6175      6175.000000            1
#        Labtop            4797      4797.000000            1
#        Tablet            2085      2085.000000            1
# Madiaa PS4              18190      6063.333333            3
#        PS5               8726      8726.000000            1
#        Phone             8129      8129.000000            1
#        Tablet            7373      7373.000000            1
#        Labtop            1521      1521.000000            1


