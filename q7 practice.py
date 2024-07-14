# Parking Fee Calculation: Calculate the parking fee based on the hours parked and different rates for short-term and long-term parking.

time=int(input("no. of hours parked"))
one_hour_parking=30
# min_parking_hours=1

if 1<=time<=2:
    print("this is short term parking")
    print(time*one_hour_parking)
else:
    print("comes under long term parking")
    one_hour_parking=20
    print(one_hour_parking*time)