''' 
Here I will ask the program to Sum the digit in an integer
steps:
1. write the program that reads an integer between 0 and 1000
2.Add all the digits in the integer
output
Enter a number between 0 and 1000:999
The sum of the digits is 27

'''
user_input = eval(input('Enter a number between 0 and 1000: '))
cal_mod = (user_input % 10)
cal_div = (user_input // 10)
cal_sum = (cal_div // 10)
sum_mod = (cal_div % 10)
total_sum = (cal_mod + cal_sum + sum_mod)
print("The sum of the digits is", total_sum)
