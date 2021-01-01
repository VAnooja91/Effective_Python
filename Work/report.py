import csv


def read_inventory(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        header = next(rows)
        inventory = list()
        
        for row in rows:
            name = str(row[0])
            quant = int(row[1])
            price = float(row[2])
            product = (name, quant, price)
            inventory.append(product)

    return inventory
