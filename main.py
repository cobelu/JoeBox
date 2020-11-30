# Connor Luckett for Joe Nelson - 2020
# This code was based on the following:
# https://projects.raspberrypi.org/en/projects/gpio-music-box/4
# Buttons should be wired to pins 17 (3V) and 5 (GND)

import pygame
from gpiozero import Button


def main():
    """
    Plays the given sound on button press.

    """
    # Note the location of the sound
    sound_file = ""

    # Initialize pygame and load the sound
    pygame.init()
    sound = pygame.mixer.Sound(sound_file)

    # Link the sound to the button
    btn = Button(17)
    btn.when_pressed = sound.play


if __name__ == '__main__':
    main()
