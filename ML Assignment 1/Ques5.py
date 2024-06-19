# Write a program that takes a string input from the user and writes it to a
# text file

Name = (input("enter your name:"))
samplefile = open('C:/Users/ASUS/PycharmProjects/ML Assignment 1/Ques5 txt file.txt','w')
print(Name,file=samplefile)