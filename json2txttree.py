""" A python code to generate a tree or table for JSON data"""
from io import StringIO

__version__ = '1.0.0'

_branch_extend = '│  '
_branch_mid    = '├─ '
_branch_last   = '└─ '
_spacing       = '   '

def _getHierarchy(jsonData, name='', file=None, _prefix='', _last=True):
    """ Recursively parse json data to print data types """
    # Handle object datatype
    if isinstance(jsonData, dict):
        name = name + ' (object)'
        print(_prefix, _branch_last if _last else _branch_mid, \
              name, sep="", file=file)
        _prefix += _spacing if _last else _branch_extend
        length = len(jsonData)
        for i, key in enumerate(jsonData.keys()):
            _last = i == (length - 1)
            _getHierarchy(jsonData[key], '"' + key + '"', file, _prefix, _last)
    # Handle array datatype
    elif isinstance(jsonData, list):
        name += ' (array)'
        print(_prefix, _branch_last if _last else _branch_mid, \
              name, sep="", file=file)
        _prefix += _spacing if _last else _branch_extend
        _getHierarchy(jsonData[0], '', file, _prefix, _last=True)
    else:
        # Handle string datatype
        if isinstance(jsonData, str):
            name = name + ' (string)'
        # Handle number datatype
        else:
            name = name + ' (number)'
        print(_prefix, _branch_last if _last else _branch_mid, \
              name, sep="", file=file)

def json2txttree(jsonData, file=None):
    """ Output JSON data as tree to file or return as string """
    if file == None:
        messageFile = StringIO()
        _getHierarchy(jsonData, file=messageFile)
        message = messageFile.getvalue()
        messageFile.close()
        return message
    else:
        _getHierarchy(jsonData, file=file)

def json2txttable(jsonData, header=None, file=None):
    """ Output JSON data as a Markkdown table to file or return as string """
    # Get tree structure
    treeFile = StringIO()
    _getHierarchy(jsonData, file=treeFile)
    tree = treeFile.getvalue()
    treeFile.close()
    # Convert to table
    table = ''
    for line in tree.splitlines():
        items = line.split('"')
        if len(items) > 1:
            field = '`' + items[1] + '`'
            datatype = items[2].replace('(','`')
            datatype = datatype.replace(')','`')
            table += '| ' + field + ' | ' + datatype + ' | - |\n'
    # Add headers
    if header == None:
        header = '| Field | Data type | Details |\n' + \
                 '| ----- | --------- | ------- |\n'
    table = header + table
    if file == None:
        return table
    else:
        print(table, file=file)


def setSymbols(branch_extend='│  ', branch_mid='├─ ', branch_last='└─ '):
    """ Override symbols for the tree structure """
    global _branch_extend
    global _branch_mid
    global _branch_last
    _branch_extend = branch_extend
    _branch_mid    = branch_mid
    _branch_last   = branch_last
