# # 1. Write a for loop that will run five times and print “hello!” to the console five times
# for o in range(5):
#     print('hello')

# # 2. Write a for loop that counts from 0 to 10, with each number being print to the console one at a time

# for number in range(11): 
#     print(number)

# # Write a for loop that counts from 10 to 0, with each number being print to the console one at a time. HINT: When calling the range function provide three arguments “range(start number, stop number, step number)”

# for number in range(10, 0 , -1):
#     print(number)


# 4. Write a for loop that will run as many times as a user wants, with each iteration printing “devCodeCamp” to the console. HINT: you will need to use the Python input() function to gather user input

# devCodeCamp = input("""Write “devCodeCamp.: """)
# run_amount = int(input("How many times do you want it to print? "))

# for input in range(run_amount):
#     print(devCodeCamp)

# 5. Write a for loop that will print each character of the string “Packers” to the console.

# str_team = "Packers"

# for char in str_team:
#     print(char)



# # 6. CHALLENGE: Fizz Buzz

# a. Write a program that prints every number from 0 to 100 to the console
# b. If a number is divisible by 3, print ‘fizz’ instead of the number
# c. If a number is divisible by 5, print ‘buzz’ instead of the number
# d. If a number is divisible by 3 and 5, print ‘fizzbuzz’ instead of the number

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number)


# While Loops task ------------------------------------------------------------------------
# 1. Write a while loop that will run five times and print “hello!” to the console five time


# number = 0 
# while (number < 5):
#     print("Hello")
#     number+=1

# 2. Write a while loop that will prompt a user for their password and will continue to prompt the user until the typed in password is correct. If correct, print to the console “User Validated”

# valid_response = False
# while valid_response == False: 
#     password = input("what is your password? ")
#     if password == "Dept":
#         print("welcome")
#         valid_response = True
#     else:
#         print("wrong")

# Write a program that takes a number as input from the user, counts all of the digits in that number, and prints the digit count to the console.

# count = 0
# number = int(input("Enter a number "))

# while (number > 0):
#     number = number // 10 
#     count = count + 1

# print ("Total number of digits : ", count)


