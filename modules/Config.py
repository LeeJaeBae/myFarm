from os import path

from cv2 import cv2
import pygame

ROOT_DIR = path.dirname(path.dirname(__file__))
img = pygame.image.load(path.join(ROOT_DIR, 'images/money.png'))

pygame.font.init()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('font/retro.ttf', size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Money(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0, 10), (60, 60))
        self.image = img
        self.point = 0

# class
