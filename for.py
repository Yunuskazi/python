from time import sleep


for i in range(1, 5):
    print(i)

# fruits = ["Apple", "Banana", "Cheery", "Grapes"]
# for fruit in fruits:
#     print(fruit)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")


c=1
while c<=3:
    print(f"c vale is {c}")
    print("Incrementing the count value\n")
    c+=1
    sleep(1)
    print(f"After incrementin the c value is {c}\n")

#break: Immediately terminates the loop completely

print("Learning the control statement (Break)")
for num in range(1, 5):
    if num == 3:
        break
    print(num)
    print("\n")


#continue: Skips the rest of the current iteration and jumps directly to the next turn of the loop.

print("Learning the control statement (Continue)")
for num in range(1, 5):
    if num == 3:
        continue
    print(num)
    print("\n")


print("Learning the control statement (Pass)")

for num in range(1, 5):
    if num == 3:
        pass  # Placeholder: I will handle this logic later
    print(num)


print("Learning the range function")
for i in range(0, 10, 2):
    print(i)  


table = int(input("Enter the number: "))
for j in range(1, 11):
    print(f"{table} x {j} = {table*j}")

option = int(input("Enter the number1: "))
for i in range(option, option * 10+1, option):
    mul = i // option
    print(f"{option} x {mul} = {i}")