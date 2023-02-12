import random

# Create Destination, Restaurant, Entertainment, and Transportation Lists
destinations = ["Dallas, TX", "Orlando, FL", "Las Vegas, NV", "Las Angeles, CA", "Maui, HI"]
restaurants = ["Benihana", "Red Lobster", "Olive Garden", "Texas de Brazil", "Halo Hawaiian BBQ & Poke Bar"]
entertainment = ["Live Music", "Escape Room", "Indoor Go Karts", "Bowling", "Indoor Climbing"]
transportation = ["Party Bus", "Rental Car", "Limousine", "Walking", "Rideshare"]

def selected_destination():
    dest_rand_result = random.choice(destinations)
    return dest_rand_result
selected_destination = random.choice(destinations)
# print(selected_destination)

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

print(f"""For your Day Trip we have selected
a. {selected_destination}
b. {selected_restaurant}
c. {selected_entertainment}
d. {selected_transportation}
""")
confirm_choice = input("Please enter Y/N to confirm this destination. ")
