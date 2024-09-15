def gm(x,y):
    return (x*y)/(x+y)
    print(gm)
def arm(x,y):
    return (x+y)/2
    print(arm)
def compare(x,y):
    if (x>y):
            a='first no is greater'
            return a
            print(a)
    if (x==y):
            a='both no are equal'
            return a
            print(a)
    else:
            a='second no is greater'
            return a
            print(a)
x = int(input('Enter 1st no : '))
y = int(input('Enter 2nd no : '))
print(gm(x,y))
print(arm(x,y))
print(compare(x,y))
# a = input('Enter 1st no : ')
# b = input('Enter 2nd no : ')
# d = (a,b)
# print(d.gm())
