from follow import follow
import csv
from report import read_inventory
from tableformat  import create_formatter


def conver_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dict(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def filter_names(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def parse_product_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])

    # rows = ([row[index] for index in [0, 1, 4]] for row in rows)

    # rows = (dict(zip(['name', 'price', 'change'], row)
    #              for row in rows)

    rows = conver_types(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])

    return rows


def ticker(filename, logfilename, fmt):
    inventory = read_inventory(filename)
    rows = parse_product_data(follow(logfilename))
    # rows = filter_names(rows, inventory)
    rows = (row for row in rows if row['name'] in inventory)
    formatter = create_formatter(fmt)
    formatter.headings(['Name', 'prices', 'Change'])
    for row in rows:
        name = row['name']
        price = row['price']
        change = row['change']
        rowdata = [name, f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


if __name__ == '__main__':

    lines = follow("Data/marketlog.csv")
    rows = parse_product_data(lines)
    for row in rows:
        print(row)