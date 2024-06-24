'''
Here I am asking the program to caculate the tips of the financial application
Creat the input variable to calculate subtotal and the graduity rate
Creat another variable to do the calculation of the first variable

Test case:
1. Enter the subtotal and a gratuity rate:15.69, 15
The graduity is 2.35 and the total is 18.04

'''


subtotal, gratuity = eval(input('Enter the subtotal and a gratuity rate: '))
total_gratuity = ((subtotal * gratuity) / 100)
total_subtotal = (total_gratuity + subtotal)
print("The gratuity is", round(total_gratuity, 2),
      "and the total is", round(total_subtotal, 2))
