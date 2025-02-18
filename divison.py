def div(a, b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return "trying to divide the number by zero, which is not possible"
    except TypeError:
        return "entered value is not numeric"


num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
print("Result:",div(num1, num2))