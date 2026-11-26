amt = float(input("Amount: "))

if amt < 2000:
    disc = amt * 0.05
elif amt <= 5000:
    disc = amt * 0.10
else:
    disc = amt * 0.15

final = amt - disc

print("Amount:", amt)
print("Discount:", disc)
print("Final Amount:", final)