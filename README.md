# tktabl

This proyect intends to be a complement on managing tables within the Python Tkinter GUI.

## Installation

Run the following to install:

```python
pip install tktabl
```

## Usage

As tktable is a complement to tkinter, you must import it in your code:

```python
import tkinter as tk
import tktabl
```

A table needs a tkinter Frame as its master

```python
root = tk.Tk()
frame = tk.Frame(root)
table = tktable.Table(frame)
frame.pack()
```

By default, it creates a 4x4 table in the specified frame.
You can also specify it size passing 2 additional arguments (col, row), e.g.

```python
root = tk.Tk()
frame = tk.Frame(root)
table = tktable.Table(frame, col=3, row=5)
frame.pack()
```

Before you pack the frame, you can also set each cell value. To do that, you can access each cell
with the 'get_cell()' method, passing it position (row, column) within the table. e.g.

```python
root = tk.Tk()
frame = tk.Frame(root)
table = tktable.Table(frame, col=3, row=5)
my_cell = table.get_cell(2,2)
frame.pack()
```

Now, the my*cell variable is associated with the cell in the \_third* row and the _third_ column

You can set the value it displays with the Cell set*value(*"value"\_) method.

```python
...
table = tktable.Table(frame, col=3, row=5)
my_cell = table.get_cell(2,2)
my_cell.set_value("Hello World!")
frame.pack()
```

Now the cell will display the string "Hellow World!"

You can also get its value with the Cell get_value() method.

Simple left click on a cell will highlight it.
Double left click will highlight its row.
Triple left click will highlight its column.

Work in progress...
