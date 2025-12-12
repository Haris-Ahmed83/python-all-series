#mutable and immuteable

spice_max = set()
print(f"initial spice_max id:  {id(spice_max)}")
spice_max.add("pizza")
spice_max.add("tea")

print(f"after add item spice_max id:  {id(spice_max)}")