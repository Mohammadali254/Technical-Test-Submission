# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

def check_pangram(word):
   
    phrase = set("abcdefghijklmnopqrstuvwxyz")
    
   
    word = set(word.lower().replace(" ", ""))
    
   
    return phrase.issubset(word)


print(check_pangram("The quick brown fox jumps over the lazy dog"))  
                               
