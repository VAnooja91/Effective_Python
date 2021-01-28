class TableFormatter:
    def headings(self, headers):
        '''Emit table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit single row of data.
        :param rowdata:
        :return:
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f'{data:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Emit a table in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    else:
        raise FormatError("Unknown format {name}")


def print_table(inventoryobj, columnslist, formatter):
    formatter.headings(columnslist)
    for obj in inventoryobj:
        # data = [str(getattr(obj, column)) for column in columnslist]
        data = []
        for column in columnslist:
            data.append(str(getattr(obj, column)))
        formatter.row(data)
