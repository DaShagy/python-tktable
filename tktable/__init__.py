__version__ = '0.1.0'


from tkinter import *
import numbers

class Table():
    def __init__(self, master, col=4, row=4):

        self._master = master

        self._row_number = row
        self._col_number = col

        self.rows = []
        self.cols = []

        self.selected_cell = None
        self.selected_row = None

        self.bind_mouse_button()
        self.create_table()

    def __str__(self) -> str:
        return f"Rows: {self._row_number}, Cols: {self._col_number}"

    def bind_mouse_button(self):
        self._master.master.bind('<Button-1>', self.select_cell)
        self._master.master.bind('<Double-Button-1>', self.select_row)

    def create_rows(self):
        for row in range(self._row_number):
            r = Row(self._master, self._col_number, row)
            self.rows.append(r)

    def create_columns(self):
        for col in range(self._col_number):
            c = Column(self._master, self._row_number, col)
            for row in range(self._row_number):
                temp_row = self.rows[row]
                cell = temp_row.get_cell(col)
                c._cells.append(cell)       
            self.cols.append(c)

    def create_table(self):
        self.create_rows()
        self.create_columns()

    def get_cell_line(self, row, col):
        if 0 <= row < self._row_number and 0 <= col < self._col_number:
            return self.rows[row], self.cols[col]

    def get_row(self, row, col):
        r, _ = self.get_cell_line(row, col)
        return r

    def get_column(self, row, col):
        _, c = self.get_cell_line(row, col)
        return c

    def get_cell(self, row, col):
        return self.get_row(row, col).get_cell(col)

    def find_widget(self, event):
        x = event.x_root - self._master.winfo_rootx() 
        y = event.y_root - self._master.winfo_rooty()
        (col, row) = self._master.grid_location(x,y)
        return row, col

    def find_cell(self, event):
        row, col = self.find_widget(event)     
        return self.get_cell(row, col)

    def find_row(self, event):
        row, col = self.find_widget(event)
        return self.get_row(row, col)

    def focus_selected_cell(self, cell):
        self.selected_cell = cell
        self.selected_cell.focus_cell()

    def unfocus_selected_cell(self):
        self.selected_cell.unfocus_cell()
        self.selected_cell = None

    def select_cell(self, event):
        try:
            if isinstance(self.selected_row, Row):
                self.unfocus_selected_row()

            cell = self.find_cell(event)

            if not isinstance(self.selected_cell, Cell):
                self.focus_selected_cell(cell)
            elif self.selected_cell == cell:
                self.unfocus_selected_cell()
            else:
                self.unfocus_selected_cell()
                self.focus_selected_cell(cell)
        except:
            pass

    def focus_selected_row(self, row):
        self.selected_row = row
        self.selected_row.focus_cells()

    def unfocus_selected_row(self):
        self.selected_row.unfocus_cells()
        self.selected_row = None

    def select_row(self, event):
        try:
            row = self.find_row(event)
            if not isinstance(self.selected_row, Row):
                self.focus_selected_row(row)
            elif self.selected_row == row:
                self.unfocus_selected_row()
            else:
                self.unfocus_selected_row()
                self.focus_selected_row(row)
        except:
            pass

    #TODO: Simplefy and generalize 'insert_headers'
    #############################

    def insert_headers(self, data):
        headers = [*data.keys()]
        print(headers)
        header_row = self.get_row(0, 0)
        for cell, key in zip(header_row.get_cells(), headers):
            cell.set_value(key)

    ##############################

    def insert_row(self):
        new_row = Row(self._master, len(self.cols), self._row_number)
        self.rows.append(new_row)
        for col, cell in zip(self.cols, new_row.get_cells()):
            col.get_cells().append(cell)
        self._row_number += 1


    #TODO: Implement insert columns

    '''

    def insert_col(self):
        new_col = Column(self._master, len(self.rows), self._col_number)
        self.cols.append(new_col)
        for row, cell in zip(self.rows, new_col.get_cells()):
            row.get_cells().append(cell)
        self._col_number += 1

    '''

class Cell(Entry):
    def __init__(self, master, posx=0, posy=0):
        self._root = master
        Entry.__init__(self, self._root)
        self._value = StringVar()

        self.grid(column=posx, row=posy)
        self.config(state="readonly", readonlybackground="white", textvariable=self._value, cursor="arrow")
        self.set_value(f"{posx},{posy}")

    def focus_cell(self):
        self.config(readonlybackground="lightblue")

    def unfocus_cell(self):
        self.config(readonlybackground="white")

    def set_value(self, value):
        if isinstance(value, numbers.Number):         
            self.config(justify=RIGHT)
        else:
            self.config(justify=LEFT)
        self._value.set(value)

    def get_value(self):
        return self._value.get()


class Cell_Line():
    def __init__(self, master, len):
        self._root = master
        self._cells = []
        self._length = len

    def create_cells(self, i):
        for n in range(self._length):
            cell = Cell(self._root, posx=n, posy=i)
            self._cells.append(cell)

    def get_cells(self):
        return self._cells

    def get_cell(self, i):
        return self._cells[i]

    def focus_cells(self):
        for cell in self._cells:
            cell.focus_cell()
    
    def unfocus_cells(self):
        for cell in self._cells:
            cell.unfocus_cell()

class Row(Cell_Line):
    def __init__(self, master, len, row_number):
        super().__init__(master, len)
        self.create_cells(row_number)


class Column(Cell_Line):
    def __init__(self, master, len, col_number):
        super().__init__(master, len)

#Test

def _test():
    d = {"Name": "Juan", "Age": 24}
    root = Tk()
    root.title("Test")
    frame = Frame(root, padx=10, pady=10)
    table = Table(frame)
    table.insert_row()
    #table.insert_col()
    #table.insert_row()
    frame.pack()

    

    #print(table.get_column(0).get_cell(3))

    root.mainloop()

if __name__ == "__main__":
    _test()