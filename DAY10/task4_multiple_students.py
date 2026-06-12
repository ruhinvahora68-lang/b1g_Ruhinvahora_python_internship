students = [
    {"Name": "RUHIN", "Marks": 85},
    {"Name": "AAMENA", "Marks": 92},
    {"Name": "ZEBA", "Marks": 78}
]


for student in students:
    name = student["Name"]
    marks = student["Marks"]
    print(f"Student: {name}, Marks: {marks}")
