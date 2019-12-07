﻿# Импорт классов ячеек статической сетки
from src.static_grid_cells.brick_cell import BrickCell
from src.static_grid_cells.tube import Tube
from src.static_grid_cells.tube_top import TubeTop

# Импорт классов сущностей
from src.entities.fake_cloud import FakeCloud
from src.entities.flower import Flower
from src.entities.player import Player


# Это регистр соответствия игровых объектов и символов записи (используются в файлах структуры уровней - "struct.txt")
class SaveSymbolRegister: #static
    static_grid_cell_dict = None
    entity_dict = None

    def init():
        SaveSymbolRegister.__init_static_grid_cell_dict()
        SaveSymbolRegister.__init_entity_dict()

    def __init_static_grid_cell_dict():
        SaveSymbolRegister.static_grid_cell_dict = { }
        SaveSymbolRegister.static_grid_cell_dict['B'] = BrickCell #<- Пример регистрации класса ячейки статической сетки (блока)
        SaveSymbolRegister.static_grid_cell_dict['T'] = TubeTop
        SaveSymbolRegister.static_grid_cell_dict['I'] = Tube

    def __init_entity_dict():
        SaveSymbolRegister.entity_dict = { }
        SaveSymbolRegister.entity_dict['~'] = FakeCloud #<- Пример регистрации класса сущности
        SaveSymbolRegister.entity_dict['F'] = Flower
        SaveSymbolRegister.entity_dict['P'] = Player