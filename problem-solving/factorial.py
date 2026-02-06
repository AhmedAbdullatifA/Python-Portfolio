def factorial(n):
    if n <0:
        return "factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else :
        return n*factorial(n-1)
    return f"the factorial of number 5 equals {factorial(5)}"
print(factorial(-6))
