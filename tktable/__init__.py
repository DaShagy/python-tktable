from tkinter import *
import numbers

class Table():
    def __init__(self, master, row=4, col=4):

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
            if col % self._col_number == 0:
                for row in range(self._row_number):
                    temp_row = self.rows[row]
                    cell = temp_row.get_cells()[col]
                    c._cells.append(cell)
            self.cols.append(c)

    def create_table(self):
        self.create_rows()
        self.create_columns()

    def get_row(self, row):
        try:
            return self.rows[row]
        except:
            pass

    def get_column(self, col):
        try:
            return self.cols[col]
        except:
            pass

    def get_cell(self, row, col):
        return self.rows[row].get_cell(col)

    def find_widget(self, event):
        x = event.x_root - self._master.winfo_rootx() 
        y = event.y_root - self._master.winfo_rooty()
        (col, row) = self._master.grid_location(x,y)
        return row, col

    def find_cell(self, event):
        row, col = self.find_widget(event)     
        return self.get_cell(row, col)

    def find_row(self, event):
        row, _ = self.find_widget(event)
        return self.get_row(row)

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

class Cell(Entry):
    def __init__(self, master, value="", posx=0, posy=0):
        self._root = master
        Entry.__init__(self, self._root)
        self._value = StringVar()

        self.grid(column=posx, row=posy)
        self.config(state="readonly", readonlybackground="white", textvariable=self._value, cursor="arrow")

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
    root = Tk()
    frame = Frame(root, padx=10, pady=10)
    table = Table(frame)
    frame.pack()
    cell = table.cols[0]._cells[0]
    cell.set_value(47)

    print(cell.get_value())


    #print(table.get_column(0).get_cell(3))

    root.mainloop()

if __name__ == "__main__":
    _test()