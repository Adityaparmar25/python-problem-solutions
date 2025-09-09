#write a program to swap to variable

# methed1

x=12
y=13

temp = x
print ('value of temp is:',temp)
x=y
print('value of x is: ', x)
y=temp
print('value of y is: ',y)

# method2
a=40
b=30
a,b=b,a
print('value of a is: ',a)
print('value of b is: ',b)

# write a program to convert a float into integer

x = 12.4
print(type(x))

x=int(x)
print(x)
print('now conversion done: ',type(x))


# write a program to take details from a student for
# ID-card and then print it in different lines.


name = input("The name of student:")
grade= input("Enter student Class:")
roll = int(input("enter student roll no.:"))
ph_no= int(input("Student phone no. "))

print("Student Identity Card ")
print('name: ',name)
print('Class: ',grade)
print('Roll no.:' ,roll)
print("Contact no.: ",ph_no)

# Write a program to take an user input as integer
# then convert it to float

p = int(input('Enter a number here:'))
print(p)
print(type(p))

p = float(p)
print(p)
print(type(p))