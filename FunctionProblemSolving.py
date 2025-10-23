# write a function to find maximum of the three number in python

def maximum_num(val1,val2,val3):
    if val1 > val2 and val1 >val3:
        print(val1,"is Greatest number")
    elif val2 > val1 and val2 > val3:
        print(val2,"is Greatest number")
    else:
        print(val3,"is Greatest number")

maximum_num(8,16,9)

# Write a python function to create and print a list where the values are square of numbers between 1 and 30

def create_list():
    l = [ ]
    for i in range(1,31):
        l.append(i**2)

    return l
print(create_list())

# write a python function that takes a number as a parameter and check ig the number is prime or not

def check_prime(num):
    if num == 1:
        print("It is not a Prime number")

    if num == 2:
        print("It is a Prime number")
    if num > 2:
        for i in range(2,num):
            if num % i ==0:
                print("It is not a Prime number")
                break

            else:
                print("It is a Prime number")

check_prime(11)

# Write a python function to sum all the number in a list

# Method 1

def add(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return (total)
print(add([52,99,45,2,5]))

# Method 2 (Using Recursion)
def add(numbers):
    if len(numbers) == 1:
        return (numbers[0])
    else:
        return (numbers[0] +add(numbers[1:]))

print(add([52,99,45,2,5]))

# Write a python program to solve the fibonacci sequence using recursion

def fs(num):
    if num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        return (fs(num-1) + fs(num-2))

print(fs(10))
