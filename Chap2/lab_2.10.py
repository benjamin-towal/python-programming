'''
Here Im going to tell the program to calculate the runway lenght
STEPS;
      1. Creat a input variable,write a program that prompts the user to enter 'v' in m/s and the acceleration 'a' in m/s squared
      2. Display the minimum runway lenght
Test Case:
Enter speed and acceleration: 60, 3.5
The minimum runway lenght for the airplane is 514.286 meters 

'''

v, a = eval(input('Enter speed and acceleration: '))
cal_lenght = pow(v, 2) / (2 * a)
print('The minimum runway lenght for this airplane is',
      round(cal_lenght, 3), 'meters')
