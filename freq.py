user_string = str(input("Enter the string: "))

u_dict = {}        # user empty dictionary

for char in user_string:
    if char in u_dict:
        u_dict[char] = u_dict[char] + 1
    else:
        u_dict[char] = 1
        
for key, value in u_dict.items():
    print(f"'{key}': {value}")
        
    