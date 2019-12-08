# Импорт классов ячеек статической сетки
from src.static_grid_cells.brick_cell import BrickCell

# Импорт классов сущностей
from src.entities.fake_cloud import FakeCloud
from src.entities.player import Player
from src.static_grid_cells.question_block import Question

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
        SaveSymbolRegister.static_grid_cell_dict['?'] = Question

    def __init_entity_dict():
        SaveSymbolRegister.entity_dict = { }
        SaveSymbolRegister.entity_dict['~'] = FakeCloud #<- Пример регистрации класса сущности
        SaveSymbolRegister.entity_dict['P'] = Player