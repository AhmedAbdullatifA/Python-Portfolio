# 🔴 Multi-Condition Data Filtering
# 🧩 Problem Name:
# Advanced Employee Performance Filter
# 📄 Description:
# Filter employees who:
# Salary > company average
# Work in departments with more than 5 employees
# Have performance score in top 25%
# Return final filtered DataFram

import numpy as np
import pandas as pd

def employee_performance_filter(df):
    """
    Filter employees who: Salary > company average and Work in departments 
    with more than 5 employees and Have performance score in top 25%
    """
    # Checking if its DataFrame or not
    if not isinstance(df,pd.DataFrame):
        df = pd.DataFrame(df)

    # Create column where Salary > company average
    df['company_average'] = df['salary'].mean()

    # Create column to count departments with more than 5 employees
    df['counting_department'] = df.groupby('department')['department'].transform("count")

    # return the result with the condition
    return df[(df['salary'] > df['company_average'])  
              & (df ['counting_department'] > 5)  
              & (df['performance_score'] > df['performance_score'].quantile(0.75)) ]


# to make the random data constant
np.random.seed(101)


# Create Random Data
d = {
    'employee_id' : np.arange(1,51),
    'department'  : np.random.choice(["Ai Engineer","Data Analaysis","Full-Stack",
    "Data Engineer","IT Consulat","Cyper Security"],50),
    'salary'      : np.random.randint(10000,50000,50),
    'performance_score' : np.random.randint(1,10,50)
}

df = pd.DataFrame(d)

print(df)

if __name__ == "__main__":
    print(employee_performance_filter(df))

# output =>
#     employee_id   department  salary  performance_score  company_average  counting_department
# 27           28  Ai Engineer   31331                  9         28816.24                   10
# 43           44  Ai Engineer   49865                  8         28816.24                   10
# 49           50  IT Consulat   40710                  8         28816.24                   12     