def is_prime(n):
    check_prime=0
    if type(n) is not int :
        print("invaild input")
    else:
        if n<=1:
           print(f"the number {n} is not prime")
        else:
            if n==2:
                print(f"the number {n} is prime")
            else:
                i=2
                while i<n :
                    if n%i==0:
                        check_prime=1
                        break
                    i+=1
            if check_prime!=0:
                return f"the number {n} is not prime"
            else:
                return f"the number {n} is prime"