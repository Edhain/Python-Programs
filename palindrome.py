def main():
    sum = 0
    n = int(input("Enter a number to check if it is a palindrome:\n"))
    
    temp = n
    while n >0:
        r = n % 10
        sum = (sum * 10) + r
        n = n // 10
        
    if temp == sum:
        print("Number is a palindrome")
    else:
        print("Number is NOT a palindrome")
        
if __name__=="__main__":
    main()