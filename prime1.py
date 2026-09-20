num = int(input("Enter the number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
    else:
        is_prime = True

if is_prime == True:
    print(f"{num} is prime number!!")
else:
    print(f"{num} is not prime number!!!!!")
        