import csv
from collections import Counter, defaultdict
import tkinter as tk
from tkinter import ttk, messagebox


def read_csv(filename):
    products = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 3:  # Ensure there are at least three columns (Serial No, Product, Price)
                    product_name = row[1].strip()  # Assuming second column is product name
                    try:
                        price = float(row[2].strip())  # Assuming third column is price
                        products.append((product_name, price))
                    except ValueError:
                        print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        messagebox.showerror("Error", "CSV file not found!")
    return products


def analyze_trends(products):
    product_counts = Counter()
    product_revenue = defaultdict(float)

    for name, price in products:
        product_counts[name] += 1
        product_revenue[name] += price

    sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)
    return [(name, count, product_revenue[name]) for name, count in sorted_products[:5]]


def predict_future_purchases(products):
    product_counts = Counter(name for name, _ in products)
    most_common_product, count = product_counts.most_common(1)[0] if product_counts else ("None", 0)
    return most_common_product, count * 7  # Predicting weekly purchase based on current sales trend


def show_trends():
    filename = 'supermarket_sales.csv'  # Updated file path
    products = read_csv(filename)

    if not products:
        messagebox.showinfo("Info", "No valid data found in the CSV file.")
        return

    trends = analyze_trends(products)
    predicted_product, predicted_quantity = predict_future_purchases(products)
    trend_text.set("\n".join(f"{i + 1}. {product}: {count} times, Total Revenue: ₹{revenue:.2f}"
                             for i, (product, count, revenue) in enumerate(trends)) +
                   f"\n\nPrediction: {predicted_product} is expected to be bought around {predicted_quantity} times next week.")


def add_product():
    name = product_name_var.get().strip()
    price = product_price_var.get().strip()
    if not name or not price:
        messagebox.showerror("Error", "Please enter both product name and price.")
        return

    try:
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Invalid price format.")
        return

    with open('supermarket_sales.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["", name, price])  # Adding empty column for serial number
    messagebox.showinfo("Success", "Product added successfully!")
    product_name_var.set("")
    product_price_var.set("")


# Tkinter UI Setup
root = tk.Tk()
root.title("Supermarket Trends")
root.geometry("400x400")

tk.Label(root, text="Product Name:").pack(pady=5)
product_name_var = tk.StringVar()
tk.Entry(root, textvariable=product_name_var).pack(pady=5)

tk.Label(root, text="Product Price:").pack(pady=5)
product_price_var = tk.StringVar()
tk.Entry(root, textvariable=product_price_var).pack(pady=5)

tk.Button(root, text="Add Product", command=add_product).pack(pady=10)
tk.Button(root, text="Show Trends", command=show_trends).pack(pady=10)

trend_text = tk.StringVar()
tk.Label(root, textvariable=trend_text, justify="left").pack(pady=10)

root.mainloop()