# 🟡 Employee Salary Filter
# 🧩 Problem Name:
# Department Salary Analysis
# 📄 Description:
# Given a DataFrame with:
# employee_id
# department
# salary
# Tasks:
# Calculate average salary per department.
# Return employees earning above their department average.     

import numpy as np
import pandas as pd

def department_salary_analysis(df) :
    """
    Calculate average salary per department
    and return employees earning above their department average.
    """
    # Checking if its DataFrame or not
    if not isinstance(df,pd.DataFrame) :
        df = pd.DataFrame(df)

    # Calculate department average salary for each employee
    df["dept_avg_salary"] = df.groupby("department")["salary"].transform("mean")

    # Filter employees earning above department average
    result = df[df["salary"] > df["dept_avg_salary"]]

    return result


np.random.seed(101)

d = {
    'employee_id' : np.arange(1,101),
    'department'  : np.random.choice(["Ai Engineer","Data Analaysis","Full-Stack",
    "Data Engineer","IT Consulat","Cyper Security"],100),
    'salary'      : np.random.randint(10000,50000,100)
}

df = pd.DataFrame(d)

print(department_salary_analysis(df))

if __name__ == "__main__":
    print(department_salary_analysis(df))