# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.


y = 0 
x= 1
print("term: 0 value: 0") 
print("term: 1 value: 1") 
for number in range(2,51,1):
    n = x + y
    y = x
    x = n
    print("term: " + str(number) + " value: " + str(n))
# Hint: The next number is found by adding the two numbers before it
