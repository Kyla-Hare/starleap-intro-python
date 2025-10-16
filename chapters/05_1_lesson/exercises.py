
##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 5 Exercise 1 **********")

def time_since_epoch():
    import time
    t=time.time()
    print("t =", t)
    days = int(t // 86400)
    print(days)
    hours = int(t // 3600)
    print(hours)
    minutes = int(t // 60)
    print(minutes)
# time_since_epoch() 

   
 # Delete this line when you write your code!





# def check_fermat(a, b, c, n-and): 
#     print()
#    if a<sup>n</sup> + b<sup>n</sup> = c<sup>n</sup




#print("Ch 5 Exercise 2: Not implemented") # Delete this line when you write your code!



#print("********** Ch 5 Exercise 3 **********")

def is_t(a, b, c): 
    print('is_t()', a, b, c) 
    if a >= b + c: 
        print('no')
    elif b >= a + c: 
        print('no') 
    elif c >= a + b: 
        print('no')
    else:
        print("yes")
        
a = float(input('how long is side a? '))
print('a is', a, type(a)) 
b = float(input('how long is side b? '))
print('b is', b, type(b)) 
c = float(input('how long is side C? '))
print('c is', c, type(c)) 
# is_t(a, b, c,)

#print("Ch 5 Exercise 3: Not implemented") # Delete this line when you write your code!



#print("********** Ch 5 Exercise 4 **********")

# def recurse(n, s):
#     if n == 0:
#         print(s)
#     else:
#         recurse(n-1, n+s)

# recurse(3, 0)

#print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!
