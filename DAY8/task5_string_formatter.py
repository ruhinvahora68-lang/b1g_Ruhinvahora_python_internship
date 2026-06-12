name = input("Enter your name: ")
city = input("Enter your city: ")


f_name = name.strip().title()
f_city = city.strip().title()


message = f"My name is {f_name} and I live in {f_city}"

print(message)
