# factorial of the given number by user

number = int(input("enter the number: "))

def fact(num):
    result = 1

    while num != 0:
        result = result * num
        num = num - 1

    return result

final_result = fact(number)
print(f"final result = {final_result}")