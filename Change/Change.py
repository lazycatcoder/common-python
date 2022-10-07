#number of change coins
while True:
    change = float(input("change owed: "))
    if change > 0 :
        break

# convert the change
change = round(change * 100)

# the number of coins
half = change // 50
dimes = (change % 50) // 25
quaters = ((change % 50) %25) // 10
nickels = (((change%50) % 25) % 10) // 5
pennis = ((((change%50) % 25) % 10) % 5)

coins = half + dimes + quaters + nickels + pennis

print (coins)