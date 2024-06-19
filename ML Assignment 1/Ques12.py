# Write a python program that calculates the sum of the digits of a given
# number
number = int(input("Enter no.:"))
sum =0
for i in str(number):
    sum=sum + int(i)

print(sum)