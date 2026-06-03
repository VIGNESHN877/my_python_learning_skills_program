"""
def add(n):
    print(n)
    return add(n-1)

ans=add(12)   # RecursionError: maximum recursion depth exceeded
"""

"""def add(n):  # this line funtion
    print(n) # this line print statement
    if n==0: # if condition is n==0 
        return n# this line return to the n
    return add(n-1) # this line return add statement act as a recursion statement 
   
number = int(input("Enter a number : "))
add(number)   # RecursionError: maximum recursion depth exceeded"""

"""

 1. Base case 
 2.Recursive Case 

"""

"""def sum_of_n(n):
    # Base case 
    if n==0:
        return 0
    return n+ sum_of_n(n-1)

n = int(input("Enter the vaule : "))
print(sum_of_n((n)))
"""
"""
def sum1(n1):
    if n1==0 :
        return 0
    return n1 + sum1(n1-1)


print(sum1(22))"""



def factorial(n): # this line called has a factorial function (n) but this function program fromla 
    if (n==0):  # if condition as a n == 0 condition was runnig and but condition once failur go the else 
        return 1
    else :
        return n * factorial(n-1)  # return to n value and multiple wwith a n*n-1= factorial ans 
    
result = factorial(6)

print(result)

def addfac(n):
    if (n==0):
        return 1
    else :
        return n * addfac(n-1)

result1=addfac(5)
print(result1)

def sum1(s):

    return 1 if(s==0) else s * (s-1) 
print(sum1(12))


def adds(a,b):
    return  a+b


print(adds(22,222))