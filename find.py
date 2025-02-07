user_string = str(input("Enter the string: "))
sub_string = str(input("Enter the string to be found: "))

index = user_string.find(sub_string)

while index != -1:
    print(index)
    index = user_string.find(sub_string, index+1)