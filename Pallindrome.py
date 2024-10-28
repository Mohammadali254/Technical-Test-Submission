# Write a Python function that checks whether a word or phrase is palindrome or not

def check_palindrome(word):
  
    phrase = ''.join(word.lower().split())
    
    
    return phrase == phrase[::-1]


print(check_palindrome("hello")) 
print(check_palindrome("kayak"))
print(check_palindrome("nurses run"))  
print(check_palindrome("madam"))
print(check_palindrome("racecar"))        
      
     
  
       
