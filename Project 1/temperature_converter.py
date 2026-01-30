# This code converts temperature value from Celsius to Fahrenheit

celsius = input("Enter temperature in Celsius: ")

#float convertion
celsius_temp = float(celsius)

fahrenheit_temp = (celsius_temp * 9/5) + 32

print(f"{celsius_temp:.1f} degrees Celsius is equal to {fahrenheit_temp:.1f} degrees Fahrenheit.")