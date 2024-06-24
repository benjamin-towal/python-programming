'''
Here Im going to ask the program to calculat the area of a hexagon
STEPS:
      1.Creat the variable and prompts the user to enter the side of a hexagon
      2.Calculate the sturdy numbers with the given input
Program Run;
Enter the side: 5.5
The area of the hexagon is 78.5895
'''

import math

cal_lenght = eval(input('Enter the side: '))
cal_area = (3*math.sqrt(3)*cal_lenght**2)/2
print("The area of the hexagon is", round(cal_area, 3))
