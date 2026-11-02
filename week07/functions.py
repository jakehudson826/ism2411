#Reflection #1 - I noticed the missing colon, where it said ": expected"
#Reflection #2 - It calculates the discount on the item based on the price of the item and the customer's tier.
#AI DISCLOSURE
#TOOL USED: META AI
#PROMPT- SENT PICTURE OF BROKEN CODE "EXPLAIN HOW TO FIX THESE LINES"
#CHANGED I >= TO I >

# Excercise 1 

# defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05)}")

# Excercise 2 

# Defining a function
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.9
    elif tier == "bronze":
        return price * .95
    else:
        return price


# Calling the function with different tiers
orginal_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(orginal_price, tier):.2f}")

# Excercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Excercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Order; ${price} | Tier: {tier} | Total: ${total}")

# Excercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Excercise 6

x = 100 # global x

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)