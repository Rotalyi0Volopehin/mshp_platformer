from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo


class Flower(DeathTouchEntity):
    #image = pygame.image.load(os.path.join(IMAGES_DIR, 'flower1.xcf'))

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, True))
        self.startposy = posy
        self.vy = -1

    def process_logic(self):
        self.rect.y += self.vy
        self.posy_carry += self.__calc_carry(self.vy)
        if (self.rect.y <= self.startposy) or (self.rect.y >= (self.startposy+128)):
            self.vy *= -1

    def __calc_carry(self, value):
        sign = (value > 0) - (value < 0)
        return abs(value) % 1 * sign

    def on_collide(self, collisions):
        pass

    def apply_gravity_force(self, value):
        self.vy += value

    def __calc_carry(self, value):
        sign = (value > 0) - (value < 0)
        return abs(value) % 1 * sign
