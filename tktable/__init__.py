__version__ = '0.1.0'


from tkinter import *
import numbers

class Table():
    def __init__(self, master, col=4, row=4):

        self._master = master

        self._row_number = row
        self._col_number = col

        self.cells = []

        self.selected_cell = None
        self.selected_line = None

        self.bind_mouse_button()
        self.create_cells()

    def __str__(self) -> str:
        return f"Rows: {self._row_number}, Cols: {self._col_number}"

    def bind_mouse_button(self):
        self._master.master.bind('<Button-1>', self.select_cell)
        self._master.master.bind('<Double-Button-1>', self.select_row)
        self._master.master.bind('<Triple-Button-1>', self.select_col)

    def create_cells(self):
        for row in range(self._col_number):
            for col in range(self._row_number):
                cell = Cell(self._master, col, row)
                self.cells.append((cell, col, row))

    def get_cell(self, row, col):
        return [t[0] for _, t in enumerate(self.cells) if t[1]==col and t[2]==row].pop()

    def get_cell_line(self, n, type="ROW"):
        try:
            if type=="ROW":
                return [t[0] for _, t in enumerate(self.cells) if t[2] == n]
            if type=="COL":
                return [t[0] for _, t in enumerate(self.cells) if t[1] == n]
        except:
            pass

    def find_widget(self, event):
        x = event.x_root - self._master.winfo_rootx() 
        y = event.y_root - self._master.winfo_rooty()
        (col, row) = self._master.grid_location(x,y)
        return row, col

    def find_cell(self, event):
        row, col = self.find_widget(event)     
        return self.get_cell(row, col)

    def find_cell_line(self, event, type="ROW"):
        row, col = self.find_widget(event)
        try:
            if type=="ROW":
                cell_line = Cell_Line (self._master, self.get_cell_line(row, type))
            if type=="COL":
                cell_line = Cell_Line (self._master, self.get_cell_line(col, type))
            return cell_line
        except:
            pass

    def focus_selected_cell(self, cell):
        self.selected_cell = cell
        self.selected_cell.focus_cell()

    def unfocus_selected_cell(self):
        self.selected_cell.unfocus_cell()
        self.selected_cell = None

    def select_cell(self, event):
        try:
            cell = self.find_cell(event)
            if self.selected_line:
                self.selected_line.unfocus_cells()
            if not isinstance(self.selected_cell, Cell):
                self.focus_selected_cell(cell)
            elif self.selected_cell == cell:
                self.unfocus_selected_cell()
            else:
                self.unfocus_selected_cell()
                self.focus_selected_cell(cell)
        except:
            pass

    def focus_selected_line(self, line):
        self.selected_line = line
        self.selected_line.focus_cells()

    def unfocus_selected_line(self):
        self.selected_line.unfocus_cells()
        del self.selected_line
        self.selected_line = None    
  
    def select_row(self, event):
        try:
            row = self.find_cell_line(event)
            if not isinstance(self.selected_line, Cell_Line):
                self.focus_selected_line(row)
            elif self.selected_line == row:
                self.unfocus_selected_line()
            else:
                self.unfocus_selected_line()
                self.focus_selected_line(row)
        except:
            pass

    def select_col(self, event):
        try:
            col = self.find_cell_line(event, type="COL")
            if not isinstance(self.selected_line, Cell_Line):
                self.focus_selected_line(col)
            elif self.selected_line == col:
                self.unfocus_selected_line()
            else:
                self.unfocus_selected_line()
                self.focus_selected_line(col)
        except:
            pass

    '''
    '''

    #TODO: Simplefy and generalize 'insert_headers'
    #############################

    def insert_headers(self, data):
        headers = [*data.keys()]
        print(headers)
        header_row = self.get_row(0, 0)
        for cell, key in zip(header_row.get_cells(), headers):
            cell.set_value(key)

    ##############################
    '''

    def insert_row(self):
        new_row = Row(self._master, len(self.cols), self._row_number)
        self.rows.append(new_row)
        for col, cell in zip(self.cols, new_row.get_cells()):
            col.get_cells().append(cell)
        self._row_number += 1


    #TODO: Implement insert columns

    

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
        self._pos = (posx, posy)

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

    def get_pos(self):
        return (self._pos)

class Cell_Line():
    def __init__(self, master, cells):
        self._root = master
        self._cells = cells
        self._length = len(self._cells)

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

    #def __del__(self):
    #    print(__class__.__name__, "destroyed")

#Test

def _test():
    d = {"Name": "Juan", "Age": 24}
    root = Tk()
    root.title("Test")
    frame = Frame(root, padx=10, pady=10)
    table = Table(frame)
    #table.insert_row()
    #table.insert_col()
    #table.insert_row()
    frame.pack()

    

    #print(table.get_column(0).get_cell(3))

    root.mainloop()

if __name__ == "__main__":
    _test()