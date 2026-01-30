# This programs prompts a user to enter details and it will display his profile
name = input("Enter your name: ")

age = int(input("Enter your age: "))


height_cm = float(input("Enter your height in centimeters: "))

is_student = input("Are you a student? (Type 'True' or 'False'): ")

#height to inches conversion
height_inches = height_cm / 2.54

print("\n--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height_cm} cm ({height_inches:.2f} inches)")
print(f"Student: {is_student}")