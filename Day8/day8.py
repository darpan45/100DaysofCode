# Functions
# def greet():
#     print("Hello")
#     print("World")
#     print("Mumbai")

# greet()

# def greet(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}")

# # name is the parameter
# # "Darpan" is the argument

# greet("Darpan")

#POSITIONAL ARGUMENTS
# def greet(name,location):
#     print(f"Hello {name}")
#     print(f"How's you been doing in {location}")
# greet("Darpan","Mumbai")

#KEYWORD ARGUMENTS
# def greet(name,location):
#     print(f"Hello {name}")
#     print(f"How's you been doing in {location}")
# greet(location="Mumbai",name="Darpan")

#PAINT AREA CALCULATOR
# import math
# test_h=int(input("Height of wall : "))
# test_w=int(input("Width of wall : "))
# coverage=5

# def paint_calc(height,width,cover):
#     no_of_cans=math.ceil((height*width)/cover)
#     print(f"You'll need {no_of_cans} cans of paint.")

# paint_calc(height=test_h,width=test_w,cover=coverage)

#PRIME NUMBER CHECKER
# n=int(input("Check this number : "))
# def prime_checker(number):
#     if number==0 or number ==1:
#         print("Neither prime nor composite")
#     else:
#         for i in range(2,number+1):
#             if (number %i==0):
#                 print(f"{number} is not a prime Number")
#                 break
#             else:
#                 print(f"{number} is a prime Number")
#                 break
# prime_checker(number=n)

#CEASAR CIPHER
#ENCRYPTION
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(text,shift):
#     encrypted_text=""
#     for i in text:
#         position=alphabet.index(i)
#         position=(position+shift)%26
#         encrypted_text+=alphabet[position]
#     print(encrypted_text)

# def decrypt(text,shift):
#     decrypted_text=""
#     for i in text:
#         position=alphabet.index(i)
#         position=(position-shift)%26
#         decrypted_text+=alphabet[position]
#     print(decrypted_text)

# if direction == 'encode':
#     encrypt(text,shift)
# elif direction =='decode':
#     decrypt(text,shift)


