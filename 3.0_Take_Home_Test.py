'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Jackson M. Rutto



1. Write a line of code that will print your name.
'''
print ("Jackson Rutto")

'''
2. How do you enter a comment in a program?
'''
#Use a hashtag to comment

'''
3. What is the ouput of the following lines of code?
print (2/3)
print (2//3)
'''
print (2/3)
#This prints 0.6666666

print (2//3)
#This prints 0

'''
4. Write a line of code that creates a variable called pi and sets it to an
appropriate value.
'''
pi = 3.14

'''
5. Why does this code not work?
A=22
print(a)
'''
#This does not work because The variable A is uppercase and not lower case


'''
6. All of the variable names below can be used. But which of these is the best?
a
A
Area
AREA
area
areaOfRectangle - this one is best
AreaOfRectangle
'''


'''
7. Which of these variables names are not allowed in Python?
apple
Apple
APPLE
Apple2
1Apple - not allowed
account number - not allowed
account_number
account.number - not allowed
accountNumber
account# - doesnt work
'''



'''
8. Why does this code not work?
print(a)
a=45
'''
#One must print after setting the variable


'''
9. Write a line of code that will ask the user for the length of a square's
side and store the result in a variable. Make sure to convert the value
to an integer.
'''
length = float(input("Length: "))


'''
10. Write a line of code that prints the area of the square, using the
number the user typed in that you stored in question 9.
'''
print("The length is: ", length)


'''11. Do the same as in questions 9 and 10, but with the formula for the
area of an ellipse. Area=pi*a*b where a and b are the lengths of the major radii.
'''
pi = 3.14
a = float(input("a: "))
b = float(input("b: "))
area = (pi * a * b)
print("The area is:", area)

'''
12. Do the same as in questions 9 and 10, but with a formula to find
the pressure of a gas. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
n = 8.3144

'''
13. Explain the mistake in this code:
pi = float(3.14)
'''
# There is no need to say float, python already knows


'''
14. Assume radius has been defined. This code runs, but isn't very good. Explain the mistake in the following code:
x=3.14
pi=x
area=pi*radius**2
'''


'''
Assuming x and y are already defined, this code runs. But
something isn't quite right. Explain the mistake in the following code:
a=((x)*(y))
'''


'''
16. Explain the mistake in the following code:
radius = input(float("Enter the radius:"))
'''
# Float and input need to be switched