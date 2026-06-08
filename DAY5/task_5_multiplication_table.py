number = int(input("Enter number: "))

print(f"---multiplication  Table of {number} ---")
for i in range(1, 11):
  result = number * i
  print(f"{number} x  {i} = {result}")