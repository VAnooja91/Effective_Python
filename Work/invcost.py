import csv
import sys


def inventory_cost(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        header = next(rows)

        total = 0.0
        for row in rows:
            name = str(row[0])
            try:
                quant = int(row[1])
                price = float(row[2])
                total += quant * price
            except ValueError:
                print("Bad row", row)

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]

else:
    filename = "Data/inventory.csv"

cost = inventory_cost(filename)
print("Total cost is :", cost)
