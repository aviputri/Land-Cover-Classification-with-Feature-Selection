#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Note:
    In numpy, every "append" action requires re-allocation of the array memory 
    and short-term doubling of memory requirements. So, the more general 
    solution is to allocate arrays to be as large as the final output of your 
    algorithm.
"""
import os
import platform
from xlrd import open_workbook
from xlrd import XL_CELL_TEXT, XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_BOOLEAN
import numpy as np


def sheet_to_array(filename, sheet_number, first_col=0, last_col=None, header=True):
    """Return a floating-point numpy array from sheet in an Excel spreadsheet.
    Notes:
    0. The array is empty by default; and any non-numeric data in the sheet will
       be skipped.
    1. If first_col is 0 and last_col is None, then all columns will be used,
    2. If header is True, only one header row is assumed.
    3. All rows are loaded.
    """
    DEBUG = True
    # sheet
    book = open_workbook(filename)
    sheet0 = book.sheet_by_index(sheet_number)
    rows = sheet0.nrows
    # cols
    if not last_col:
        last_col = sheet0.ncols
    if first_col >= last_col:
        raise Exception("First column must be smaller than last column!")
    cols = [col for col in range(first_col, last_col + 1)]
    # rows
    skip = 0
    if header:
        skip = 1
    data = np.empty([len(cols), rows - skip])

    for row in range(skip, sheet0.nrows):
        row_values = sheet0.row(row)
        for col, cell in enumerate(row_values):
            if DEBUG and row < 2:
                print row, col, cell.ctype, cell.value, '\n'
            if col in cols and cell.ctype == XL_CELL_NUMBER:
                data[col - first_col, row - skip] = cell.value
    return data

### TESTS =====================================================================

FILE = 'trainingsample.xls'
SHEET = 0  # the sheet number being processed
# range of cols that must appear in output
FIRST = 2
LAST = 3

userhome = os.path.expanduser('~')
desktop = userhome + '/Desktop/'
filename = '%s%s' % (desktop, FILE)

# whole sheet
data = sheet_to_array(filename, SHEET)
print data

# subset
data = sheet_to_array(filename, SHEET, FIRST, LAST, True)
print data

# faulty inputs
#data = sheet_to_array('foo', SHEET, FIRST, LAST, HEADER)
#print data

#data = sheet_to_array(filename, 999, FIRST, LAST, HEADER)
#print data

#data = sheet_to_array(filename, SHEET, LAST, FIRST, HEADER)
#print data