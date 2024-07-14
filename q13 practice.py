# Tax Calculation: Calculate the tax to be paid based on income brackets and tax rates.

income=int(input("Please enter the income per annum \n"))

if income < 250000:
    tax="you don`t want to give tax"

elif 250000 <= income <500000:
    print("you have to pay 5% of income")
    tax_pay=(income-250000)*0.05
    tax=("you have to pay",tax_pay)

elif 500000 <= income <1000000:
    print("you have to pay 20% of income")
    tax_pay=(12500)+(income-500000)*0.2
    tax=("you have to pay",tax_pay)
else:
    print("you have to pay 30% of income")
    tax_pay=(112500)+(income-1000000)*0.3
    tax=("you have to pay",tax_pay)

print(tax)