# Write a program to check whether a given number is an ugly number. Return boolean (True or False)
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Sample #1:
# Input:  21
# Output: False

# Sample #2
# Input: 1
# Output: True

#Write clarifying questions

#what are ugly numbers?
#What are prime numbers? 
#look for edge-cases
    #input with zero or/and negative numbers 


def ugly_number(num):
    '''
    INPUT: A positive number
    OUTPUT: boolean
    '''
    if num == 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1

print(ugly_number(4))
print(ugly_number(30))
print(ugly_number(19))
print(ugly_number(1))



