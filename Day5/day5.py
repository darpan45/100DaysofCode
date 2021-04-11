#LOOPS
# fruits =["Apple" ,"Banana","Cherry"]
# for fruit in fruits:
#     print(fruit)

#Average Height Task
# students_height =[180,124,165,173,189,169,146]
# sum=0
# for height in students_height :
#     sum=sum + height
# avg=sum/len(students_height)
# print(avg)

#High Score in class
# students_scores =[98,78,65,89,86,55,91,64,89,96]
# max1=0
# for score in students_scores :
#     if score > max1:
#         max1=score
# print(max1)

#For loop with Range
# for num in range(1,10):
#     print(num)

# for num in range(1,11,3):
#     print(num)

#Calculate sum of all even numbers from 1 to 100
# sum1=0
# for i in range(2,101,2):
#     sum1+=i
# print(sum1)

#FizzBuzz Interview Coding  Question
# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number %5==0:
#         print("Buzz")
#     else:
#         print(number)

#PASSWORD GENERATOR
# import random
# print("Welcome to the PyPassWord Generator")
# no_of_letters=int(input("How many letters would you like in your password ?\n"))
# no_of_symbols=int(input("How many symbols would you like ?\n"))
# no_of_numbers=int(input("How many numbers would you like ?\n"))
# letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# symbols="!@#$%^&*()+"
# numbers="1234567890"
# password=""
# for i in range(no_of_letters):
#     password+=(random.choice(letters))
# for i in range(no_of_symbols):
#     password+=(random.choice(symbols))
# for i in range(no_of_numbers):
#     password+=(random.choice(numbers))
# print('Your Password generated is  : ' +password)

# import random
# print("Welcome to the PyPassWord Generator")
# no_of_letters=int(input("How many letters would you like in your password ?\n"))
# no_of_symbols=int(input("How many symbols would you like ?\n"))
# no_of_numbers=int(input("How many numbers would you like ?\n"))
# letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# symbols="!@#$%^&*()+"
# numbers="1234567890"
# password_list=[]
# for i in range(no_of_letters):
#     password_list+=(random.choice(letters))
# for i in range(no_of_symbols):
#     password_list+=(random.choice(symbols))
# for i in range(no_of_numbers):
#     password_list+=(random.choice(numbers))
# random.shuffle(password_list)

# print('Your Password generated is  : ' +"".join(password_list))

# print("CONGRATULATIONS DAY5 COMPLETE!!!!!!!!!!!")

