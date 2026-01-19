def count_vowels(string):
    if not isinstance(string, str):
        return "Invalid input, please enter a string."
    else:
        string=string.lower()
        vowels="aeoui"
        i=0
        for a in string:
            for b in vowels:
                if a==b:
                    i+=1
        return i