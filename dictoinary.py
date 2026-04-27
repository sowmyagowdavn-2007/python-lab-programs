# Create a dictionary
student = {
    "name": "Sowmya",
    "age": 20,
    "course": "BCA"
}

# Search for a key
key = input("Enter key to search: ")

if key in student:
    print("Key found!")
    print("Value:", student[key])
else:
    print("Key not found")

# Search for a value
value = input("Enter value to search: ")

if value in student.values():
    print("Value found!")
else:
    print("Value not found")
