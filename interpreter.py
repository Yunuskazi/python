import time

print("🟢 Step 1: Starting the program...")
time.sleep(1)  # Pauses for 1 second

print("🟡 Step 2: The interpreter is reading code line-by-line...")
time.sleep(1)  # Pauses for 1 second

print("🟠 Step 3: Almost at the error...")
time.sleep(1)  # Pauses for 1 second

# 🚨 This line has a mistake (you cannot divide a number by zero)
result = 10 / 0 

print("🔵 Step 4: This line will NEVER run.")