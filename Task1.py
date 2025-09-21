#Dictionary of Student Marks

marks={'Alice':85,'Aryan':95,'Chintu':68}
name=input("Enter the student's name:")


if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("student not found.")
