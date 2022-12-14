# Импорт классов ячеек статической сетки
from src.static_grid_cells.brick_cell import BrickCell
from src.static_grid_cells.castle import CastleEntry
from src.static_grid_cells.tube import TubeBottom
from src.static_grid_cells.tube import TubeTop
from src.static_grid_cells.coin import Coin
from src.static_grid_cells.question_block import Question
from src.static_grid_cells.princess import Princess
from src.static_grid_cells.player_ghost import PlayerGhost

# Импорт классов сущностей
from src.entities.fake_cloud import FakeCloud
from src.entities.player import Player
from src.entities.flower import Flower
from src.entities.mushroom import Mushroom
from src.entities.turtle import Turtle


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
        SaveSymbolRegister.static_grid_cell_dict['E'] = CastleEntry
        SaveSymbolRegister.static_grid_cell_dict['t'] = TubeBottom
        SaveSymbolRegister.static_grid_cell_dict['T'] = TubeTop
        SaveSymbolRegister.static_grid_cell_dict['C'] = Coin
        SaveSymbolRegister.static_grid_cell_dict['?'] = Question
        SaveSymbolRegister.static_grid_cell_dict['V'] = Princess
        SaveSymbolRegister.static_grid_cell_dict['G'] = PlayerGhost

    def __init_entity_dict():
        SaveSymbolRegister.entity_dict = { }
        SaveSymbolRegister.entity_dict['~'] = FakeCloud #<- Пример регистрации класса сущности
        SaveSymbolRegister.entity_dict['P'] = Player
        SaveSymbolRegister.entity_dict['F'] = Flower
        SaveSymbolRegister.entity_dict['M'] = Mushroom
        SaveSymbolRegister.entity_dict['S'] = Turtle