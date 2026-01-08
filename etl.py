import csv
import json


# STEP 1: Load users.json

with open("data/raw/users.json", "r") as f:
    users = json.load(f)

users_lookup = {
    u["user_id"]: {
        "name": u["name"],
        "city": u["city"]
    }
    for u in users
}


# STEP 2: Load products.json


with open("data/raw/products.json", "r") as f:
    products = json.load(f)

products_lookup = {
    p["product_id"]: {
        "product_name": p["product_name"],
        "category": p["category"],
        "price": p["price"]
    }
    for p in products
}


# STEP 3: Read orders.csv

clean_orders = []
skipped_rows = 0

with open("data/raw/orders.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            if not row["user_id"] or not row["product_id"]:
                skipped_rows += 1
                continue

            user_id = int(row["user_id"])
            product_id = int(row["product_id"])
            quantity = int(row["quantity"])

            if user_id not in users_lookup:
                skipped_rows += 1
                continue

            if product_id not in products_lookup:
                skipped_rows += 1
                continue

            clean_orders.append({
                "order_id": row["order_id"],
                "user_id": user_id,
                "product_id": product_id,
                "quantity": quantity
            })

        except:
            skipped_rows += 1
            continue


# STEP 4: Enrich orders


enriched_orders = []

for order in clean_orders:
    user = users_lookup[order["user_id"]]
    product = products_lookup[order["product_id"]]

    total_amount = order["quantity"] * product["price"]

    enriched_orders.append({
        "order_id": order["order_id"],
        "user_id": order["user_id"],
        "user_name": user["name"],
        "city": user["city"],
        "product_id": order["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "price": product["price"],
        "quantity": order["quantity"],
        "total_amount": total_amount
    })


# STEP 5: Load outputs

# Save CSV
with open("processed/enriched_orders.csv", "w", newline="") as f:
    fieldnames = enriched_orders[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(enriched_orders)

# Save JSON
with open("processed/enriched_orders.json", "w") as f:
    json.dump(enriched_orders, f, indent=4)

print("✅ ETL Finished Successfully")
print(f"🧹 Skipped rows: {skipped_rows}")
print(f"📦 Total clean orders: {len(enriched_orders)}")

