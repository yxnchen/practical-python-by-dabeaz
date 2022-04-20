# This class does nothing, but it serves as a kind of design specification for additional classes that will be defined shortly. 
# A class like this is sometimes called an “abstract base class.”
class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()
    

# The TableFormatter class you defined in part (a) is meant to be extended via inheritance. 
# In fact, that’s the whole idea. To illustrate, define a class TextTableFormatter like this:
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))
        
class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')


class FormatError(Exception):
    pass

        
def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % fmt)
    

def print_table(data, headers, formatter):
    formatter.headings(headers)
    for d in data:
        rowdata = [str(getattr(d, h)) for h in headers]
        formatter.row(rowdata)
