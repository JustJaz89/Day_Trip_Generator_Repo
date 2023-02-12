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
d. {selected_transportation}
""")
print(day_trip)
confirm_choice = input("Please enter Y/N to confirm this destination. ")