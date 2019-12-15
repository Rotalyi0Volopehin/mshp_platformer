import pygame
import glob

from src.io_tools import IO_Tools


class SFX_Player:
    sounds = { }
    volume = 0.5

    @staticmethod
    def load():
        SFX_Player.sounds = { }
        slash = IO_Tools.sep_slash()
        for sound_path in glob.glob("sfx{}*.wav".format(slash)):
            sound_name = sound_path[sound_path.rfind(slash) + 1: sound_path.rfind('.')]
            SFX_Player.sounds[sound_name] = pygame.mixer.Sound(sound_path)

    @staticmethod
    def play_sound(name):
        if SFX_Player.volume > 0.01:
            sound = SFX_Player.sounds[name]
            sound.set_volume(SFX_Player.volume)
            sound.play()