import pygame

from ..Object import Object


class Chicken(Object):
    def __init__(self, img, x, y, area: pygame.Rect):
        Object.__init__(self, img, x, y)
        self.area = area

    def update(self, direction):
        super().update(direction)
        print(self.rect.contains(self.area))
