# proplem is to create Secret Message Decoder
# 🎯 Problem Statement
# You are given a string that contains a hidden message. The message is encoded using a custom rule:
# 1. 	Every word is reversed.
# 2. 	Vowels (a, e, i, o, u) are replaced with numbers:
# • 	1, 2, 3, 4, 5
# 3. 	The message may contain punctuation, which should be preserved in its original position.
# Your task is to decode the message and return the original string.
def SecretMassage(string):
    string=string[::-1]
    string=list(string)
    i=0
    for a in string:
        if a=='1':
            string[i]='a'
        elif a=='2':
            string[i]='e'
        elif a=='3':
            string[i]='i'
        elif a=='4':
            string[i]='o'
        elif a=='5':
            string[i]='u'
        i+=1
    return ''.join(string)
print(SecretMassage(" !2egassaM t2rc2S "))
