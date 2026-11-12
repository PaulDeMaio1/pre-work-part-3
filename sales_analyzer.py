import csv
from collections import defaultdict

# Define the totals before reading the file
total_revenue = 0.0
revenue_by_product = defaultdict(float)
quantity_by_product = defaultdict(int)
revenue_by_date = defaultdict(float)

# Read the sales data
with open("sales_data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        date = row["date"]
        quantity = int(row["quantity"])
        price = float(row["price"])

        line_revenue = quantity * price

        total_revenue += line_revenue
        revenue_by_product[product] += line_revenue
        quantity_by_product[product] += quantity
        revenue_by_date[date] += line_revenue

# Find the highest revenue day
best_day = max(revenue_by_date, key=revenue_by_date.get)
best_day_revenue = revenue_by_date[best_day]

# Formatted text report
with open("sales_report.txt", "w") as f:
    f.write("=" * 40 + "\n")
    f.write("SALES SUMMARY REPORT\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total Revenue: ${total_revenue:,.2f}\n\n")

    f.write("Revenue and Quantity by Product:\n")
    f.write("-" * 40 + "\n")
    f.write(f"{'Product':<12}{'Quantity':>10}{'Revenue':>16}\n")
    for product in sorted(revenue_by_product):
        f.write(
            f"{product:<12}"
            f"{quantity_by_product[product]:>10}"
            f"{'$' + format(revenue_by_product[product], ',.2f'):>16}\n"
        )

    f.write("\n")
    f.write(f"Best Day: {best_day} (${best_day_revenue:,.2f})\n")

# Product summary CSV
with open("product_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "total_quantity", "total_revenue"])
    for product in sorted(revenue_by_product):
        writer.writerow([
            product,
            quantity_by_product[product],
            round(revenue_by_product[product], 2),
        ])

print("Created sales_report.txt and product_summary.csv")