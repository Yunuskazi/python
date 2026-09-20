# Fibanocii series
# 0, 1, 1, 2, 3, 5, 8, 13

num = int(input("Enter the number: "))
a=0
b=1

while a <= num:
    print(a, end=" ")
    a, b = b, a + b


# Generating a Specific Count using a for Loop
# def generate_fib(num):
#     if num <= 0:
#         return []
#     elif num == 1:
#         return [0]
#     seq = [0, 1]

#     for i in range(2, num):
#         nxt_num = seq[-1] + seq[-2]
#         seq.append(nxt_num)

#     return seq

# print(generate_fib(10))