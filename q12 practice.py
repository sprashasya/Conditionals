# Library Membership: Determine the membership fee for a library based on the member's age and membership type (individual, family, senior).

age=int(input("Please enter the age of use \n"))
membership_type=input("Please enter the membership type \n")

if age<18:
    if membership_type=="individual":
        print("you have to pay 3000 per month")
    else:
        print("you are not eligible for the family and senior membership")
elif 18<=age<=59:
    if membership_type=="individual":
        print("you have to pay 3000 per month")
    elif membership_type=="family":
        print("you have to pay 2000 per month")
    else:
        print("you are not eligible for the senior membership")
elif age >= 60:
    if membership_type == "individual" or membership_type == "senior":
        print("You have to pay 1500 per month.")
    else:
        print("Senior membership is only available for individual or senior members.")
else:
    print("Invalid age or membership type entered.")
    
    