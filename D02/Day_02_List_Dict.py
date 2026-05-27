# Exercise 1 -  Basic List Comprehension
# 1.	Prints the first and last elements
# 2.	Prints every element doubled, using a list comprehension
# 3.	Prints only the even numbers, using a list comprehension with a filter
# 4.	Sorts the list in descending order and prints it
# 5.	Adds the number 100 to the end, removes 15, then prints the final list
numbers = [4, 8, 15, 16, 23, 42]
def first_and_last(nums):
    print(nums[0], nums[-1])
    
def double(nums):
    print([n * 2 for n in nums])

def find_even(nums):
    print([n for n in nums if n % 2 == 0])

def sort_desc(nums):
    nums.sort(reverse = True)
    print(nums)

def modify_number(nums):
    nums.append(100)
    nums.remove(15)
    print(nums)

# Exercise 2 — Word counter
# Write a function count_words(text) that takes a string and returns a dictionary mapping each word to how many times it appears.
# def count_words(text):
#     # your code here
#     pass
def count_words(text):
    words = text.split()
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    return d
# Then write a second function top_n_words(counts, n) that returns the top n most common words as a list of (word, count) tuples, sorted by count descending.
def top_n_words(d, n):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]

# Exercise 3 — Inventory system
# Build a simple inventory using a dictionary where keys are product names and values are dicts with price and quantity.
# inventory = {}
# Write these functions:
# 	1.	add_product(inventory, name, price, quantity) — adds or updates a product
# 	2.	remove_product(inventory, name) — removes a product if it exists, returns True/False
# 	3.	total_value(inventory) — returns the total value (sum of price × quantity across all products)
# 	4.	low_stock(inventory, threshold) — returns a list of product names with quantity below the threshold
def add_product(inventory, name, price, quantity):
    inventory[name] = {"price": price, "quantity": quantity}

def remove_product(inventory, name):
    if name in inventory:
        del inventory[name]
        return True
    else:
        return False
    
def total_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["price"] * item["quantity"]
    return total

def low_stock(inventory, threshold):
    stock = []
    for name, item in inventory.items(): 
        if item["quantity"] < threshold:
            stock.append(name)
    return stock

def remove_product_price(inventory, price):
    # list out all items to another list
    to_remove = [name for name, item in inventory.items() if item["price"] == 0.50]
    for name in to_remove:
        del inventory[name]

# ===================== Test ========================

# Exercise 1
# first_and_last(numbers)
# double(numbers)
# find_even(numbers)
# sort_desc(numbers)
# modify_number(numbers)

# Exercise 2
# # Test
# text = "the quick brown fox jumps over the lazy dog the fox is quick"
# result = count_words(text)
# print(result)
# # Expected: {'the': 3, 'quick': 2, 'brown': 1, 'fox': 2, ...}
# Test:
# print(top_n_words(result, 3))
# Expected: [('the', 3), ('quick', 2), ('fox', 2)]

# Exercise 3
inv = {}
add_product(inv, "apple", 0.50, 100)
add_product(inv, "bread", 2.50, 5)
add_product(inv, "milk", 3.00, 2)
print(total_value(inv))          # Expected: 68.5
print(low_stock(inv, 10))        # Expected: ['bread', 'milk']
remove_product(inv, "apple")
print(inv)                        # apple should be gone