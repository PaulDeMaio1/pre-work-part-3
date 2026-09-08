

product_name = "Wireless Mouse"
price_text = "29.99"
quantity_text = "3"
tax_rate_text = "0.08"

price = float(price_text)
quantity = int(quantity_text)
tax_rate = float(tax_rate_text)

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Product: {product_name}")
print(f"Price: ${price} * {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ({tax_rate * 100}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")