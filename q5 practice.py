# Online Shopping Discount: Apply a discount if the total purchase amount exceeds a certain threshold.

total_purchase=int(input("enter the total purchase :\n"))
Threshold=2500

if total_purchase<Threshold:
    print("There is no discount.You have to pay",total_purchase)
else:
    discount=total_purchase*0.2
    discount_amount=total_purchase-discount
    print("You receive the discount on your purchase. Now you have to pay",discount_amount)
