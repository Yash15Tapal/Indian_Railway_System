# Defifning Variables for Indian Railway System

train_name = "Rajdhani Express"
train_number = 12301
ticket_price = 2450.50
is_ac_available = True
seat_numbers = [1, 2, 3, 4, 5]

# Showing the Details using print Function

# print("Train Name:",train_name)
# print("Train Number:",train_number)
# print("Ticket Price:",ticket_price)
# print("AC Availability:",is_ac_available)
# print("Seat Numbers:",seat_numbers)

# Show the data types of the variables using type Function

# print("The data type of train_name:",type(train_name))
# print("The data type of train_number:",type(train_number))
# print("The data type of ticket_price:",type(ticket_price))
# print("The data type of is_ac_available:",type(is_ac_available))
# print("The data type of seat_numbers:",type(seat_numbers))

# Getting passenger information
# print("=== Indian Railway Booking System ===")
# passenger_name = input("Enter passenger name:")
# age = int(input("Enter age:"))
# destination = input("Enter destination:")

# # Display booking confirmation
# print("\n=== Booking Details ===")
# print(f"Passenger: {passenger_name}")
# print(f"Age: {age}")
# print(f"Destination: {destination}")
# print("Booking confirmed!")

#Arthematic Operators

# base_price = 1500
# service_price = 100
# total_price = base_price + service_price

# print(f"Base Price: ₹{base_price})")
# print(f"Service Charge: ₹{service_price}")
# print(f"Total Price: ₹{total_price}")

# #Comparison operators
# passenger_age = 25
# senior_citizen_age = 60
# is_senior = passenger_age >= senior_citizen_age

# print(f"\nIs passenger senior citizen? {is_senior}")

# Logical operators

# has_ticket = True
# has_id_proof = True
# can_board = has_ticket and has_id_proof

# print(f"can Board Train? {can_board}")

#Control Flow - If Statements

#Age based pricings

# Age = int(input("Enter passenger age: "))

# if Age < 5:
#     price = 0
#     category = "Infant (Free)"
# elif Age < 12:
#     price = 750
#     category = "Child (50% Discount)"
# else:
#     price = 1500
#     category = "Adult"

# print(f"Category: {category}")
# print(f"Ticket Price: ₹{price}")

# For Loop - Display available trains

# train = [
#     {"name": "Rajdhani Express",
#      "number":12301,
#      "destination":"New Delhi"},
#      {"name": "Shatabi Express",
#         "number":12001,
#         "destination":"Chennai"},
#     {"name": "Duronto Express",
#         "number":12291,
#         "destination":"Mumbai"}
# ]

# print("Available Trains:")
# for train in train:
#     print(f"{train['number']} - {train['name']} to {train['destination']}")

# While Loop - Booking System Menu

# print("\n=== Booking Menu ===")
# choice = 0

# while choice != 3:
#     print("1. Book Ticket")
#     print("2. Check Status")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Booking ticket ......")
#     elif choice == 2:
#         print("Checking Status")
#     elif choice == 3:
#         print("Thank you for using Indian Railways!")
#     else:
#         print("Invalid Choice!")

# List

# states = ["Maharashtra", "Kerala", "Punjab", "Tamil Nadu", "Gujarat"]

# print("Original List:", states)

# # Add elements
# states.append("Karnataka")
# states.insert(2, "Rajasthan") # insert at index
# print("After Append & Insert:", states)

# # Extend with another list
# states.extend(["Goa", "Bihar"])
# print("After Extend:", states)

# # Remove elements
# states.remove("Punjab")       # remove specific element
# popped = states.pop()         # remove last element
# print("Removed Element:", popped)
# print("After Remove & Pop:", states) 

# # Sorting & Reversing
# states.sort()
# print("Sorted List:", states)
# states.reverse()
# print("Reversed List:", states)

# # Index & Count
# print("Index of Kerala:", states.index("Kerala"))
# print("Count of kerala:", states.count("Kerala"))

# # Copy & CLear
# copy_states = states.copy()
# print("Copied List:", copy_states)
# states.clear()
# print("Cleared List:", states)

# # TUPLE
# cities = ("Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", "Mumbai")

# print("Tuple:", cities)

# # Count
# print("Count of Mumbai:", cities.count("Mumbai"))

# # Index
# print("Index of Chennai:", cities.index("Chennai"))

# # Length
# print("Length:", len(cities))

# # Membership
# print("Delhi in tuple?", "Delhi" in cities)

# # Min & Max (alphabetical)
# print("Min:", min(cities))
# print("Max:", max(cities))

# Dictionary
# capitals = {
#     "Maharashtra": "Mumbai",
#     "Kerala": "Thiruvanthapuram",
#     "Tamil Nadu": "Chennai",
#     "Gujarat": "Ghandhinagar"
# }

# print("Dictonary:", capitals)

# # Get & Access
# print("Capital of Kerala:", capitals.get("Kerala"))

# # keys, Values, Items
# print("States:", capitals.keys())
# print("Capitals:", capitals.values())
# print("Pairs:", capitals.items())

# # Update & Add
# capitals.update({"Karnataka": "Bengaluru"})
# capitals["Punjab"] = "Chandigarh"
# print("After Update:", capitals)

# # Remove
# capitals.pop("Tamil Nadu")      # remove by key
# capitals.popitem()              # remove last inserted
# print("After Pop & Popitem:", capitals)

# # Copy & Clear
# copy_caps = capitals.copy()
# capitals.clear()
# print("Copied:", copy_caps)
# print("Claeared:", capitals)

# SET
# languages = {"Hindi", "English", "Marathi", "Tamil", "Telugu"}

# print("Original Set:", languages)

# # Add & Remove
# languages.add("Gujarati")
# languages.discard("English")
# print("After Add & Discard:", languages)

# # Remove (error if not present)
# languages.remove("Hindi")

# Set Operations
# south = ("Tamil", "Telugu", "Kannada")
# print("Union:", languages.union(south))
# print("Intyersection:", languages.intersection(south))
# print("Difference:", languages.difference(south))
# print("Symmetric Difference:", languages.symmetric_difference(south))

# # Copy & Clear
# copy_lang = languages.copy()
# languages.clear()
# print("Copied:", copy_lang)

# # STRING
# movie = "Sholay is a Classic Bollywood Movie"

# print("Original:", movie)

# # Case
# print(movie.upper())
# print(movie.lower())
# print(movie.title())
# print(movie.capitalize())
# print(movie.swapcase())

# # Check
# print(movie.startswith("Sholay"))
# print(movie.endswith("Movie"))
# print("Is Alpha?", movie.isalpha()) # spaces break alpha
# print("Is Digit?", movie.isdigit())

# # Find and Replace
# print("Find 'Classic':", movie.find("Classic"))
# print(movie.replace("Classic", "Legendary"))

# # Split & Join
# words = movie.split()
# print("Split:", words)
# joined = "-".join(words)
# print("Joined:", joined)

# # Strip
# line = "   Jai Hind   "
# print("Stripped:", line.strip())
# print("Left Strip:", line.lstrip())
# print("Right Strip:", line.rstrip())

# # Count & Index
# print("Count of 'o':", movie.count("o"))
# print("Index of 'Bollywood':", movie.index("Bollywood"))

# # Length
# print("Length:", len(movie))

# DATE & TIME
import datetime

# Current date & time
now = datetime.datetime.now()
print("Now:", now)

# Today
today = datetime.date.today()
print("Today:", today)

# Specific date (Republic Day)
republic_day = datetime.date(1950, 1, 26)
print("Republic Day:", republic_day.strftime("%D-%B-%Y"))

# Time Difference
diff = today - republic_day 
print("Days since Republic Day:", diff.days)

# Current components
print("Years:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Create a time object
t = datetime.time(10, 30, 15)
print("Custom Time:", t)

# Combine date & time
dt = datetime.datetime.combine(today, t)

# Formatting
print("Formatted:", now.strftime("%A, %D %B %Y, %I:%M %p"))