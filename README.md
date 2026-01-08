# Multi-Source ETL Pipeline

## Description
This project is a **simple yet complete ETL pipeline** that:

- Reads `users.json` and `products.json`
- Reads `orders.csv`
- Cleans and validates data
- Joins orders with users and products
- Calculates `total_amount` for each order
- Outputs **analytics-ready datasets** in CSV and JSON formats

---

## Data Sources

| File | Description |
|------|------------|
| `users.json` | Contains user data (user_id, name, city) |
| `products.json` | Contains product data (product_id, product_name, category, price) |
| `orders.csv` | Contains order data (order_id, user_id, product_id, quantity) |

---

## ETL Process

1. **Extract**
   - Read raw JSON and CSV files

2. **Transform**
   - Clean invalid data (missing user_id, product_id, or quantity)
   - Convert data types (`int`, `float`)
   - Enrich orders by joining with users and products
   - Calculate `total_amount = quantity * price`

3. **Load**
   - Save cleaned and enriched data to:
     - `enriched_orders.csv`
     - `enriched_orders.json`

---

## Output

- **CSV**: `enriched_orders.csv` → enriched orders with user and product info + total_amount  
- **JSON**: `enriched_orders.json` → same data in JSON format  
- **Console**: prints the number of skipped rows and total valid orders

---

## Technology Stack

- Python 3.x  
- CSV and JSON (built-in modules)  
- File Handling  
- Dict / Lookup logic for joining datasets  
- ETL workflow concept

---

## How to Run

1. Clone the repository:

```bash
git clone <repo_url>
cd project_3
