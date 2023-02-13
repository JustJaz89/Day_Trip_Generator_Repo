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