amt = float(input("Amount: "))

if amt < 2000:
    disc = amt * 0.05
elif amt <= 5000:
    disc = amt * 0.10
else:
    disc = amt * 0.15

after_disc = amt - disc
gst = after_disc * 0.05
final = after_disc + gst

print("Amount:", amt)
print("Discount:", disc)
print("GST (5%):", gst)
print("Final Amount:", final)