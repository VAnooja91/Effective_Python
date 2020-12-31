import csv
def inventory_cost(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        header = next(rows)
        total = 0.0
        for row in rows:
            name = str(row[0])
            quant = int(row[1])
            price = float(row[2])
            total += quant * price
    return total
cost = inventory_cost("Data\inventory.csv")
print("Total cost is :", cost)
