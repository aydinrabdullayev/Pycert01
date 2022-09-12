# var == 0
# black_sheep == (2 * white_sheep)
#
# var = 0  # Assigning 0 to var
# print(var == 0)
#
# var = 1  # Assigning 1 to var
# print(var == 0)
#
# var = 0  # Assigning 0 to var
# print(var != 0)
#
# var = 1  # Assigning 1 to var
# print(var != 0)
#
# black_sheep > white_sheep  # Greater than
#
#
# centigrade_outside ≥ 0.0  # Greater than or equal to
#
# current_velocity_mph < 85  # Less than
# current_velocity_mph ≤ 85  # Less than or equal to
#
# Priority	Operator
# 1	+, -	unary
# 2	**
# 3	*, /, //, %
# 4	+, -	binary
# 5	<, <=, >, >=
# 6	==, !=
#
#
# n = int(input())
# print(n >= 100)
#
# if the true_or_not expression represents the truth (i.e., its value is not equal to zero), the indented statement(s) will be executed;
# if the true_or_not expression does not represent the truth (i.e., its value is equal to zero), the indented statement(s) will be omitted (ignored), and the next executed instruction will be the one after the original indentation level.
#
# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()
## Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)
#
#
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)
#
# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
#
# # We check if the second number is larger than current largest_number
# # and update largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
#
# # We check if the third number is larger than current largest_number
# # and update largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
#
# # Print the result
# print("The largest number is:", largest_number)
#
# i suggest
# if number1 > number2 and number1 > number3:
#     largest_number=number1
# else:
#     if number2 > number3: largest_number=number2
#     else: largest_number=number3
#
# print("The largest number is:", largest_number)
#
# # Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.
#
# largest_number = max(number1, number2, number3)
#
# # Print the result.
# print("The largest number is:", largest_number)
# a=-4
# b=6
# c=2E2
# largest_number = max(a,b,c)
#
# print(largest_number)

# best_plant = input("Enter the first number: ")
#
# if best_plant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif best_plant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else: print("Spathiphyllum! Not,",best_plant,"!")
#
# income = float(input("Enter the annual income: "))
#
# if income <= 85528:
#     tax = income * 0.18 - 556.02
# else: tax = 14839.02 + 0.32 * (income - 85528)
#
# if tax <= 0:
#     tax = 0.0
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
#
# year = int(input("Enter a year: "))
#
# if year < 1582:
#     print("Not within the Gregorian calendar period")
#     exit()
#
# if year % 4 != 0:
#     print('Common year')
# elif year % 100: #WFT??
#     print('Leap year')
# elif year % 400: #WFT??
#     print('Common year')
# else: print('Leap year')

# Operator	Description	Example
# ==	returns if operands' values are equal, and False otherwise
# x == y  # False
# x == z  # True
#
# !=	returns True if operands' values are not equal, and False otherwise
# x != y  # True
# x != z  # False
#
# >	True if the left operand's value is greater than the right operand's value, and False otherwise
# x > y  # False
# y > z  # True
#
# <	True if the left operand's value is less than the right operand's value, and False otherwise
# x < y  # True
# y < z  # False
#
# ≥	True if the left operand's value is greater than or equal to the right operand's value, and False otherwise
# x >= y  # False
# x >= z  # True
# y >= z  # True
#
# ≤	True if the left operand's value is less than or equal to the right operand's value, and False otherwise
# x <= y  # True
# x <= z  # True
# y <= z  # False

# while True:
#     print("I'm stuck inside a loop.")
#
# # Store the current largest number here.
# largest_number = -999999999
#
# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
#
# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
#
# # Print the largest number.
# print("The largest number is:", largest_number)
#
#
# a = 10000000
# while a>0:
#     print(a)
#     a-=1
#

# # A program that reads a sequence of numbers
# # and counts how many numbers are even and how many are odd.
# # The program terminates when zero is entered.
#
# odd_numbers = 0
# even_numbers = 0
#
# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
#
# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))
#
# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)
# vs
# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)
#
# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# number = int(input())
#
# while secret_number != number:
#     print ("Ha ha! You're stuck in my loop!")
#     number = int(input())
# print("Well done, muggle! You are free now.")
#
# for i in range(10):
#     print("The value of i is currently", i)
# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2
#
# import time
#
# for i in range(1, 6):
#     print("Mississippi",i)
#     time.sleep(1.0)
# print("Ready or not, here I come!")
# # break - example
#
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
#
# # continue - example
#
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
# # break - example
#
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
#
# # continue - example
#
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
#
# largest_number = -99999999
# counter = 0
#
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
#
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
#
# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
#
# largest_number = -99999999
# counter = 0
#
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
#
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

exit_word = "chupacabra"
word = input()

while exit_word != word:
    word=input()
print("You've successfully left the loop.")