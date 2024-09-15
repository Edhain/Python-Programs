# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(9))
def fibseries(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    else:
        return fibseries(n-1)+ fibseries(n-2)
        
print(fibseries(8))