'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Jackson M. Rutto



1. Write a line of code that will print your name.
'''
print ("Jackson Rutto")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?
'''
name = (input("What is your name?" ))
print(name)

'''
3. Predict the output of the following lines of code and then test them? Write down your prediction and the output.
print (17/9) - divide 17 by 9 --- 1.888
print (17//9) - floor 17 by 9 --- 1
print (17%9) - square root? --- 8
'''



'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.
'''
b = float(input("Base of triangle: "))
h = float(input("Height of triangle: "))
area = ((b / 2) * h)
print(area)

'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
a = "May the force be with you!"
print(a)



'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
l = float(input("Length of square: "))
area = (l ** 2)
print(area)

'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
pi = 3.14
a = float(input("Length of first major radii: "))
b = float(input("Length of other major radaii: "))
area = (pi * a * b)
print(area)
'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
n = float(input("Number of moles: "))
v = float(input("Volume: "))
t = float(input("Temperture (K): "))
r = 8.3144
p = (n * r * t) / v
print(p)

'''
9. Ask a user for an integer and then print the square root.
'''
import math
number = int(input("Enter an integer for its square root: "))
answer = (math.sqrt(number))
print(answer)

'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
mass = float(input("Mass of object: "))
acc = float(input("Acceleration: "))
force = mass * acc
print(force)