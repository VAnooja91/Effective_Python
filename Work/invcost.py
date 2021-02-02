import csv
from report import read_inventory


def inventory_cost(filename):
    inventory = read_inventory(filename)
    return inventory.total_cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage:{argv[0]} ''inventory')
    inventory = argv[1]
    cost = inventory_cost(inventory)
    print("Total cost:", cost)


if __name__ == "__main__":
    import sys
    main(sys.argv)
