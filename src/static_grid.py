from src.exceptions import Exceptions
from src.static_grid_cells import StaticGridCell
from src.base_classes import DrawableObject


# Это сетка статических игровых объектов 64x64 (игровое поле)
class StaticGrid(DrawableObject):
    def __init__(self, game, level, lvl_struct_lines, images):
        super().__init__(game)
        if not (isinstance(lvl_struct_lines, type([])) and isinstance(images, type({}))):
            Exceptions.throw(Exceptions.argument_type)
        self.level = level
        self.cells = [[]] * len(lvl_struct_lines)
        if StaticGridCell.cell_types_from_save_symbols == None:
            StaticGridCell.init()
        for iy in range(len(lvl_struct_lines)):
            line = lvl_struct_lines[iy]
            if not isinstance(line, str):
                Exceptions.throw(Exceptions.argument_type)
            if (iy > 0) and (len(line) != len(self.cells[iy - 1])):
                Exceptions.throw(Exceptions.argument_type, "lines of the level's save-file must have equal length")
            for ix in range(len(line)):
                symbol = line[ix]
                if symbol in StaticGridCell.cell_types_from_save_symbols:
                    cell_type = StaticGridCell.cell_types_from_save_symbols[symbol]
                    cell = cell_type(game, images[cell_type.__name__], ix, iy)
                    if not isinstance(cell, StaticGridCell):
                        Exceptions.throw(Exceptions.argument_type)
                    self.cells[iy].append(cell)
                else:
                    self.cells[iy].append(None)

    def process_draw(self):
        self.game_object.screen.blit(self.level.background, self.level.background.get_rect())
        for row in self.cells:
            for cell in row:
                if cell != None:
                    cell.process_draw()