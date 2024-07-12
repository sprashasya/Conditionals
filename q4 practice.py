# Restaurant Seating: Determine if there are available seats in a restaurant and if a reservation is needed based on the current time and seating capacity.

from datetime import datetime

seating_capacity = 250
current_occupancy = 200 
empty_seat = seating_capacity - current_occupancy

if empty_seat == 0:
    print("Sorry, there are no seats available at this time.")
    print("A reservation may be required.")
elif empty_seat < seating_capacity:
    print("Sorry, there are no seats available at this time.")
    print(f"There are {seating_capacity - current_occupancy} people waiting.")
else:
    print("Yes, there are seats available at this time.")
    print("No reservation needed.")

