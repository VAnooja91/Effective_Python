import csv
import sys


def inventory_cost(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        header = next(rows)

        total = 0.0
        for lineno, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                quant = int(record['quant'])
                price = float(record['price'])
                total += quant * price
            except ValueError:
                print("Row {0}: couldn't convert {1}".format(lineno, row))

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]

else:
    filename = "Data/inventory.csv"

cost = inventory_cost(filename)
print("Total cost is :", cost)
