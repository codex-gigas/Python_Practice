# Program to calculte surface are of cube from length of an edge

#This is was implemented by Fairoz Ahmed Shaik

'''You can calculate the surface area of a cube if you know the length of an edge.
Write a program that takes the length of an edge as input and prints
the cube’s surface area as output'''

#Taking length of an edge as input
a=float(input('Enter length of an edge of cube: '))
#s is a variable which stores the value of area of surface after performing some calculation
#To calculate the area surface of cube the formula is 6*a^2;
s=6*(a*a)
#It prints the surface area of cube.
print('The surface area of the cube is ' + str(s))

'''
Output:

Enter length of an edge of cube: 5
The surface area of the cube is 150.0

'''