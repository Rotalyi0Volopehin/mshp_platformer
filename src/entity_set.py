from src.entity import Entity
from src.save_symbol_register import SaveSymbolRegister
from src.exceptions import Exceptions


# Это множество всех сущностей, используемых на одном уровне
class EntitySet:
    def __init__(self, game, level, lvl_struct_lines, images):
        if not (isinstance(lvl_struct_lines, type([])) and isinstance(images, type({}))):
            Exceptions.throw(Exceptions.argument_type)
        self.level = level
        self.entities = []
        if SaveSymbolRegister.entity_dict == None:
            SaveSymbolRegister.init()
        for iy in range(len(lvl_struct_lines)):
            line = lvl_struct_lines[iy]
            if not isinstance(line, str):
                Exceptions.throw(Exceptions.argument_type)
            if (iy > 0) and (len(line) != len(lvl_struct_lines[iy - 1])):
                Exceptions.throw(Exceptions.argument_type, "lines of the level's save-file must have equal length")
            for ix in range(len(line)):
                symbol = line[ix]
                if symbol in SaveSymbolRegister.entity_dict:
                    cell_type = SaveSymbolRegister.entity_dict[symbol]
                    cell = cell_type(game, images[cell_type.__name__], ix << 6, iy << 6)
                    if not isinstance(cell, Entity):
                        Exceptions.throw(Exceptions.return_type)
                    self.entities.append(cell)
