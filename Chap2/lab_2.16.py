'''
Here Im going to nask the program find the average acceleration
STEPS:
      1.Create a variable and prompts the user to enter the inputs of the variable
      2.Calculate the input to find the average acceleration 
Program Run;
Enter v0,v1,and t: 5.5, 50.9, 4.5
The average acceleration is 10.0889  

'''

velo_0, velo_1, time = eval(input('Enter v0, v1, and t: '))
cal_average = (velo_1 - velo_0)/time
print(round(cal_average, 4))
