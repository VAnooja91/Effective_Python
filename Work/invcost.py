import csv
with open("Data/inventory.csv") as fh:
    rows = csv.reader(fh)
    header = next(rows)
    total = 0.0
    for row in rows:
            name = str(row[0])
            quant = int(row[1])
            price = float(row[2])
            total += quant * price
    print("Total cost is: ", total)