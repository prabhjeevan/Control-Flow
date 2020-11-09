# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
side_a = int(input("Input Side A: "))
side_b = int(input("Input Side B: "))
side_c = int(input("Input Side C: "))

if (side_a == side_b and side_a == side_c):
    print("The triangle with sides " + str(side_a) + " " + str(side_b) + " " + str(side_c) + " is an equalateral triangle because all three sides are equal in length.")
elif (side_a != side_b and side_a != side_c and side_b != side_c):
    print("The triangle with sides " + str(side_a) + " " + str(side_b) + " " + str(side_c) + " is an scalene triangle because all three sides are unequal in length.")
else: 
    print("The triangle with sides " + str(side_a) + " " + str(side_b) + " " + str(side_c) + "is an isosceles triangle because all two sides are the same in length.")
    