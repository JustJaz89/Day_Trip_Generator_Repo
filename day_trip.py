import random

# Create Destination, Restaurant, Entertainment, and Transportation Lists
destinations = ["Dallas, TX", "Orlando, FL", "Las Vegas, NV", "Las Angeles, CA", "Maui, HI"]
restaurants = []
entertainment = []
transportation = []

selected_destination = random.randrange(len(destinations))
print(f"We have selected {destinations[selected_destination]} for your destination! Are you satisfied with this location?")
confirm_choice = input("Please enter Y/N to confirm this destination.")
