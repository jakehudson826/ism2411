# Excercise 1: build a list
#
#Python lists are highly flexible dynamic arrays that can store multiple data types, like strings and integers, in a single structure. They automatically resize behind the scenes, completely eliminating the need to manually manage memory allocations when elements change.


#In a managerial accounting project for Stuart Advertising Company, a Python list could have automated the manual compilation of 12 months of expense data. Instead of spending hours copying and pasting figures into Excel for a regression analysis, a dynamic list combined with a loop could instantly filter outliers and format the figures.

print("--- Excercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(len(inventory))  # Output: 5

# Excercise 2: index practice

print("--- Excercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)

# Excercise 3: list slicing

print("--- Excercise 3: List Slicing ---")

print(inventory[:3]) # grabs the first three items
print(inventory[:-2]) # grabs the last two items
print(inventory[::2]) # grabs every second item

# Excercise 4: list methods

print("--- Excercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Excercise 5: tuple comparison

print("--- Excercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates

try:
    coords[0] = 99 # Attempting to change the first coordinate
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident" )


# Excercise 6: List Average Sales

print("--- Excercise 6: List Average Sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best Sale (loop): {best}")
print(f"Worst Sale (loop): {worst}")

# Excercise 7: Accumulator Pattern

print("--- Excercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)    

# Excercise 8: Filter

print("--- Excercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")