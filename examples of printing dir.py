# Both dictionaries have the same keys
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# Create a list of keys. Could have used groceries = stock.keys()
groceries = ["banana", "orange", "apple"]

# Print the price item associated with a key 'banana'
print(prices["banana"])

for item in prices:
    print(item)   # prints the keys in dict prices

# Calculate the value of the inventory
print("how many items: " + str(len(prices)))

total = 0
for item in prices:
    total += prices[item] * stock[item]  # Both dict have same key
print(total)
