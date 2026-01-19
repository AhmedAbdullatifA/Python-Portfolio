list1 =[1,2,3,4,5,1,2,3,4]
def unique_number(list):
    for q in list:
        if type(q) is not int :
            print("this list is not valid")
            break
    if len(list)%2==0 :
        print("this list is even number and dont have a unique number")
    else :
            for x in list :
                if list.count(x)==1 :
                    print(f"the unique number is {x}")
unique_number(list1)