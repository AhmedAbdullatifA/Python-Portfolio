# 🔴Hard: Custom Data Profiling Report
# 🧩 Problem Name:
# Mini Data Profiling System
# 📄 Description:
# Create a function that:
# Takes a DataFrame.
# For each column:
# Detects if numeric or categorical.
# If numeric → print mean, std, min, max.
# If categorical → print number of unique values and top 3 frequent values.
# Output structured summary as a new DataFrame.

import numpy as np
import pandas as pd

def mini_data_profiling_system(df):
    """
    Creates a structured profiling report for a DataFrame.
    """
    x = 0
    lis = []
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)

    for x in df.columns :
        if pd.api.types.is_numeric_dtype(df[x]):
            lis.append({
                "Column": x, 
                "Type": "Numeric", 
                "Mean": df[x].mean(), 
                "Std": df[x].std(), 
                "Min": df[x].min(), 
                "Max": df[x].max()
            })
        else:
            lis.append({ 
                "Column": x, 
                "Type": "Categorical", 
                "Unique Values": df[x].nunique(), 
                "Top 3 Frequent": df[x].value_counts().head(3).to_dict() 
                })
    return pd.DataFrame(lis)

np.random.seed(20)

d = {
    'name' : np.random.choice(['Ahmed','Mohammed','Adham','Yasser','Hazem','Omar'],25),
    'age' :  np.random.randint(18,22,25),
    'department' : np.random.choice(['IT','CS','AI','IS'],25),
    'GPA' : np.random.uniform(2,4,25)
}

if __name__ == "__main__":
    test= mini_data_profiling_system(d)
    print(test)

#        Column         Type  Unique Values  ...       Std   Min   Max
# 0        name  Categorical            6.0  ...       NaN   NaN   NaN
# 1         age      Numeric            NaN  ...  1.011599  18.0  21.0
# 2  department  Categorical            4.0  ...       NaN   NaN   NaN
# 3         GPA      Numeric            NaN  ...  0.446582   2.0   2.0

# [4 rows x 8 columns]
