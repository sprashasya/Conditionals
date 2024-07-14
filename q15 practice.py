# Insurance Premium: Calculate the insurance premium based on the type of coverage and the insured amount.

insurance=input("Please enter the type of insurance\n")
insurance_premium=input("please enter the type of premium\n")

if insurance=="Health Insurance":
    if insurance_premium=="gold":
        print("we cover the all the medical treatement including treatement cost,operations,medicine cost, and any other thing")
    elif insurance_premium=="silver":
        print("we cover the medicine cost and operation cost")
    else:
        print("we cover only medicine cost")
else:
    print("we don`t offer this type of insurance")