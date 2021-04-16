#Function return types

# def format_name(fname,lname):
#     #Docstring :hover over function name
#     '''
#     Take first and last name and format it into Title case
#     '''
#     if fname =="" or lname=="":
#         return "No inputs provided"
#     newfname=fname.title()
#     newlname=lname.title()
#     return f"My name is {newfname} {newlname}."

# output=format_name("darpan","PEDNEKAR")
# print(output)


# year =int(input("Enter a year : "))
# def is_leap(year):
#     if year %4 ==0 :
#         if year % 400 !=0 and year %100 ==0:
#             return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year,month):
#     month_days_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
#     month_days_notleap=[31,28,31,30,31,30,31,31,30,31,30,31]
#     leap=is_leap(year)
#     if leap:
#         return month_days_leap[month-1]
#     else:
#         return month_days_notleap[month-1]

# year=int(input("Enter a year : "))
# month=int(input("Enter a month : "))
# days=days_in_month(year ,month)
# print(days)

# def calc(operation):
#     if operation =="+":
#         value=first_no+second_no
#         dict1["value"]=value
#         return value
#     elif operation =="-":
#         value=first_no-second_no
#         dict1["value"]=value
#         return value
#     elif operation =="*":
#         value=first_no*second_no
#         dict1["value"]=value
#         return value
#     elif operation =="/":
#         value=first_no/second_no
#         dict1["value"]=value
#         return value
#     else:
#         return "Wrong input"


#CALCULATOR
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    first_no=float(input("What is your first number? "))
    for key in operations:
        print(key)

    continue_calc=True

    while continue_calc:
        operation_sym=input("Pick an operation : ")
        second_no=float(input("What is your next number? "))
        cal_func=operations[operation_sym]
        answer=cal_func(first_no,second_no)
        more_calc=input(f"Type 'y' to continue calculating with {answer} ,else press 'n' to start new calculation and 'exit' to exit")
        if more_calc == 'y':
            first_no=answer
        elif more_calc=='n':
            continue_calc=False
            calculator()
        elif more_calc =='exit':
            continue_calc=False

calculator()




