#. Count the number of lines and number of characters and number of words in a file?
line = "Hi how are you"
word = line.split()
length = len(line)
number_of_words = len(word)

print(line)
print(word)
print(length)
print(number_of_words)


def count_file_contents(filename):
    f_line = 0
    f_char = 0
    f_word = 0

    with open(filename, "r") as file:
        for line in file:
            f_line += 1
            f_char += 1
            f_word += 1

    print(f"number of line: {f_line}")
    print(f"number of character: {f_char}")
    print(f"number of word: {f_word}")



count_file_contents("sample.txt")    
