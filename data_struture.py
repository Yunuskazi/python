#string: immutable sequence of text characters enclosed in quotes

text = "python" #string
print(text[0])

#list: list the ordered, mutable sequence that allows the duplicate items
#ordered -> computer remebers the sequence/index of the elements

list = ["apple", "Banana"]
print(list)
list.append("cherry")
print(list)
print("printing the 1st item:")
print(list[0])

print("Chaging the value at 0th index")
list[0]="pineapple"
print(list)

#tuple: ordered, Immutable sequence allows the duplicate items

print("Learning Tuple")

tup = (1, 2, 2, 3)
print(tup)
print("checking the index:")
print(tup[2])

# tup[0] = 10 throws the error: 'tuple' object does not support item assignment


#set: Unordered collections of unique items with no duplicates allowed

print("learning the set")
sett = {1,2,3,4,4}
print(sett)
# print(sett[0]) this throws error, shows that set is inordered


#dictionery: unordered collection of key-value pair

print("Learning the dictionery")

user = {"name":"Yunus", "age":"25"}
print(user)
print(user["name"])