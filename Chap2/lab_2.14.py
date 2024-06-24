'''
Here Im going to ask the program to calculat the area of a triangle
STEPS:
      1.Creat a variable and prompts the user to enter the three points of a triangle
      2.Calculate the variables using the formula of geometry
      3.Enter the inputs by adding the sides of the triangle and divided it by two
      4.The answer of the inputs you will calculate it using the area of a triangle
Program Run;
Enter three points of a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6

'''
import math

x1, y1, x2, y2, x3, y3 = eval(input('Enter three points of a triangle: '))
side_1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
side_2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
side_3 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
total_sides = (side_1 + side_2 + side_3)/2
cal_area = math.sqrt(total_sides * (total_sides-side_1) *
                     (total_sides-side_2)*(total_sides-side_3))
print('The area of the triangle is', (round(cal_area, 2)))
