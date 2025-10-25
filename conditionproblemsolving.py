#1.write a program to check if a number is positive


num = int(input("Enter a number to check: "))
if num >= 0:
    print(f"{num} is a Positive number")
else: print(f"{num} This is not a Positive number")

#2.Write a Program to check whether a number is odd or even

if num % 2 ==0:
    print(f"{num} This is a Even Number")
else:
    print(f"{num} this is a Odd number")

#3.write a program to create area calculator

print("********Area Calculator********")
print("""Press 1 to get the Area of Square 
Press 2 to get the Area of rectangle
Press3 to get the Area of Circle
Press 4 to get the Area of triangle""")

choice = int(input("Enter a number between 1-4: "))

if choice == 1:
    side = float(input("Enter the length of one Side: "))
    area = side**2
    print(f"Area of a Square is {area}")
elif choice ==2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length*width
    print(f"The Area of the Rectangle is {area}")
elif choice == 3:
    radius = float(input("Input The Raduis of the Circle: "))
    area = (22/7)*(radius**2)
    print(f"The Area of the Circle is {area}")

elif choice ==4:
    base = float(input("Enter the Base of the Triangle"))
    height = float(input("Enter the height of the Triangle"))
    area = 1/2*(base*height)
    print(f"The Area of the Triangle is {area}")

else:
    print("Invalid Input")

# 4.Write a Program to check whether the passed letter is a vowel or not

letter = input("Enter a Letter here: ")

if (letter in "aeiou") or (letter in "AEIOU"):
    print("The letter is vowel")
else: print("This is Not a Vowel letter")

#Write a program to check if a number is a single digit number,2 digit number, and so on... upto 5 digits

num1 = int(input("Input a number: "))
if num1 >= 0 and  num1 <= 9:
    print("Number digit is 1")
elif num1 >= 10 and num1 <= 99 :
    print("Your number digit is 2")
elif num1 >= 100 and num1 <= 999 :
    print("Your number digit is 3")
elif num1 >= 1000 and num1 <= 9999 :
    print("Your number digit is 4")
elif num1 >= 10000 and num1 <= 99999 :
    print("Your number digit is 5")
else: print("Youre number digit is more than 5")