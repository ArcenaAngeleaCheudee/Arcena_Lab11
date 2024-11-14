# Input Values
item1 =  input("Enter the amount of your first purchase: ")
item2 = input("Enter the amount of your second purchase: ")
item3 = input("Enter the amount of your third purchase: ")
total_amount = float(item1) + float(item2) + float(item3)

print (f"Total amount: ${total_amount}")

# Discount application
if (total_amount>100):
    discount = total_amount * 0.10
    total_amount -= discount
    print(f"We are pleased to inform you that a 10% discount has been applied to your total, ${discount: .2f} saved.")
else:
    print("No discount applied.")

# Discounted total amount 
print(f"Total amount after discount: ${total_amount: .2f}")

# Loyalty Points
loyalty_points = total_amount / 10 

print(f"{loyalty_points: .2f} loyalty points successfully added to credit.")

# Payent & change 
payment = input("Enter amount for payment: ")
change1 = float(payment) - total_amount

if (float(payment)>=total_amount):
    print(f"CHANGE: ${change1: .2f}")
else:
    print("Payment Declined. Please check your balance and try again.")