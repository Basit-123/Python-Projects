#Q1:Write a program to Print First 10 natural numbers.
# print("=============The First Ten Natural Number===============")
# for i in range(1,11):
#     print(i)

#Q2:Write a program to Calculate the sum of all numbers from 1 to a given number.

# number = int(input("Enter a Number: "))

# sum = 0
# for i in range(1, number + 1):
#     sum = sum + 1
# print(sum)


#Q3:Write a program to print multiplication table of a given number.

# number = int(input("Enter a Number: "))

# print("Multiplication Table of", number)
# for i in range(1,11):
#     print(number,'X',i,'=',number * i)


#Q4:Write a program to display only those numbers from a list (numbers = [12, 75, 150,
# 180, 145, 525, 50]) that satisfy the following conditions: The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if i % 5 ==0:
#         if i > 150:
#             continue
#         print(i)
       
#     if i > 500:
#         break

#Q5:Write a program to Print list in reverse order using a loop.
# my_list = [1,2,3,4,5,6,7,8,9,10] 
# for i in range(len(my_list)-1,-1,-1):
#     print(i)



#Q6:6. Write a program to display all prime numbers within a range.

# num = int(input("Enter a Number here: "))

# if num == 1:
#     print("It is not a prime Number")

# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("It is not a Prime Number")
#             break

#     else:
#         print("It is a Prime Number")        



#Q7:7. Write a program to Find the factorial of a given number.

# num = int(input("Enter any Number here: "))

# fact = 1

# if num < 0:
#     print("The Factorial Of 0 does not exists: ")

# if num == 0:
#     print("factorial of 0 is", 1)

# if num > 0:
#     for i in range(1,num +1):
#         fact = fact * i

# print("The factorial of the given number is", fact)
         

#Q8:Write a program to find the sum of the series up to n terms.

# number = int(input("Enter the number of terms: "))

# sum_of_series = 0
# for i in range(1, number + 1):
#     sum_of_series += i

# print(f"Sum of the series upto {number} terms is: {sum_of_series}")    

#Q9:Write a Python program to guess a number between 1 and 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt
#appears again until the guess is correct, on successful guess, user will get a "Well
#guessed!" message, and the program will exit.

# import random

# number = random.randint(1, 9)

# guess = None
# while guess != number:
#     guess = input("Guess a number between 1 and 9: ")
    
#     if guess.isdigit():
#         guess = int(guess)
#         if guess == number:
#             print(f"You got it! The number was {number}.")
#         elif guess < number:
#             print("Too low, try again!")
#         else:
#             print("Too high, try again!")
#     else:
#         print("Please enter a valid number between 1 and 9.")


#Q10. Write a Python program that accepts a word from the user and reverses it.

# word = input('Enter a Word: ')
# reversed_word =  word[::-1]
# print("Reversed Word:",reversed_word)

# Q11:Write a Python program that accepts a string and calculates the number of digits and
# letters.

# text = input('Enter a string')

# letters = 0
# digits = 0 


# for i in text:
#     if i.isalpha():
#         letters += 1
#     elif i.isdigit():
#         digits  += 1 

# print('Letters: ',letters)
# print('Digits: ', digits)           



# Q12:Write a program to calculate the length of string provide input by user (without using
# len).

# text = input("Enter a String: ")
# lenght = 0

# for i in text:
#     lenght +=1


# print("Length of the String", lenght)



#Q13:Write a Python program to print the number of vowels and consonant in your full
# name.

# text = input("Enter your full name: ")
# vowels = 0
# consonants = 0
# vowel_set = "aeiouAEIOU"

# for char in text:
#     if char.isalpha():
#         if char in vowel_set:
#             vowels += 1
#         else:
#             consonants += 1

# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)



#Q14:Write a Python program that generates list of values. The values must be taken from
#user as input.


# values = input("Enter values separated by spaces: ").split()
# print("Generated list:", values)


#Q15. Write a Python program to copy elements from one list to another.

# values = input("Enter values separated by spaces: ").split()
# copied_list = values.copy()
# print("Original list:", values)
# print("Copied list:", copied_list)


# Q16:Write a python program to select the maximum value from list (without using
# maximum function).

# values = [3, 5, 7, 2, 8, 1]

# if not values:
#     print("The list is empty.")
# else:
#     max_value = values[0]  
#     for num in values:
#         if num > max_value:
#             max_value = num  

#     print("Maximum value:", max_value)



# Q17:Write a Python program to count the number of even and odd numbers from a series
# of numbers. Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)


# Q18:Find the sum of squares of each element of the list using for loop. numbers = [3, 5, 23,
# 6, 5, 1, 2, 9, 8

# numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]

# sum_of_squares = 0

# for num in numbers:
#     sum_of_squares += num ** 2

# print("Sum of squares:", sum_of_squares)


#Q19From given list: gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28, “Speakers”,
# 27.00, “Television”, 1000, “Laptop Case”, “Camera Lens”]
# a) Create separate lists of strings and numbers.
# b) Sort the strings list in ascending order
# c) Sort the strings list in descending order
# d) Sort the number list from lowest to highest
# e) Sort the number list from highest to lowest


# gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

# strings = []
# numbers = []

# for item in gadgets:
#     if isinstance(item, str):
#         strings.append(item)
#     else:
#         numbers.append(item)


# strings.sort()  
# strings_descending = sorted(strings, reverse=True)  
# numbers.sort()  
# numbers_descending = sorted(numbers, reverse=True) 


# print("Strings in ascending order:", strings)
# print("Strings in descending order:", strings_descending)
# print("Numbers from lowest to highest:", numbers)
# print("Numbers from highest to lowest:", numbers_descending)
