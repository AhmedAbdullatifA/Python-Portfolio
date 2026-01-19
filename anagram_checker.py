def anagram_checker(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if sorted(str1) == sorted(str2):
        print(f" {str1} and {str2} are anagrams")
    else:
        print(f" {str1} and {str2} are not anagrams")