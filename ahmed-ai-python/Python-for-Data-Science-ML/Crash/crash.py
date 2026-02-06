# first section

# Q1 : What is 7 to power of 4 ?
print(7**4) # => 2401



#Q2 : Split this string: s = "Hi there Sam!" , into a list.
s = "Hi there Sam!"
s= s.split()
print(s) # => ['Hi', 'there', 'Sam!']



# Q3 : Given the variables:
planet = "Earth"
diameter = 12742
#  Use .format() to print the following string:
# The diameter of Earth is 12742 kilometers.
print("The {} of Earth is {} kilometers".format(planet,diameter)) 
# => # The diameter of Earth is 12742 kilometers.



# Q4 : Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0]) # => hello



# Q5 : Given this nested dictionary grab the word "hello"
# Be prepared, this will be annoying/tricky
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][-1]) # => hello (الحمدالله)



# Q6 : What is the main difference between a tuple and a list?
# list is mutable you can editand change it  
# tuble is immutable you cant edit and change it



# Q7: Create a function that grabs the email website domain from a string in the form:
#So for example, passing "user@domain.com" would return: domain.com
def domainGet(s):
    i = 0
    for a in s:
        if a == '@' :
            return s[i+1:]
        i+=1

def domainGet2(email):
    return email.split('@')[-1]

print(domainGet("user@domain.com")) # => domain.com
print(domainGet2("user@domain.com")) # => domain.com


# Q8 :  Create a basic function that returns True if the word 'dog' is 
# contained in the input string Don't worry about edge cases like a punctuation 
# being attached to the word dog, but do account for capitalization.
def findDog(s):
    s = s.lower()
    return "dog" in s
print(findDog("the dog is animal")) # => True



# Create a function that counts the number of times the word "dog" 
# occurs in a string. Again ignore edge cases
def countDog(s):
    s = s.split()
    num = s.count("dog")
    return num
print(countDog('This dog runs faster than the other dog dude!')) # => 2


# Q10 :** Use lambda expressions and the filter() function to filter out 
# words from a list that don't start with the letter 's'.
seq = ['soup','dog','salad','cat','great']
L = list(filter(lambda item : item[0] == 's',seq))
print(L) # => ['soup', 'salad']



# Q11 :You are driving a little too fast, and a police officer stops you. 
# Write a function to return one of 3 possible results: 
# "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". 
# If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
# If speed is 81 or more, the result is "Big Ticket". 
# Unless it is your birthday (encoded as a boolean value in 
# the parameters of the function) -- on your birthday, 
# your speed can be 5 higher in all cases. 
def caught_speeding(speed, is_birthday):
    if is_birthday :
        if speed <= 65:
            return "No ticket"
        elif speed > 65 and speed < 85 :
            return  "Small ticket"
        else : 
            return "big ticket"
    else:
        if speed <= 60:
            return "No ticket"
        elif speed > 60 and speed < 80:
            return  "Small ticket"
        else : 
            return "big ticket"
print(caught_speeding(81,True)) # => Small ticket
print(caught_speeding(81,False)) # => big ticket
