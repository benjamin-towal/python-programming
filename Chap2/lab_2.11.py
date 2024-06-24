'''

Here Im going to ask the program to find the Initial deposit value
STEPS;
     1. Creat three input variables and prompts the user to enter the inputs
     2. The user will first enter the final account value
     3. Secondly, the annual inerest rate in persent
     4. Lastly the number of years
     5. And the program will calculate and displays the initial deposit amount
Test Case:
Enter final account value: 1000
Enter annual interest rate in persent: 4.25
Enter number of years: 5
Initial deposit value is 808.8639197424636

'''

account_value = eval(input('Enter final account value: '))
input_percent = eval(input('Enter annual interest rate in percent: '))
input_year = eval(input('Enter number of years: '))
initial_deposit_amount = (
    account_value / (1 + (input_percent/1200))**(input_year*12))
print("The initial deposit value is", initial_deposit_amount)
