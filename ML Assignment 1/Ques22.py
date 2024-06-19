# Write a python program that returns the minimum and maximum values
# in a list of numbers

str1 = input("enters number:")
numbers = list(map(int, str1.split()))

print(max(numbers))
print(min(numbers))