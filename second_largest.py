def SecondLargest(list):
    max1=0
    list2=list.copy()
    for a in list:
        if a>max1:
            max1=a
    list2.remove(max1)
    max2=0
    for b in list2:
        if b>max2:
            max2=b
    return max2