def palindrome(thing):
    if type(thing) is float :
          print("this not valid word")
    elif type(thing) is int :
         thing=str(thing)
         Reverse=thing[::-1]
         if Reverse==thing:
                print(f"the {thing} is a palindrome")
    else:
         Reverse=thing[::-1]
         if Reverse==thing:
              print(f"the {thing} is a palindrome")
palindrome("ahha")
palindrome(121)