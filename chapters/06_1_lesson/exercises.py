
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

# def ack(m, n): 
    
    
# print("********** Ch 6 Exercise 3 **********")

# Exercise 3 should be worked in a new file called palindrome.py



# print("********** Ch 6 Exercise 4 **********")

# Do your work for Exercise 4 here.

def is_power(a, b):

    if a == 1:
        return True 
    elif a == b:
        return True 
    elif a > b:
        return is_power(a/b,b) 
    else: 
        return False 

while True:

    n = int(input('number '))
    result = is_power(n,3) 
    print(result) 
        

# print("********** Ch 6 Exercise 5 **********")

# Do your work for Exercise 5 here.

# print("Ch 6 Exercise 5: Not implemented") # Delete this line when you write your code!
