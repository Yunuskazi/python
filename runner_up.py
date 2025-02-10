n = int(input())                 # input() reads the input as string 
arr = map(int, input().split())  # map converts the string to integer

arr = list(arr)                  # arr is converted t array     
sorted_arr = sorted(arr)         # using sorted() the array are sorted in ascending order
runner_up = sorted_arr[-2]       # -2 represents the last 2nd position

print(runner_up)

