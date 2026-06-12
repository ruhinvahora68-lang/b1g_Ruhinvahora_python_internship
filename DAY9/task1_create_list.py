numbers = []

print("Please enter 6 numbers:")

for i in range(1, 7):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print("-" * 30)
print(f"Your list of numbers: {numbers}")
