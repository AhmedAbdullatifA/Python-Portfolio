def SumOneDigit(n):
    if n==0:
        return 0
    else:
        result=n%10+SumOneDigit(n//10)
        result2=result%10+SumOneDigit(result//10)
        return result2
print(f"the summation of digit number until one digit of 12345 is {SumOneDigit(12345)}") 
# OR
def SumOneDigit(n):
    sum=0
    n=str(n)
    n=list(n)
    for a in n:
        a=int(a)
        sum=sum+a
    if sum<10:
        return sum 
    else:
        sum=sum%10+SumOneDigit(sum//10)
        return sum
print(f"the summation of digit number until one digit of 12345 is {SumOneDigit(12345)}")  
