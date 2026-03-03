# Lab 4: User Profile Creator

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in centimeters: "))
student_status = input("Are you a student? (Type 'True' or 'False'): ")

height_inches = height_cm / 2.54

print("\n--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height_cm:.2f} cm ({height_inches:.2f} inches)")
print(f"Student: {student_status}")
print("--------------------")