import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    with open(filename) as fh:
        rows = csv.reader(fh, delimiter=delimiter)

        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        for row in rows:
            if not row:
                continue

            if select:
                row = [row[index] for index in indices]

            if types:
                row = [typefunc(val) for typefunc, val in zip(types, row)]

            if has_headers:
                data = dict(zip(headers, row))
            else:
                data = tuple(row)
            records.append(data)

    return records


