import random

import pygame
from os import path
import modules
from modules.Config import Money, draw_text
from modules.Object import Object
from modules.Animals.Chicken import Chicken

images_folder = path.join(modules.Config.ROOT_DIR, "images")

# load images
bg = pygame.image.load(path.join(images_folder, 'farm2.png'))

character_sheet = pygame.image.load(path.join(images_folder, 'character.png'))
farmer_image = pygame.image.load(path.join(images_folder, 'farmer.png'))
chicken_image = pygame.image.load(path.join(images_folder, 'chicken.png'))

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(size=(1024, 768 + 80))
clock = pygame.time.Clock()
pygame.display.set_caption("myFarm")
FPS = 30

sprites = pygame.sprite.Group()
farm_sprites = pygame.sprite.Group()
layered_updates = pygame.sprite.LayeredUpdates
sprites.add()

run = True
test_array = []


class Farmer(Object):
    def __init__(self, img, sheet, block=[]):
        self.left_states = {0: (1850, 7, 55, 72), 1: (1770, 6, 55, 72), 2: (1691, 6, 55, 72), 3: (1610, 6, 55, 72)}
        self.right_states = {0: (13, 6, 55, 70), 1: (93, 6, 55, 72), 2: (173, 6, 55, 72), 3: (253, 6, 55, 72)}
        self.up_states = {0: (13, 404, 55, 72), 1: (93, 404, 55, 72), 2: (173, 404, 55, 72), 3: (253, 404, 55, 72)}
        self.down_states = {0: (491, 404, 55, 72), 1: (570, 404, 55, 72), 2: (651, 404, 55, 72), 3: (732, 404, 55, 72)}
        Object.__init__(self, img, 500, 350, self.left_states, self.right_states, self.up_states, self.down_states,
                        sheet)
        self.block_area = block

    def handle_event(self, event):
        if len(self.block_area) > 0:
            for block in self.block_area:
                block = block.get_rect() if type(block) is not pygame.Rect else block
                if self.rect.colliderect(block):
                    if self.rect.top <= block.bottom:
                        self.rect.y += 10
                    if self.rect.right >= block.left:
                        self.rect.x -= 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')

    def add_block_area(self, *stuff):
        # print(type(stuff))
        self.block_area.extend(stuff)


user = Farmer(farmer_image, character_sheet)
money = Money()

farm_sprites.add(user, money)

chicken_coop_area = pygame.Rect(850, 80, 160, 300)
chicken_coop = pygame.Surface(chicken_coop_area.size, pygame.SRCALPHA)
chicken_coop.fill((0, 0, 0, 0))

sheep_pasture_area = pygame.Rect(620, 80, 230, 310)
sheep_pasture = pygame.Surface(sheep_pasture_area.size, pygame.SRCALPHA)

sheep_pasture.fill((0, 0, 0, 0))

user.add_block_area(chicken_coop_area, sheep_pasture_area)

while run:
    # clock.tick(FPS)

    if len(sprites) > 0:
        for obj in sprites:
            if random.randint(0, 5) % 3 == 0:
                obj.auto()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # user.update('up'
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_SPACE:
                chick = Chicken(chicken_image, chicken_coop.get_rect().centerx, chicken_coop.get_rect().centery,
                                chicken_coop_area)
                sprites.add(chick)
                test_array.append(chick)
            if event.key == pygame.K_1:
                if len(test_array) > 0:
                    sprites.remove(test_array[len(test_array) - 1])
                    test_array.remove(test_array[len(test_array) - 1])
                money.point += 100
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.QUIT:
            run = False

    # sprites.update()
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 80))
    # sprites.draw(screen)
    draw_text(screen, str(money.point), 65, 70 + int(len(str(money.point)) * 10), 12)
    farm_sprites.draw(screen)
    screen.blit(chicken_coop, chicken_coop_area)
    screen.blit(sheep_pasture, sheep_pasture_area)
    screen.blit(user.image, user.rect)
    chicken_coop.fill((255, 255, 255, 0))
    sprites.draw(chicken_coop)
    user.handle_event(event)
    clock.tick(FPS)
    pygame.display.update()
# screen.blit()
