essential_spices = {"cardamom","Ginger","Cinnamon"}
optionalc_spices = {"Clove","Ginger","Black pepper"}

all_spices = essential_spices| optionalc_spices
print(f"all spices {all_spices}")

#commom (for common we use &)
commom_spices = essential_spices & optionalc_spices
print(f"Common spices: {commom_spices}")

only_in_essential = essential_spices - optionalc_spices
print(f"only essential spices: {only_in_essential}")

print(f"Is clove in essential spices? {'clove'in essential_spices}")
print(f"Is Ginger in essential spices? {'Ginger'in essential_spices}")
