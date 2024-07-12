# Flight Status: Check if a flight is on time, delayed, or canceled based on its current status.

from datetime import datetime

Flight_on_time=datetime(2024, 7, 12, 15, 30, 45)  
Flight_Delayed=datetime(2024, 7, 12,17, 25, 45)

specific_time = Flight_on_time

if specific_time<Flight_on_time:
    print("Flight is before time")

elif specific_time==Flight_on_time:
    print("Flight is in time")

elif specific_time==Flight_Delayed:
    print("Flight is delayed")
    
else:
    print("Flight is canceled")