# Gym Membership: Check if a person qualifies for a student discount on a gym membership based on their age and student ID.

age=int(input("Please enter the age of the person \n"))
student_response = input("Do you have a valid student ID? (yes/no): \n").strip().lower()
student_id = student_response == 'yes'
gym_fee=3000

if age<17:
    print("Please do not join gym and play outdoor or indoor sports") 
    exit()

if (18<=age<=25 and student_id):
    print("you are student and your details are verified")
    dicount=gym_fee*0.5
    new_gym_fee=gym_fee-dicount
    print("You have to pay",new_gym_fee,"per month")
else:
    print("You have to pay",gym_fee,"per month")

    