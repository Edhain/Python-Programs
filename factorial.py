def main():
    fact = 1
    
    n = int(input("Enter a number:\n"))
    
    for i in range(1,n+1):
        fact = fact * i
    
    print("The factorial of ", n, "is ", fact)

if __name__=="__main__":
    main()