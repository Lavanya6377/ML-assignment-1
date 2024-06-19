# Write a program that converts temperature from Celsius to Fahrenheit
# and vice versa based on user input.

temperature = float(input("Enter the temperature: "))
conversion_type = input("Enter 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ").upper()

if conversion_type == 'C':
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature} Fahrenheit is equal to {converted_temperature:.2f} Celsius.")
elif conversion_type == 'F':
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature} Celsius is equal to {converted_temperature:.2f} Fahrenheit.")