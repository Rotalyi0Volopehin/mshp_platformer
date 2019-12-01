from src.entities.npc import NPC
from src.constants import Stats


# Патрулирующий NPC
class PatrollingNPC(NPC):

    def __init__(self, game, image, posx, posy, speed, distance):
        super().__init__(game, image, posx, posy)
        self.steps = 0
        self.speed = speed
        self.distance = distance

    def process_logic(self):
        super().process_logic()
        if (self.vx > 0) and (self.rect.right >= self.game_object.gameplay_stage.current_level.width - 1):
            self.change_direction()
        elif (self.vx < 0) and (self.rect.x <= 0):
            self.change_direction()

        if self.on_ground:
            self.vy = 0
            self.vx = self.speed
        else:
            self.vy = Stats.GRAVITY
            self.vx = 0

        self.steps += abs(self.speed)
        if self.steps >= self.distance:
            self.change_direction()

    def player_collision(self, collision):
        if collision.top:
            self.die()

    def obstacle_collision(self, collision):
        if collision.left or collision.right:
            self.change_direction()

    def change_direction(self):
        if self.steps < 10:
            return
        self.speed = -self.speed
        self.steps = 0

    def die(self):
        super().die()
