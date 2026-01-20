def SumDigit(n):
    if n==0:
        return 0
    else:
        result=n%10+SumDigit(n//10)
        return result
print(f"the summation of digit number of 12345 is {SumDigit(12345)}")  
# OR
def SumDigit(n):
    sum=0
    n=str(n)
    n=list(n)
    for a in n:
        a=int(a)
        sum=sum+a
    return sum
print(f"the summation of digit number of 12345 is {SumDigit(12345)}" )