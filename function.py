from time import sleep


#function is the block of code that runs only  when  explicitly called

def greet(name):
    print(f"hello, {name}!!")

greet("yunus")

print("Please add the two numbers using functions:")

def add(num1, num2):
    print("adding 2 numbers:")
    result = num1 + num2
    print("Printing it from the Function defination....")
    sleep(1)
    print(f"After adding {num1} and {num2}, Result is {result}")
    return result

n1 = int(input("enter the numer1: "))
n2 = int(input("Enter the nmber2: "))

final_result=add(n1, n2) 
print(f"Printing the final result from the function call is : {final_result}")