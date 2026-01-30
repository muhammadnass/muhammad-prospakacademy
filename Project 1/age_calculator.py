#This is a simple age calculator with current year set as 2026

current_year = 2026

birth_year_str = input("Enter your birth year: ")

#integer conversion

birth_year_int = int(birth_year_str)

age = current_year - birth_year_int

print(f"You are approximately {age} years old.")