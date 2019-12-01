from src.entities.patrolling_npc import PatrollingNPC


class Mushroom(PatrollingNPC):

    # Скорость перемещения
    speed = 0.25
    # Дистанция патрулирования
    distance = 100

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, self.speed, self.distance)
