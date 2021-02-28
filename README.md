# tktabl

This proyect intends to be a complement on managing tables within the Python Tkinter GUI.

## Installation

Run the following to install:

```shell
$ pip install tktabl
```

## Usage

### Import

As tktable is a complement to tkinter, you must import it in your code:

```python
import tkinter as tk
import tktabl
```

### Create a table

Creating a table requires a tkinter root as an argument. This will create a
default 5x4 table in its own tkinter frame.
Note that the first row is a column headers row.

```python
root = tk.Tk()
table = tktable.Table(root)
table.pack()
```

You can specify it size passing 2 additional arguments (col, row), e.g.:

```python
root = tk.Tk()
table = tktable.Table(root, col=3, row=5)
table.pack()
```

This will create a 6x3 table where the first row is a column headers row.

You can pass a list of strings as column headers, e.g.:

```python

headers = ["ID", "Name", "Age"]

root = tk.Tk()
table = tktable.Table(root, headers=headers)
table.pack()
```

This will create a 5x3 table where the first row is the column headers row
with the values "ID", "Name", and "Age" respectively

You can pass a list of dictionaries with the data you want to display, e.g.:

```python

data = [
    {"ID": 1, "Name": "Juan", "Age": 24},
    {"ID": 2, "Address": "5th 20-22"}
]

root = tk.Tk()
table = tktable.Table(root, data=data)
table.pack()
```

Note that not every dictionary has the same keys.
This, will create a 4x3 table.
First row will be a row with headers "ID", "Name", "Age" and "Address".
Second row will be the data of the first dictionary.
Third row will be the data of the second dictionary.
(If the dictionary doesn't has any value in a given header, the corresponding
cell will be left blank)

Finally, you can mix all these arguments, e.g.:

```python
...
table = tktable.Table(root, row=5, headers=headers, data=data)
table.pack()
```

In this case, it will create a table where there will be as many columns
as headers in the headers variable plus the data variable without repeating themselves

After creating the table and before running your app, you must pack it with the Table.pack() function.

### Usefull methods

- Table.get_cell(row, column): will return a Cell object in the corresponding
  row and column.

- Table.get_data(): will return a list of dictionaries, as many as rows are in the table, ignoring
  headers row, and each dictionary will have as many named keys as columns are in the table.

- Table.get_row_data(row): will return a dictionary with as many keys as columns are in the table and
  with values corresponding the number of row passed as argument (Row 0 is the first row **after** the
  header row)

- Cell.get_value(): will return the value displayed by the cell

- Cell.set_value(value): Cell will display the value passed as argument

### Some features

Simple left click on a cell will highlight it.
Double left click will highlight its row.
Triple left click will highlight its column.

Work in progress...

## Changelog

v 0.2.0[02/28/2021]: The table includes its own tkinter frame master. Added set and get data functions.
