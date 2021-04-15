# #DICTIONARY
# programming_dictionary={
#     #key:value
#     "apple":"red",
#     "banana":"yellow",
#     "guava":"green",
# }
# #just like list..just imagine in list key is its index,similar way dictionary is also called

# #Retrieving items from dictionary
# #LIST list1[0]
# # print(programming_dictionary["apple"])

# #Addin items into dictionary
# #LIST list1[2]="orange"
# programming_dictionary["orange"]="orange"
# # print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#Grading Program Exercise
# student_scores={
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }

# student_grades={}
# for key in student_scores:
#     if student_scores[key] >90 and student_scores[key] <=100:
#         student_grades[key]="Outstanding"
#     elif student_scores[key] >80 and student_scores[key] <=90:
#         student_grades[key]="Exceeds Expectation"
#     elif student_scores[key] >70 and student_scores[key] <=80:
#         student_grades[key]="Acceptable"
#     elif student_scores[key] <70:
#         student_grades[key]="Fail"

# print(student_grades)

#NESTING IN DICTIONARY AND LIST
# travel_log={
#     "France":{"cities_visited":["Paris","Lille"]},
#     "India":{"cities_visited":["Mumbai","Pune","Delhi"]},
#     "USA": "Chicago",
# }
# print(travel_log)

# travel_log=[
#     {
#         "country":"France",
#     "cities_visited":["Paris","Lille"],
#     "visits":12
#     },
#     {
#         "country":"India",
#         "cities_visited":["Mumbai","Pune","Delhi"],
#         "visits":8
#         },
#     {
#         "country":"USA",
#         "cities_visited":["Chicago","Texas"],
#         "visits":10
#         },
# ]

# def add_new_country(country_visited,no_of_visits,cities_visited):
#     new_country={}
#     new_country["country"]=country_visited
#     new_country["cities_visited"]=cities_visited
#     new_country["visits"]=no_of_visits
#     travel_log.append(new_country)

# add_new_country("Russia",2,["Moscow","Saint Petersburg"])
# print(travel_log)

#Secret Auction Project
# print("Welcome to the secret auction program")
# players_available=True

# def highest_bidder(bidders_list):
#     highest=0
#     winner=""
#     for key in bidders_list:
#         bid_amount=bidders_list[key]
#         if bid_amount > highest:
#             highest=bid_amount
#             winner=key
#     print(f"The winner is {winner} with a bid of ${highest}.")

# bidders_list={}
# while(players_available):
#     name=input("What is your name? : ")
#     bid=int(input("What is your bid? : "))
#     bidders_list[name]=bid
#     other_players=input("Are there any other bidders ? Type 'yes' or 'no' ")
#     if other_players.lower() == "no":
#         players_available=False

# print(bidders_list)
# highest_bidder(bidders_list)





    


