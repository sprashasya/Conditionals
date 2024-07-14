# Hotel Room Availability: Check if a hotel room is available based on the date and room type.

from datetime import datetime
hotel_booking=datetime(2024, 7, 12, 15, 30, 45)
rooms = 250
room_occupancy = 200 
empty_room = rooms - room_occupancy

if True:
    if empty_room == 0:
        print("Sorry, there are no rooms available at this time.")
        print("A reservation may be required.")
    elif empty_room < rooms:
        print("Sorry, there are no rooms available at this time.")
        print(f"There are {rooms - room_occupancy} people waiting.")
    else:
        print("Yes, there are rooms available at this time.")
        print("reservation needed.")
