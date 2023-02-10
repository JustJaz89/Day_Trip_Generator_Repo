import random

# Create Destination, Restaurant, Entertainment, and Transportation Lists
destinations = ["Dallas, TX", "Orlando, FL", "Las Vegas, NV", "Las Angeles, CA", "Maui, HI"]
restaurants = ["Benihana", "Red Lobster", "Olive Garden", "Texas de Brazil", "Halo Hawaiian BBQ & Poke Bar"]
entertainment = ["Live Music", "Escape Room", "Indoor Go Karts", "Bowling", "Indoor Climbing"]
transportation = ["Party Bus", "Rental Car", "Limousine", "Walking", "Rideshare"]

def selected_destination():
    dest_rand_result = random.choice(destinations)
    return dest_rand_result

selected_destination = random.randrange(len(destinations))

def selected_restaurant():
    rest_rand_result = random.choice(restaurants)
    return rest_rand_result

selected_restaurant = random.randrange(len(restaurants))

def selected_entertainment():
    enter_rand_result = random.choice(entertainment)
    return enter_rand_result

selected_entertainment = random.randrange(len(entertainment))

def selected_transportation():
    trans_rand_result = random.choice(transportation)
    return trans_rand_result

selected_transportation = random.randrange(len(transportation))

print(f"For your Day Trip we have selected {selected_destination}")
# print(f"For your Day Trip we have selected {destinations[selected_destination]} for your destination,{restaurants(selected_restaurant)} for your restaurant, {entertainment(selected_entertainment)} for your entertainment, and {transportation(selected_transportation)} for your transportation.")
# Easy Way
confirm_choice = input("Please enter Y/N to confirm this destination. ")

# # Or Hard Way
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
#     new_dest_response = input(f"Would you rather visit {get_destination} instead? Y/N ")
#     if new_dest_response == "Y":
#         print("Ok!")
#         get_summary()
#     elif new_dest_response == "N":
#         edit_destination


