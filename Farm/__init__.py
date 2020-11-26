import pygame
from os import path
import math

TILESIZE = 10


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # player의 이미지를 받아온다
        self.image = pygame.image.load(path.join(path.dirname(__file__) + "/img", 'player.png'))
        # player를 감싸는 사각형을 생성한다
        self.rect = self.image.get_rect()
        # player의 회전을 구현하기 위함
        self.rotate_angle = 0
        # player의 회전 속도
        self.rotate_speed = 1
        # player의 회전각
        self.rotate_angle = 0
        # player가 도는 궤도의 반지름
        self.orbit_radius = 100
        # player의 위치
        self.pos_x = 0
        self.pos_y = 0
        # play가 도는 궤도 중심의 위치
        self.orbit_pos_x = 0
        self.orbit_pos_y = 0

    def up(self):
        self.rect.y -= TILESIZE
        print(self.rect)

    def down(self):
        self.rect.y += TILESIZE
        print(self.rect)

    def left(self):
        self.rect.x -= TILESIZE
        print(self.rect)

    def right(self):
        self.rect.x += TILESIZE
        print(self.rect)

    def update(self):
        self.rotate_angle += self.rotate_speed / 100
        self.rect.centerx = self.orbit_pos_x + self.orbit_radius * math.cos(self.rotate_angle)
        self.rect.centery = self.orbit_pos_y + self.orbit_radius * math.sin(self.rotate_angle)


__all__ = ['Player']
