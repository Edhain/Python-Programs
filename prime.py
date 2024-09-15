def main():
    n = int(input("Enter number to check if prime or not:\n"))
    
    if n<=1:
        print("Number is NOT prime")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            print("Number is NOT prime")
            return
    
    print("Number is prime")
    
if __name__=="__main__":
    main()