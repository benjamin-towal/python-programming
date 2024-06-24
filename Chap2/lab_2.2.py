'''
Here I am asked to create a program that calculate the volume of a cylinder
1. I have to import the math library
2. Create two input variable to get the radius and lenght of a cylinder
3. Create another variable to calculate the area
4. And the other variable will also be to calculate the volume

Test Case:
Enter the radius and length of a cylinder:5.5, 12
The area is 95.0331
The volume is 1140.4

'''
import math


radius, lenght = eval(input('Enter the radius and lenght of a cylinder: '))
area = radius * radius * math.pi
volume = area * lenght
print("The area is", round(area, 4))
print("The volume is", round(volume, 1))
