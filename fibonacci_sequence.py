def fibonacci_sequence(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        fip=fibonacci_sequence(n-1)
        fip.append(fip[-1]+fip[-2])
        return fip