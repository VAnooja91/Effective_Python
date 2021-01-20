import csv
import sys
from report import read_inventory


def inventory_cost(filename):
    total = 0
    inventory = read_inventory(filename)
    for prod in inventory:
        quant = prod['quant']
        price = prod['price']
        total += quant * price

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]

else:
    filename = "Data/inventory.csv"

cost = inventory_cost(filename)
print("Total cost is :", cost)

