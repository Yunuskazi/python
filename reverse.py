#Reverse a string

user_string = str(input("enter the string: "))

rev_string = ""

for char in user_string:
    print(f"char in the loop {char}")
    rev_string = char + rev_string
    print(f"reverse strin in the loop {rev_string}")

print(rev_string)


#####################################################################
#method 2 
# by slicing method

string = str(input("enter the string: "))

rev_str = string[::-1]

print(rev_str)

####################################################################
# Check the pallindrome

if ({string} == {rev_str}):
    print("string is pallindrome!!!!")
else:
    print("string is not palllindrome!!!!!!!!")