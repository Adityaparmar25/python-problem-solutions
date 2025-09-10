
A = "OOTD.YOLD.ASAP.BRB.GTG.OTW"

# Write a program to separate the following into coma(,) separated values

b = A.split(".")
print(b)

# write a program to sort string alphabetically in python

a = input("Enter anything here: ")
b= sorted(a)
print(b)

# Write a program to remove a given character from a string

a = "Aditya"
b = a.replace("t","")
print(b)

# Z = "F.R.I.E.N.D.S"
# write a program to remove dot(.) from following string
z = "F.R.I.E.N.D.S"
b = z.replace(".","")
print(b)

# Write a program to check the number of occurrence of sub string in a string
a = "she sells seashells on the sea shore"
b = a.count("sea")
print("The number of times Sea is occurring is",b)


# take an input from a user as a string then , reverse it

a  = input("Enter any word of reversing it: ")
print(a[::-1])

# write a program to check if a string contains only digits

a = input("Enter anything: ")
b =a.isdigit()
if b == True:
    print("It Contains only digit")
else:print("It doesn't contains only Digit")

# Write a program to check if a string is Palindrome
a = input("Enter a word to check it is Palindrome: ")
rev = a[::-1]
if a == rev:
    print("It is Palindrome")
else:
    print("It's not a Palindrome")

# Write a program to find numbers of vowels in a string

a = input("Enter word to check Vowels: ")
vowel = 0
for i in a:
    if  i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowel+=1
print("Number of vowels in this string are",vowel)

# Write a program to check if every word in string begins with a capital letter

a = input("enter anything here: ")
print(a.istitle())