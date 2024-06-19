# Write a python program that generates the first n numbers in the
# Fibonacci sequence

import math as mt
Numbers = int(input("enter first n numbers"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, Numbers):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()