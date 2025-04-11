# write a program to take a positive number as input from user. 
# if the user enters negative number then keep promting him to enter positive number
#  until he enters the positive number and then print the same

# i = int(input("Enter a positive number: "))
# while i < 0:
#     i = int(input("Please enter a positive number: "))
# print(f"You entered: {i}")
# # write a program to take a positive number as input from user.

#1/4------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to check if a number entered by the user is divisible by both 3 and 5. If it is, print "Divisible by 3 and 5".
# If it is divisible by only 3 or only 5, print "Divisible by 3" or "Divisible by 5" respectively.
# Keep prompting the user for a number until they enter a valid positive number.

# def divisible_by_3_and_5():
#     while True:
#         try:
#             x = int(input("enter a + number: "))
#             if x <= 0:
#                 print("Please enter a positive number.")
#                 continue
            
#             if x % 3 == 0 and x % 5 == 0:
#                 print("didvisible by 3 and 5")
#             elif x % 5 == 0:
#                 print("divisible by 5")
#             elif x % 3 == 0:
#                 print("divisible by 3")
#             else:
#                 print("not divisible by 3 and 5")
#             break
#         except ValueError:
#             print("Enter a postive number")
#             
# divisible_by_3_and_5()



# Write a program that prompts the user to input a positive integer. Then, the program should print the sum of all the digits in that number. 
# For example, for the number 123, the program should output 1 + 2 + 3 = 6. 
# If the user enters a negative number, the program should keep asking for a positive integer.

# while True:
#     try:
#         num = int(input("Enter a positive number: "))
#         if num <= 0:
#             print("Please enter a valid positive number.")
#             continue

#         # Sum of digits without using loop or map()
#         digit_sum = 0
#         temp = num
#         while temp > 0:
#             digit_sum += temp % 10  # Get the last digit
#             temp //= 10  # Remove the last digit
#         print("Sum of digits:", digit_sum)
#         break  # Exit loop after valid input
#     except ValueError:
#         print("Invalid input. Please enter a positive integer.")




#Write a program that calculates the factorial of a number entered by the user.
#If the number is negative, the program should print "Factorial is not defined for negative numbers" 
# and keep asking for a non-negative number until the user enters one.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1) # recusrsive case

# num = int(input("enter a number: "))
# while num < 0:
#     num = int(input("enter positive: "))
# print(f"the factorial of num is {factorial(num)}")





#Write a program that prints the Fibonacci sequence up to the nth term, where n is a positive integer entered by the user.
#  If the user enters a non-positive integer, keep asking for a valid input.






#Write a program that asks the user for a number and keeps prompting for the number until the user enters a positive even number. 
# Once a positive even number is entered, print it and exit the loop

# n = int(input("enter number: "))
# while n < 0:
#     n = int(input("enter  positive number: "))
# print(n)


#Write a program to determine whether a number entered by the user is prime or not. 
# The program should prompt the user until they enter a positive integer greater than 1.


# while True:
#     try:
#         n = int(input("a + positive number: "))
#         if n <= 1:
#             print("enter a posotive number")
#             continue
#         is_prime = True
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         if is_prime == True:
#             print(f"{n} is a prime number")
#         else:
#             print(f"{n} is not a prime number")
#         break
#     except ValueError:
#         ("Invalid input. Please enter a positive integer greater than 1.")

            
#Write a program that prints the multiplication table for a number entered by the user (from 1 to 10). 
# If the number is negative, prompt the user to enter a positive number.

while True:
    try:
        n = int(input(" Enter a number: "))
        if n < 0:
            print("enter a positive number")
            continue 
        for i in range(1,11):
            print(f"{i} * {n} = {i * n}")
            m = n*i 
        break
    except ValueError:
        print("negative value try again")

#Write a program that prompts the user to input a string. 
# If the string length is less than 5, print "String is too short" and ask for a new string until the length is 5 or greater.

# while True:
#     s = str(input("enter a string: "))
#     l = len(s)
#     if l < 5:
#         print("too short enter length grater than 5")
#         continue
#     elif l >= 5:
#         print (f"length of string is {l}: \ngreater than or equal to 5")
#     break



