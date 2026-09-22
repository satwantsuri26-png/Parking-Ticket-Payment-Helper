def calculate_change (paid,price):
    change = paid - price
    return change

snack_price = 25
print("======Parking Ticket Payment Helper======")
print(f"This ticket costs {snack_price} units.")
print("Accepted coins: 1,5,10 and 25/n")

total_inserted = 0
coins_inserted = 0

while True: 
    coin = int(input("Insert a coin (1, 5, 10 or 25):"))

    if coin != 1 and coin !=5 and coin != 10 and coin != 25:
        print ("Invalid coin; try again!/n")
        continue

    total_inserted += coin 
    coins_inserted += 1
    print (f"Inserted {coin}. Total so far: {total_inserted}/n")

    if total_inserted >= snack_price:
        print ("Enough money inserted!/n")
        break 

change_due = calculate_change(total_inserted, snack_price)

print ("Dispensing your ticket...")

if change_due == 0:
     pass
else:
     print (f"Here is your change: {change_due} units")

print ("/n===== PURCHASE SUMMARY =======")
print ("Parking price:", snack_price)
print (coins_inserted)