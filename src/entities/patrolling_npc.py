from src.entities.npc import NPC


# Патрулирующий NPC
class PatrollingNPC(NPC):

    _temp_gravity = 1

    def __init__(self, game, image, posx, posy, speed, distance):
        super().__init__(game, image, posx, posy)
        self.steps = 0
        self.speed = speed
        self.distance = distance

    def process_logic(self):
        super().process_logic()
        if (self.vx > 0) and (self.rect.right > self.game_object.current_level().width()):
            self.change_direction()
        elif (self.vx < 0) and (self.rect.x <= 0):
            self.change_direction()

        if self.on_ground:
            self.vy = 0
            self.vx = self.speed
        else:
            self.vy = self._temp_gravity
            self.vx = 0

        self.apply_velocity()
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
        self.speed = -self.speed
        self.steps = 0

    def die(self):
        super().die()
