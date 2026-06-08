age = int(input("Enter age: "))

if age < 10:
  print("Ticket Category: Child")
  print("Price: Rs 100")
elif age < 50:
  print("Ticket Category: Adult")
  print("Price: Rs 300")
else:
  print("Ticket Category: Senior")
  print("Price: Rs 250")