# Practice 2: Using Dictionary Methods
# Task:
# Create a dictionary for fruit prices:
# Print all keys
# Print all values
# Use get() to find the price of "banana"
# Add "orange" with price 80 using update()
# Remove "apple" using pop()
# Print the final dictionary

fruit_price = {
    "apple": 100,
    "banana" : 150,
    "mango" : 200

}
#keys
print("keys: ",fruit_price.keys())

#value
print("values: ",fruit_price.values())

#get()
print("get the value of banana: ",fruit_price.get("banana"))

#update
fruit_price.update({"orange":80})

#pop
fruit_price.pop("apple")

print("updated_keys: ",fruit_price.keys())

print("final_fruit_price",fruit_price)