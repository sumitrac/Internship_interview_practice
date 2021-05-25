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
    # Ugly numbers are those number whose prime factors are 2, 3 or 5. 
    # From 1 to 15, there are 11 ugly numbers 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15. 
    # The numbers 7, 11, 13 are not ugly because they are prime. 
    # The number 14 is not ugly because in its prime factor the 7 will come.

#What are prime numbers?
    # prime numbers are whole numbers greater than 1, that have only two factors – 1 
    # and the number itself. Prime numbers are divisible only by the number 1 
    # or itself. For example, 2, 3, 5, 7 and 11 are the first few prime numbers.

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
            num = i/i
    return num == 1

print(ugly_number(4))
print(ugly_number(30))
print(ugly_number(19))
print(ugly_number(1))



