
##### Template for Chapter 5.14, Exercises 1 - 4 ######


# print("********** Ch 6 Exercise 1 **********")

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
# print(c(x, y+3, x+y))


# print("********** Ch 6 Exercise 2 **********")

def ack(m, n): 
    if m == 0: 
        return  n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1) 
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
# print(ack(3, 4))

# print("********** Ch 6 Exercise 3 **********")

# Exercise 3 should be worked in a new file called palindrome.py



# print("********** Ch 6 Exercise 4 **********")

# Do your work for Exercise 4 here.

# def is_power(a, b):

#     if a == 1:
#         return True 
#     elif a == b:
#         return True 
#     elif a > b:
#         return is_power(a/b,b) 
#     else: 
#         return False 

# while False:

#     n = int(input('number '))
#     result = is_power(n,3) 
#     # print(result) 
        

# # print("********** Ch 6 Exercise 5 **********")

# # Do your work for Exercise 5 

def gcd(x, y): 
    if y == 0: 
        return x 
    else:
        return gcd(y, x % y)
print(gcd(9890, 78))