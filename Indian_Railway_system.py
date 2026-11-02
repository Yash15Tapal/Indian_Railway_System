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
print("=== Indian Railway Booking System ===")
passenger_name = input("Enter passenger name:")
age = int(input("Enter age:"))
destination = input("Enter destination:")

# Display booking confirmation
print("\n=== Booking Details ===")
print(f"Passenger: {passenger_name}")
print(f"Age: {age}")
print(f"Destination: {destination}")
print("Booking confirmed!")