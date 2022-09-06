# print("Hello, World!")
# print("Hello, Python!")
# print("Hello, I am Aydi!")
#
# print("The itsy bitsy spider climbed up the waterspout.")
# print("Down came the rain and washed the spider out.")
#
# print("The itsy bitsy spider climbed up the waterspout.")
# print()
# print("Down came the rain and washed the spider out.")
#
# print("The itsy bitsy spider\nclimbed up the waterspout.")
# print()
# print("Down came the rain\nand washed the spider out.")
#
# print("The itsy bitsy spider\nclimbed up the waterspout.")
# print()
# print("Down came the rain\nand washed the spider out.")
#
# print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
#
# print("My name is", "Python.")
# print("Monty Python.")
#
# print("My name is", "Python.", end=" ")
# print("Monty Python.")
#
# The default behavior reflects the situation where the end keyword argument is implicitly used in the following way: end="\n".
#
# print("My name is ", end="")
# print("Monty Python.")
#
# # print("My", "name", "is", "Monty", "Python.", sep="-")
# # print("My", "name", "is", "Monty", "Python.", sep="_")
#
# print("My", "name", "is", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")
#
# print("Programming","Essentials","in")
# print("Python")
#
# print("Programming","Essentials","in", end='...', sep='***')
# print("Python")

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# 1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window.
#
# 2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.8 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.
#
# 3. To call a function (this process is known as function invocation or function call), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.
#
# 4. Python strings are delimited with quotes, e.g., "I am a string" (double quotes), or 'I am a string, too' (single quotes).
#
# 5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.
#
# 6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.
#
# 7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.
#
# 8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.
#
# 9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.
#
#
# print("2")
# print(2)
#
# integers, that is, those which are devoid of the fractional part;
# and floating-point numbers (or simply floats), that contain (or are able to contain) the fractional part.
#
# print(0o123) # octal
# print(0x123) # hex
#
# Take, for example, the speed of light, expressed in meters per second. Written directly it would look like this: 300000000.
#
# To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.
#
# It reads: three times ten to the power of eight.
#
# In Python, the same effect is achieved in a slightly different way - take a look:
#
# 3E8
#
#
# A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.
#
# If you would like to use it in a program, you should write it this way:
# print("I like \"Monty Python\"")
# 6.62607E-34
# print(0.0000000000000000000001)
#
# print('I\'m Monty Python.')
#
# # or
#
# print("I'm Monty Python.")
#
# print(True > False)
# print(True < False)
# print('"I\'m"\n""learning""\n"""Python"""')
#
# 1. Literals are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").
#
# 2. The binary system is a system of numbers that employs 2 as the base. Therefore, a binary number is made up of 0s and 1s only, e.g., 1010 is 10 in decimal.
#
# Octal and hexadecimal numeration systems, similarly, employ 8 and 16 as their bases respectively. The hexadecimal system uses the decimal numbers and six extra letters.
# 3. Integers (or simply ints) are one of the numerical types supported by Python. They are numbers written without a fractional component, e.g., 256, or -1 (negative integers).
#
# 4. Floating-point numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers that contain (or are able to contain) a fractional component, e.g., 1.27.
#
# 5. To encode an apostrophe or a quote inside a string you can either use the escape character, e.g., 'I\'m happy.', or open and close the string using an opposite set of symbols to the ones you wish to encode, e.g., "I'm happy." to encode an apostrophe, and 'He said "Python", not "typhoon"' to encode a (double) quote.
#
# 6. Boolean values are the two constant objects True and False used to represent truth values (in numeric contexts 1 is True, while 0 is False.
#
#
#
# print(2+2)
# print(2-2)
# print(2==2)
#
# print(2 ** 3)
# print(2 ** 3.)
# print(2. ** 3)
# print(2. ** 3.)
#
# print(2 * 3)
# print(2 * 3.)
# print(2. * 3)
# print(2. * 3.)
#
# print(6 / 3)
# print(6 / 3.)
# print(6. / 3)
# print(6. / 3.)
#
# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 3.)
#
# print(6 // 4)
# print(6. // 4)
#
# print(-6 // 4)
# print(6. // -4)
#
# print(14 % 4)
# print(14 % 3)
# print(14 % 2)
#
# print(12 % 4.5)
#
# print(-4 + 4)
# print(-4. + 8)
#
# print(-4 - 4)
# print(4. - 8)
# print(-1.1)
#
# print(+2)
# print(9 % 6 % 2)
#
# print(2 ** 2 ** 3)
#
#
# [1 +, - unary 2 **(right sided) 3 *, /, //, % 4 +, - binary 5 <, <=, >, >= 6 ==, !=](https://www.mindmeister.com/map/2406561771)
#
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# print(2 * 3 % 5)
#
# print((2 ** 4), (2 * 4.), (2 * 4))
#
# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
#
# print((2 % -4), (2 % 4), (2 ** 3 ** 2))
#
# Key takeaways
# 1. An expression is a combination of values (or variables, operators, calls to functions ‒ you will learn about them soon) which evaluates to a certain value, e.g., 1 + 2.
#
# 2. Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the * operator multiplies two values: x * y.
#
# 3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division ‒ always returns a float), % (modulus ‒ divides left operand by right operand and returns the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation ‒ left operand raised to the power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division ‒ returns a number resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)
#
# 4. A unary operator is an operator with only one operand, e.g., -1, or +3.
#
# 5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.
#
# 6. Some operators act before others – the hierarchy of priorities:
#
# the ** operator (exponentiation) has the highest priority;
# then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example: 4 ** -1 equals 0.25)
# then *, /, //, and %;
# and, finally, the lowest priority: the binary + and -.
# 7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.
#
# 8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.
#
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#
# If you want to give a name to a variable, you must follow some strict rules:
#
# the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
# the name of the variable must begin with a letter;
# the underscore character is a letter;
# upper- and lower-case letters are treated as different (a little differently than in the real world - Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
# the name of the variable must not be any of Python's reserved words (the keywords - we'll explain more about this soon).
#
# https://peps.python.org/pep-0008/
#
# var = 1
# print(var)
#
# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'
# print(var, account_balance, client_name)
# print(var)
#
# var = "3.8.5"
# print("Python version: " + var)
# var = 1
# # print(Var)
#
# var = 1
# print(var)
# var = var + 1
# print(var)
#
# var = 100
# var = 200 + 300
# print(var)
#
#
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c)
#
# john=3
# mary=5
# adam=6
# total_apples=john+mary+adam
# print('Total number of apples:', total_apples)
#
# variable = variable op expression
# x=10
# y=x+1
# x+=1
#
# print(y==x)
#
# kilometers = 12.25
# miles = 7.38
#
# miles_to_kilometers = miles*1.61
# kilometers_to_miles = kilometers/1.61
#
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 1 euro==1 usd so nok

# euro = 12.25
# nok = 73.8
#
# euro_to_nok = euro*9
# nok_to_euro = nok/9
#
# print(euro, "euro is", round(euro_to_nok, 1), "nok")
# print(nok, "nok is", round(nok_to_euro, 1), "euro")


# x = 0 # hardcode your test data here
# x = float(x)
# # write your code here
# y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", y)
#
# x = 1 # hardcode your test data here
# x = float(x)
# # write your code here
# y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", y)
#
# x = -1 # hardcode your test data here
# x = float(x)
# # write your code here
# y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", y)
#
# var = 2
# print(var)
#
# var = 3
# print(var)
#
# var += 1
# print(var)
#
# var = "007"
# print("Agent " + var)
#
# var = 2
# var = 3
# print(var)
#
# a = '1'
# b = "1"
# print(a + b)
#
# a = 6
# b = 3
# a /= 2 * b
# print(a)
# # This program evaluates the hypotenuse c.
# # a and b are the lengths of the legs.
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
# print("c =", c)
#
# # This is a test program.
# x = 1
# y = 2
# # y = y + x
# print(x + y)

# This program prints
# # an introduction to the screen.
# print("Hello!")  # Invoking the print() function
# # print("I'm Python.")
#
# # print("String #1")
# print("String #2")
#
# # This is
# a multiline
# comment. #
#
# print("Hello!")
#
# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")
#
# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")
#
# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)
#
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)
#
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
#
# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")
#
# string * number
# number * string
#
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# print('ba'+5*'na')

#
# A function capable of doing that is called str():
#
# str(number)
# int(number)
# float(number)
#
#
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
#
#
#
# # input a float value for variable a here
# print('please write value of a')
# a = int(input())
# # input a float value for variable b here
# print('please write value of b')
# b = int(input())
# # output the result of addition here
# print(a+b)
# # output the result of subtraction here
# print(a-b)
# # output the result of multiplication here
# print(a*b)
# # output the result of division here
# print(a/b)
# print("\nThat's all, folks!")
#
# x = float(input("Enter value for x: "))
#
# # Write your code here.
# y = 1 / (x + 1 / (x + 1 / (x + 1/x)))
# print("y =", y)
#
#
#
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# # Write your code here.
# mins = (mins+dura)
# hour = hour+mins//60
# mins = mins%60
# hour = hour%24
#
# print(hour,mins,sep=':')
#
#
#
# name = input("Enter your name: ")
# print("Hello, " + name + ". Nice to meet you!")
#
# name = input("Enter your name: ")
# print("Hello, " + name + ". Nice to meet you!")
#
# print("\nPress Enter to end the program.")
# input()
# print("THE END.")
#
#
# num_1 = input("Enter the first number: ") # Enter 12
# num_2 = input("Enter the second number: ") # Enter 21
#
# print(num_1 + num_2) # the program returns 1221
#
# my_input = input("Enter something: ") # Example input: hello
# print(my_input * 3) # Expected output: hellohellohello
#
#
# x = int(input("Enter a number: ")) # The user enters 2
# print(x * "5")
#
#
# x = input("Enter a number: ") # The user enters 2
# print(type(x))
#
