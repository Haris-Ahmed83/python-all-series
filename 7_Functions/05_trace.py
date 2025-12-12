def add_vat(price,vat_rate):
    return price *(100+ vat_rate)/100

order = [100,150,200]

for price in order:
    final_amount = add_vat(price,10)
    print(f"Original: {price}, Final with vat: {final_amount}")
    
