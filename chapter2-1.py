firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
num_marbles = input("Enter number of marbles you wish to purchase: ")
num_marbles = int(num_marbles)
cost = 1.2
total = num_marbles * cost

print()
print()
print("Order prepared for Chad Collard")
print()
print(f"{num_marbles} marbles ordered @ ${cost:.2f}")
print()
print(f"Total cost is ${total:.2f}")



