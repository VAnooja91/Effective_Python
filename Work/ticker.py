from follow import follow
import csv


def conver_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dict(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def parse_product_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = conver_types(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])
    return rows


if __name__ == '__main__':

    lines = follow("Data/marketlog.csv")
    rows = parse_product_data(lines)
    for row in rows:
        print(row)