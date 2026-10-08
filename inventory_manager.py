# ==============================================================
# Warehouse Inventory Management Tool
# Constraints: no custom functions, no classes, no imports,
#              no file reads/writes.
# ==============================================================

# ---------------- TASK 1: Data setup ----------------
inventory = {
    "Laptop": 12,
    "Keyboard": 8,
    "Monitor": 5,
    "Mouse": 0,
    "Router": 15,
}

# Order queue: list of tuples -> (item_name, requested_quantity)
order_queue = [
    ("Laptop", 4),
    ("Mouse", 2),
    ("Monitor", 7),
    ("Webcam", 3),      # item not in inventory
    ("Keyboard", 8),
    ("Router", 10),
    ("Laptop", 10),     # only 8 left after the first order
    ("Router", 5),
]

# ---------------- Tracking variables ----------------
fully_fulfilled_count = 0
unfulfilled_items = []   # list of (item, quantity_short, reason)

print("=" * 60)
print("        WAREHOUSE ORDER PROCESSING LOG")
print("=" * 60)
print("Starting inventory:", inventory)
print("-" * 60)

# ---------------- TASK 2: Process orders ----------------
order_number = 1
index = 0

while index < len(order_queue):
    item, requested = order_queue[index]
    stock = inventory.get(item)          # None if key does not exist

    if stock is None:
        # Invalid / missing item
        print(f"Order #{order_number}: [MISSING]  '{item}' is not in the "
              f"catalogue. Requested {requested}, supplied 0.")
        unfulfilled_items.append((item, requested, "Invalid item"))

    elif stock == 0:
        # Out of stock
        print(f"Order #{order_number}: [OUT OF STOCK]  '{item}' has 0 units. "
              f"Requested {requested}, supplied 0.")
        unfulfilled_items.append((item, requested, "Out of stock"))

    elif stock >= requested:
        # Full fulfillment
        inventory[item] = stock - requested
        fully_fulfilled_count += 1
        print(f"Order #{order_number}: [SUCCESS]  {requested} x '{item}' "
              f"shipped. Remaining stock: {inventory[item]}")

    else:
        # Partial fulfillment (0 < stock < requested)
        shortfall = requested - stock
        inventory[item] = 0
        print(f"Order #{order_number}: [PARTIAL]  '{item}' - shipped {stock} "
              f"of {requested}. Shortfall: {shortfall}")
        unfulfilled_items.append((item, shortfall, "Partial fulfillment"))

    order_number += 1
    index += 1

# ---------------- TASK 3: Summary report ----------------
print("\n" + "=" * 60)
print("               END-OF-BATCH SUMMARY")
print("=" * 60)

print("\n1. Final inventory:")
print("  ", inventory)

print("\n2. Total fully fulfilled orders:", fully_fulfilled_count,
      "out of", len(order_queue))

print("\n3. Items that could not be fully supplied:")
if len(unfulfilled_items) == 0:
    print("   None - every order was fulfilled in full.")
else:
    for entry in unfulfilled_items:
        name, qty, reason = entry
        print(f"   - {name}: {qty} unit(s) short  ({reason})")

print("\nTotal units short across all orders:",
      sum(q for _, q, _ in unfulfilled_items))
print("=" * 60)
