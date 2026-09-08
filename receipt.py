
print("="*50)

print("STORE RECEIPT")

print("="*50)
#Above is header for the receipt

item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"
subtotal1 = float(item1_price) * int(item1_qty)

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"
subtotal2 = float(item2_price) * int(item2_qty)

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"
subtotal3 = float(item3_price) * int(item3_qty)
tax_rate = "0.075"
grandsubtotal = subtotal1 + subtotal2 + subtotal3
TOTAL = grandsubtotal + (grandsubtotal * float(tax_rate))
print(f"{item1_name}        ${item1_price} * {item1_qty}        ${subtotal1:.2f}")
print(f"{item2_name}        ${item2_price} * {item2_qty}        ${subtotal2:.2f}")
print(f"{item3_name}        ${item3_price} * {item3_qty}       ${subtotal3:.2f}")

print("-"*50)
#This will be the "Grandsubtotal" which is the total of all the 3 items before tax is applied
print(f"Subtotal:                           ${grandsubtotal:.2f}")
#This is going to be the tax rate for the receipt, it is set to 7.5% in this case
print(f"Tax ({float(tax_rate)*100}%):                     ${grandsubtotal * float(tax_rate):.2f}")

print("="*50)

print(f"TOTAL:                              ${TOTAL:.2f}")

print("="*50)