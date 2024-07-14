# Festival Discount: Apply special discounts during a festival period.

Festival=input("Please enter the festival")
 
if Festival=="Diwali":
    discount_percent=40
elif Festival =="Holi":
    discount_percent=30
elif Festival =="New Year":
    discount_percent=30
else:
    print("sorry there is no discount on your purchase")

if discount_percent > 0:
    purchase_amount = float(input("Please enter the total purchase amount: "))
    discount_amount = (discount_percent / 100) * purchase_amount
    discounted_price = purchase_amount - discount_amount
    print(f"You receive a {discount_percent}% discount on your purchase.")
    print(f"After discount, you need to pay: ₹{discounted_price:.2f}")