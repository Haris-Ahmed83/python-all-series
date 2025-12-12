ingrendints = ["water","milk","black tea","cardomom","Garlic"]
#Append
ingrendints.append("sugar")
#remove
ingrendints.remove("water")
print(f"Over List: {ingrendints}")

spice_options = ["ginger","cardomam"]
chia_ingredints = ["water","milk","cardamom","Garlic"]
print(f"Chia: {chia_ingredints}")

#sorting
chia_ingredints.sort()
print(f"Sort: {chia_ingredints}")

#pop
last_added = chia_ingredints.pop()
print(f"Pop: {last_added}")

#reverse
second_ingrendints = ["water","milk","black tea","cardomom","Garlic"]
second_ingrendints.reverse()
print(f"reverce: {second_ingrendints}")

#max function
suger_level = [10,20,30,40,50]
print(f"Maximum sugar:{max(suger_level)}")
print(f"Minimum sugar:{min(suger_level)}")
