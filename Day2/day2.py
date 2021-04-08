##String
# print("Hello"[0])
# print("Hello"[4])
# print("123"+"456")

# #Integer
# print(123)
# print(123+456)

##Float
# print(12.3+45.6)

##Boolean 
# value1=True
# value2=False

##Type Conversion and Types

# name=len(input("What is your name ?"))
# new_name=str(name)
# print("My name has " + new_name + " characters .")


##Task 1
##Adding the sum of two digit number
# a=input("Enter a two digit number :\n")
# b=int(a[0])+int(a[1])
# print(b)

##Arithmetic Operation
# print(3+1)
# print(4-2)
# print(4*6)
# print(10/2)
# print(10**2)

# #It follow PEMDAS Rule
# ()
# **
# * / #for both these ,the leftmost will take place first
# + - #for both these ,the leftmost will take place first


##BMI Calculator
##BMI =weight/(height*height)

# weight=float(input("Enter your weight in kgs : "))
# height=float(input("Enter your height in m : "))
# bmi=weight/height**2
# print(round(bmi,2))

##F string
# name="Darpan"
# height=1.71
# print(f"my name is {name} and my height is {height}.")

##Tim Urban Life in Weeks
# age=int(input("What is your current age ?"))
# total_days=90*365
# total_weeks=90*52
# total_months=90*12
# days_remaining=total_days-(age*365)
# weeks_remaining=total_weeks-(age*52)
# months_remaining=total_months-(age*12)
# print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months remaining .")

# #Tip Calculator 
print("Welcome to the tip Calculator .")
tot_bill=float(input("What was the total Bill ? $ "))
#print(tot_bill)
perc_tip=int(input("What percentage tip would you like to give ? 10 12 or 15 ? ")) 
#print(perc_tip)
no_of_people=int(input("How many people to split the bill ?"))
#print(no_of_people)
result=round(float((tot_bill + (tot_bill*perc_tip/100))/no_of_people),2)
print(f"Each person should pay : $ {result}")

print("CONGRATULATIONS DAY2 COMPLETE!!!!!!!!!!!")