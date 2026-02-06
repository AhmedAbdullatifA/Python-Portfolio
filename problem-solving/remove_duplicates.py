def RemoveDuplicates(list):
    for a in list :
        if list.count(a)>1:
            list.remove(a)
    return list
