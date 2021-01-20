import csv

# with open(filename) as fh:
#     rows = csv.reader(fh, delimiter=delimiter)


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):

    if select and not has_headers:
        raise RuntimeError("select arguments requires column names")
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
        for lineno, row in enumerate(rows, start=1):
            if not row:
                continue

            if select:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [typefunc(val) for typefunc, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print("Row {}: couldn't convert {}".format(lineno, row))
                        print("Row {}: Reason {}".format(lineno, e))
                    continue
            if has_headers:
                data = dict(zip(headers, row))
            else:
                data = tuple(row)
            records.append(data)

    return records

