m = int(input("Enter the starting value : "))  
n = int(input("Enter the end value : "))

for num in range(m, n + 1):  
    if num < 2:  
        continue  
    for i in range(2, num): 
        if num % i == 0:  
            break
    else: 
        print(num)