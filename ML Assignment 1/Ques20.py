# Write a python program that takes a list of numbers and returns their sum.

list1 = list(input("enter a list of numbers:"))

for i in list1:
    sum = 0
    for j in str(i):
        sum = sum + int(j)

print(sum)