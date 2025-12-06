masala_spices = ("Cardamom","Clove","Cinnamon")
(spice1, spice2, spice3)=masala_spices 

print(f"{spice1},{spice2},{spice3}")


Ginger_ratio,Cardamom_ratio = 1,2
print(f"The ratio of Ginger is: {Ginger_ratio} and Cardamom is {Cardamom_ratio}")


Ginger_ratio,Cardamom_ratio=Cardamom_ratio,Ginger_ratio
print(f"The ratio of Ginger is: {Ginger_ratio} and Cardamom is {Cardamom_ratio}")

#membership

print(f"is Ginger in masala_spices :{"Ginger" in masala_spices }")
print(f"is Cinnamon in masala_spices :{"Cinnamon" in masala_spices }")