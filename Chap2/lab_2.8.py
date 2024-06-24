'''

Here Im going to ask the program to calculates the energy needed heat water from an initial to a final temperature
STEPS:
     1.Creat a variable and prompt the user to enter the amount of water in kilograms
     2.Creat another two variable to prompt the user to enter the initial and final temperature of the water
Test Case;
 Enter the amount of wter in kilogramns: 55.5
 Enter the initial temperature: 3.5
 Enter the final temperature: 10.5
 The energy needed is 1625484.0

'''

input_kilo = eval(input('Enter the amount of water in kilograms: '))
initial_temperature = eval(input('Enter the initial temperatuer: '))
final_temperature = eval(input('Enter the final temperature: '))
cal_total = input_kilo * (final_temperature - initial_temperature) * 4184
print('Enter energy needed is', cal_total)
