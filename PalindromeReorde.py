def PalindromeReorder(string : str) -> str:
    list1=list(string)
    x=0
    c=""
    for a in list1 :
        if list1.count(a) %2==1 and len(list1) %2==0:
            return "NO SOLUTION"
        elif list1.count(a) %2==1:
            x+=1
            c=a
            list1.remove(a)
    if len(list1) %2==1 and x>2:
        return "NO SOLUTION"
    else :
        list1.sort()
        y="".join(list1)
        return y[::2] + c + y[::-2]
    
print(PalindromeReorder("AAAACACBA"))  # "AACABACAA"
print(PalindromeReorder("aaaaaaccccccvvvv")) # "abccba" + "abccba"