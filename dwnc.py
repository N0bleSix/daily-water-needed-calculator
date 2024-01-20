#This is a program that can calculate and tell you how much water you need to drink daily based on your weight.

#Requests input from the user as to what their weight is.
weight = input('How much do you weigh in pounds/kilos?')

#Prints to the user that they weight what they inputed for the 'weight' variable.
your_weight = print('You weigh ' + weight + '.')

#Converts the 'weight' variable to a float and multiplies it by half.
weight_in_half = float(weight) * 0.5

#Converts the 'weight_in_half' variable to an integer, so it will not be in decimal form even as a whole number.
daily_water_needed = int(weight_in_half)

#Prints to the user the amount of water intake needed daily in ounces.
print('Your recommended daily water intake is ' + str(daily_water_needed) + ' ' + 'ounces.')