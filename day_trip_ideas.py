greeting = "Thank you for choosing this Day Trip Generator to plan your upcoming vacation."
print(greeting)

import random

destinations = ["Dallas, TX", "Orlando, FL", "Las Vegas, NV", "Las Angeles, CA", "Maui, HI"]
restaurants = ["Benihana", "Red Lobster", "Olive Garden", "Texas de Brazil", "Halo Hawaiian BBQ & Poke Bar"]
entertainment = ["Live Music", "Escape Room", "Indoor Go Karts", "Bowling", "Indoor Climbing"]
transportation = ["Party Bus", "Rental Car", "Limousine", "Walking", "Rideshare"]

selected_destination = random.choice(destinations)
selected_restaurant = random.choice(restaurants)
selected_entertainment = random.choice(entertainment)
selected_transportation = random.choice(transportation)

day_trip = (f"""For your Day Trip we have randomly selected
a. {selected_destination}
b. {selected_restaurant}
c. {selected_entertainment}
d. {selected_transportation}""")
print(day_trip)

confirm_choice = input("Please enter Y/N to confirm this destination. ")

def new_destination(confirm_choice):
    while confirm_choice != "Y":
        selected_destination = random.choice(destinations)
        confirm_choice = input(f"Would you rather visit {selected_destination} instead? ")
    else:
        print(f"You have selected {selected_destination} as the destination for your trip.")

new_destination(confirm_choice)

def new_restaurant(confirm_choice):
    while confirm_choice != "Y":
        selected_restaurant = random.choice(restaurants)
        confirm_choice = input(f"Would you rather go to {selected_restaurant} instead? ")
    else:
        print(f"You have selected {selected_restaurant} as the restaurant for your trip.")

new_restaurant(confirm_choice)

def new_entertainment(confirm_choice):
    while confirm_choice != "Y":
        selected_entertainment = random.choice(entertainment)
        confirm_choice = input(f"Would you rather enjoy {selected_entertainment} instead? ")
    else:
        print(f"You have selected {selected_entertainment} as the entertainment for your trip. ")

new_entertainment(confirm_choice)

def new_transportation(confirm_choice):
    while confirm_choice != "Y":
        selected_transportation = random.choice(transportation)
        confirm_choice = input(f"Would you rather use {selected_transportation} instead? ")
    else:
        print(f"You have selected {selected_transportation} as the transportation for your trip. ")
        get_review()

new_transportation(confirm_choice)

def get_review():
    print(f""" Let's review your Day Trip:
    Destination: {selected_destination}
    Restaurant: {selected_restaurant}
    Entertainment: {selected_entertainment}
    Transportation: {selected_transportation}""")
    final_answer = input("Are you excited about this trip? Y/N : ")
    if final_answer == "Y":
        print("Congratulations! You are all set to enjoy your trip!")
    elif final_answer == "N":
        new_destination()



# # Hard Mode
# def edit_selection():
#     print("Which option would you like to change? Destination, Restaurant, Entertainment, Transportation")
#     change_response = input("""
#     Please enter one of the following options;
#     a. Destination
#     b. Restaurant
#     c. Entertainment
#     d. Transportation
#     """)
#     if change_response == "a":
#         edit_destination()
#     elif change_response == "b":
#         edit_restaurant()
#     elif change_response == "c":
#         edit_entertainment()
#     elif change_response == "d":
#         edit_transportation()
#     else:
#         get_summary()

# def edit_destination():
#     get_destination = selected_destination()
#     new_dest_response = input(f"Would you rather visit {get_destination} instead? Y/N: ")
#     if new_dest_response == "Y":
#         print("Ok!")
#         get_summary()
#     elif new_dest_response == "N":
#         edit_destination()

# def edit_restaurant():
#     get_restaurant = selected_restaurant()
#     new_rest_response = input(f"Would you rather go to {get_restaurant} instead? Y/N: ")
#     if new_rest_response == "Y":
#         print("Great!")
#         get_summary()
#     elif new_rest_response == "N":
#         edit_restaurant()

# def edit_entertainment():
#     get_entertainment = selected_entertainment()
#     new_enter_response = input(f"Would you rather enjoy {get_entertainment} instead? Y/N: ")
#     if new_enter_response == "Y":
#         print("Awesome!")
#         get_summary()
#     elif new_enter_response == "N":
#         edit_entertainment()

# def edit_transportation():
#     get_transportation = selected_transportation()
#     new_trans_response = input(f"Would you rather use {get_transportation} instead? Y/N: ")
#     if new_trans_response == "Y":
#         print("Amazing!")
#         get_summary()
#     elif new_trans_response == "N":
#         edit_transportation()