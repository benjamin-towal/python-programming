'''
Here Im asking the programm to convert feet into meters
1. Creat a input variable to calculate the foot of a meters
2.  And the other variable will  culculate the feet into meters

Test Case:
Enter the value of feet: 16.5
16.5 feet is 5.0325 meters

'''

cal_meters = eval(input('Enter a value for feet: '))
feet_into_meters = (0.305 * cal_meters)
print(cal_meters, 'feet is', feet_into_meters, 'meters')
