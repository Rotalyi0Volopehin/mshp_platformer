# Импорт классов ячеек статической сетки
from src.static_grid_cells.brick_cell import BrickCell
from src.static_grid_cells.Tube import Tube
from src.static_grid_cells.TubeTop import TubeTop
# Импорт классов сущностей
from src.entities.fake_cloud import FakeCloud
from src.entities.Flower import Flower


# Это регистр соответствия игровых объектов и символов записи (используются в файлах структуры уровней - "struct.txt")
class SaveSymbolRegister: #static
    static_grid_cell_dict = None
    entity_dict = None

    def init():
        SaveSymbolRegister.__init_static_grid_cell_dict()
        SaveSymbolRegister.__init_entity_dict()

    def __init_static_grid_cell_dict():
        SaveSymbolRegister.static_grid_cell_dict = { }
        SaveSymbolRegister.static_grid_cell_dict.update({'B': BrickCell})
        SaveSymbolRegister.static_grid_cell_dict.update( {'T': Tube} )
        SaveSymbolRegister.static_grid_cell_dict.update({'P': TubeTop})

    def __init_entity_dict():
        SaveSymbolRegister.entity_dict = { }
        SaveSymbolRegister.entity_dict['~'] = FakeCloud #<- Пример регистрации класса сущности
        SaveSymbolRegister.entity_dict['F'] = Flower # это цветок (враг)

