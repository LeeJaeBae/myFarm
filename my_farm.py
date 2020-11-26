# Pygame template - skeleton for a new pygame project
import pygame
import random
import math
from os import path
import Farm

WIDTH = 1024
HEIGHT = 768
FPS = 60

# define colors 자주쓰이는 색을 미리 지정해줬습니다
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
# mixer란 효과음을 쓸 때 유용하다.
pygame.mixer.init()
# 게임의 스크린 크기를 정해줍니다
game_world = pygame.display.set_mode((WIDTH, HEIGHT))
# 게임의 제목을 정해줍니다.
pygame.display.set_caption("GREAT ADVENTURE OF TOP")

# folder 폴더를 미리 지정해주어 간단하게 이용할 수 있게 했습니다.
game_folder = path.dirname(__file__)
image_folder = path.join(game_folder, 'image')

# 자주쓰이는 Clock의 객체를 만들어줍니다.
clock = pygame.time.Clock()

TILESIZE = 48

# player을 생성
player = Farm.Player()
# sprite_group로 선언된 sprite의 Group()에 player를 넣는다.
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
# player의 처음 위치를 화면의 중간으로 설정한다.
player.rect.x = WIDTH / 2
player.rect.y = HEIGHT / 2


def draw_grid():
    # 0부터 TILESIZE씩 건너뛰면서 WIDTH까지 라인을 그려준다
    for x in range(0, WIDTH, TILESIZE):
        # 첫번째 인자부터 game_world(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
        pygame.draw.line(game_world, (0, 0, 0, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(game_world, (0, 0, 0, 50), (0, y), (WIDTH, y))


# Game loop 게임이 실행되는 메인 반복문입니다. 프레임마다 반복문이 실행된다고 보면 됩니다
running = True
while running:
    # keep loop running at the right speed 초당 프레임을 지정해줍니다
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        key_event = pygame.key.get_pressed()

        if key_event[pygame.K_UP]:
            player.up()
        if key_event[pygame.K_DOWN]:
            player.down()
        if key_event[pygame.K_LEFT]:
            player.left()
        if key_event[pygame.K_RIGHT]:
            player.right()

    # Update

    # Draw / render
    # 우선 화면을 하얀색으로 채워주자
    game_world.fill(WHITE)
    draw_grid()

    # player.update()
    sprite_group.draw(game_world)
    # 가상의 궤도 중간에 점을 찍어 잘 회전하는지 확인해본다.
    # *after* drawing everything, update the display
    pygame.display.update()

pygame.quit()
