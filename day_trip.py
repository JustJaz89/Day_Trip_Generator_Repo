import random

# Create Destination, Restaurant, Entertainment, and Transportation Lists
destinations = ["Dallas, TX", "Orlando, FL", "Las Vegas, NV", "Las Angeles, CA", "Maui, HI"]
restaurants = ["Benihana", "Red Lobster", "Olive Garden", "Texas de Brazil", "Halo Hawaiian BBQ & Poke Bar"]
entertainment = ["Live Music", "Escape Room", "Indoor Go Karts", "Bowling", "Indoor Climbing"]
transportation = ["Party Bus", "Rental Car", "Limousine", "Walking", "Rideshare"]

def selected_destination():
    dest_rand_result = random.choice(destinations)
    return dest_rand_result

def selected_restaurant():
    rest_rand_result = random.choice(restaurants)
    return rest_rand_result

def selected_entertainment():
    enter_rand_result = random.choice(entertainment)
    return enter_rand_result

def selected_transportation():
    trans_rand_result = random.choice(transportation)
    return trans_rand_result





# selected_destination = random.randrange(len(destinations))
# print(f"We have selected {destinations[selected_destination]} for your destination! Are you satisfied with this location?")
# confirm_choice = input("Please enter Y/N to confirm this destination.")