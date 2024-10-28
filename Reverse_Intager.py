# Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reversed_digit_ordering(intager):
  
    if intager < 0:
        reversed_order = '-' + str(intager)[:0:-1]  
    else:
        reversed_order = str(intager)[::-1]  
    
    return int(reversed_order)


print(reversed_digit_ordering(500))   
print(reversed_digit_ordering(-56))  
print(reversed_digit_ordering(-90))   
print(reversed_digit_ordering(91))   
