from src.obstacle import Obstacle


class BrickCell(Obstacle):
    def do_register_collisions(self):
        return False