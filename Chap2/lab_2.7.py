'''
Here Im going to ask the program to find the number of years and days
Steps:
     1.Write a program tha prompts the user to enter the minutes
     2.Displays the number of years and days for the minutes
Test case;
Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
'''

input_mins = eval(input('Enter the number of minutes: '))
cal_years = (input_mins / (60 * 24 * 365))
cal_days = (input_mins / (60 * 24)) % 365
# print(cal_days)
print(input_mins, "minutes is approximately",
      round(cal_years), "years and", round(cal_days), "days")
