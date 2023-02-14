greeting = "Thank you for choosing this Day Trip Generator to plan your upcoming vacation."
print(greeting)

import random

destinations = ["Dallas, TX", "Orlando, FL", "Las Vegas, NV", "Las Angeles, CA", "Maui, HI"]
restaurants = ["Benihana", "Red Lobster", "Olive Garden", "Texas de Brazil", "Halo Hawaiian BBQ & Poke Bar"]
entertainment = ["Live Music", "Escape Room", "Indoor Go Karts", "Bowling", "Indoor Climbing"]
transportation = ["Party Bus", "Rental Car", "Limousine", "Walking", "Rideshare"]

def selected_destination():
    dest_rand_result = random.choice(destinations)
    return dest_rand_result
selected_destination = random.choice(destinations)

def selected_restaurant():
    rest_rand_result = random.choice(restaurants)
    return rest_rand_result
selected_restaurant = random.choice(restaurants)

def selected_entertainment():
    enter_rand_result = random.choice(entertainment)
    return enter_rand_result
selected_entertainment = random.choice(entertainment)

def selected_transportation():
    trans_rand_result = random.choice(transportation)
    return trans_rand_result
selected_transportation = random.choice(transportation)

day_trip = (f"""For your Day Trip we have randomly selected
    Destination: {selected_destination}
    Restaurant: {selected_restaurant}
    Entertainment: {selected_entertainment}
    Transportation: {selected_transportation}""")
print(day_trip)

confirmed_trip = (f"""Let's review your Day Trip:
    Destination: {selected_destination}
    Restaurant: {selected_restaurant}
    Entertainment: {selected_entertainment}
    Transportation: {selected_transportation}""")

confirm_choice = input("Please enter Y/N to confirm these travel options. ")

# while confirm_choice:
#     if confirm_choice == "Y":
#         print(confirmed_trip)
#     else:
#         print(selected_destination)

def new_destination(confirm_choice):
    if confirm_choice != "Y":
        selected_destination = random.choice(destinations)
        confirm_choice = input(f"Would you rather visit {selected_destination} instead? ")
    else:
        print(f"You have selected {selected_destination} as the destination for your trip.")

new_destination(confirm_choice)

def new_restaurant(confirm_choice):
    if confirm_choice != "Y":
        selected_restaurant = random.choice(restaurants)
        confirm_choice = input(f"Would you rather go to {selected_restaurant} instead? ")
    else:
        print(f"You have selected {selected_restaurant} as the restaurant for your trip.")

new_restaurant(confirm_choice)

def new_entertainment(confirm_choice):
    if confirm_choice != "Y":
        selected_entertainment = random.choice(entertainment)
        confirm_choice = input(f"Would you rather enjoy {selected_entertainment} instead? ")
    else:
        print(f"You have selected {selected_entertainment} as the entertainment for your trip. ")

new_entertainment(confirm_choice)

def new_transportation(confirm_choice):
    if confirm_choice != "Y":
        selected_transportation = random.choice(transportation)
        confirm_choice = input(f"Would you rather use {selected_transportation} instead? ")
    else:
        print(f"You have selected {selected_transportation} as the transportation for your trip. ")

new_transportation(confirm_choice)

print(confirmed_trip)

final_answer = input("Are you excited about this trip? Y/N : ")
if final_answer == "Y":
    print("Congratulations! You are all set to enjoy your trip!")
elif final_answer == "N":
    new_destination(confirm_choice)
    new_restaurant(confirm_choice)
    new_entertainment(confirm_choice)
    new_transportation(confirm_choice)

# final_answer = input("Are you excited about this trip? Y/N : ")
# if final_answer != "N":
#     print("Congratulations! You are all set to enjoy your trip!")
# else:
#     print("Sorry we couldn't help to plan your upcoming trip.")

# def confirmed_trip():
#     print(f""" Let's review your Day Trip:
# Destination: {new_destination}
# Restaurant: {new_restaurant}
# Entertainment: {new_entertainment}
# Transportation: {new_transportation}""")

# confirmed_trip()