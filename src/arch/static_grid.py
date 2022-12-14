from src.exceptions import Exceptions
from src.arch.static_grid_cell import StaticGridCell
from src.arch.save_symbol_register import SaveSymbolRegister


# Это сетка статических игровых объектов (игровое поле)
class StaticGrid:
    def __init__(self, game, level, lvl_struct_lines, images):
        if not (isinstance(lvl_struct_lines, type([])) and isinstance(images, type({}))):
            Exceptions.throw(Exceptions.argument_type)
        self.level = level
        self.cells = [[] for _ in  range(len(lvl_struct_lines))]
        if SaveSymbolRegister.static_grid_cell_dict == None:
            SaveSymbolRegister.init()
        for iy in range(len(lvl_struct_lines)):
            line = lvl_struct_lines[iy]
            if not isinstance(line, str):
                Exceptions.throw(Exceptions.argument_type)
            if (iy > 0) and (len(line) != len(self.cells[iy - 1])):
                Exceptions.throw(Exceptions.argument_type, "lines of the level's save-file must have equal length")
            for ix in range(len(line)):
                symbol = line[ix]
                if symbol in SaveSymbolRegister.static_grid_cell_dict:
                    cell_type = SaveSymbolRegister.static_grid_cell_dict[symbol]
                    cell = cell_type(game, images[cell_type.__name__], ix, iy)
                    if not isinstance(cell, StaticGridCell):
                        Exceptions.throw(Exceptions.return_type)
                    self.cells[iy].append(cell)
                else:
                    self.cells[iy].append(None)

    @property
    def width(self):
        return len(self.cells[0])

    @property
    def height(self):
        return len(self.cells)