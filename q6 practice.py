# Bank Loan Eligibility: Determine if a person is eligible for a bank loan based on their credit score and income.

Credit_score = 650
income=int(input("Please provide us user income per month \n"))

if Credit_score >=650 and income>=15000:
    print("You are eligible for the loan")
else:
    print("You are not eligible for the loan")
