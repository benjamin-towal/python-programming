'''
Here Im asking the programm to convert pound into kilograms
1. Creat a input variable to calculate the pound
2.  And the other variable will  culculate the pound into kilograms

Test case:
Enter a value in pounds:55.5
55.5 pound is 25.197 kilograms

'''

pounds = eval(input('Enter a value in pounds: '))
cul_value = (0.454 * pounds)
print(pounds, 'pounds is', cul_value, 'Kilograms')
