products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

max_sold = 0
best_selling = ""

for product, info in products.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        best_selling = product

print(f"1. Самый продаваемый товар: {best_selling} ({max_sold} шт.)")

total_revenue = 0

for product, info in products.items():
    revenue = info["price"] * info["sold"]
    total_revenue += revenue

print(f"2. Общая выручка: {total_revenue} руб.")

max_revenue = 0
best_revenue_product = ""

for product, info in products.items():
    revenue = info["price"] * info["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        best_revenue_product = product

print(f"3. Товар с наибольшей выручкой: {best_revenue_product} ({max_revenue} руб.)")