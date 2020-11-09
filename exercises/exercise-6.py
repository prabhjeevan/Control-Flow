# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

month = input("Enter the month of the year (Use 3 characters only: ").lower()
day =  int(input("Enter the day of the month: "))

if month == "jan":
    print(month.upper() + " " + str(day) + " is in " + " Winter.")
elif month == "feb":
    print(month.upper() + " " + str(day) + " is in " + " Winter.")
elif (month == "mar" and day < 20):
    print(month.upper() + " " + str(day) + " is in " + " Winter.")
elif (month == "dec" and day >20):
    print(month.upper() + " " + str(day) + " is in " + " Winter.")
elif (month == "mar" and day >20):
    print(month.upper() + " " + str(day) + " is in " + " Spring.")
elif (month == "apr"):
    print(month.upper() + " " + str(day) + " is in " + " Spring.")
elif (month == "may"):
    print(month.upper() + " " + str(day) + " is in " + " Spring.")
elif (month == "jun" and day < 21):
    print(month.upper() + " " + str(day) + " is in " + " Spring.")
elif (month == "jun" and day > 20):
    print(month.upper() + " " + str(day) + " is in " + " Summer.")
elif (month == "jul"):
    print(month.upper() + " " + str(day) + " is in " + " Summer.")
elif (month == "aug"):
    print(month.upper() + " " + str(day) + " is in " + " Summer.")
elif (month == "sep" and day < 22):
    print(month.upper() + " " + str(day) + " is in " + " Spring.")
elif (month == "sep" and day > 21):
    print(month.upper() + " " + str(day) + " is in " + " Fall.")
elif (month == "oct"):
    print(month.upper() + " " + str(day) + " is in " + " Fall.")
elif (month == "nov"):
    print(month.upper() + " " + str(day) + " is in " + " Fall.")
elif (month == "dec" and day < 21):
    print(month.upper() + " " + str(day) + " is in " + " Fall.")
else:
    print("PLEASE INPUT MONTH AND DAY")

    
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.