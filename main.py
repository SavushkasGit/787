import pygame
import random
import sys

# Initializations
pygame.init()
clock = pygame.time.Clock()

# Window settings
screen_width = 400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Гонки на трассе")
pygame.display.set_icon(pygame.image.load("unnamed.bmp"))
bg = pygame.image.load("road.jpg")
FPS = 120
sound = pygame.mixer.Sound("gonka.wav")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player and enemy settings
player_width = 50
player_height = 100
player_x = 375
player_y = 500
player_speed = 7

enemy_width = 65
enemy_height = 125
enemy_x = 200
enemy_y = 50
enemy_speed = 6


def game_loop():
    player_x = 175
    player_y = 700
    enemy_x = 200
    enemy_y = 50

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0, 0))
        sound.play(0)

        keys = pygame.key.get_pressed()

        # Player movement
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            if player_x < 0:
                player_x = 0
        elif keys[pygame.K_RIGHT]:
            player_x += player_speed
            if player_x > screen_width - player_width:
                player_x = screen_width - player_width
        elif keys[pygame.K_UP]:
            player_y -= player_speed
            if player_y < 0:
                player_y = 0
        elif keys[pygame.K_DOWN]:
            player_y += player_speed
            if player_y > screen_height - player_height:
                player_y = screen_height - player_height

        # Enemy movement
        enemy_y += enemy_speed
        if enemy_y > screen_height:
            enemy_y = 0
            enemy_x = random.randint(0, screen_width - player_width)

        player = pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
        enemy = pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

        # Collision
        if player.colliderect(enemy):
            running = False
            game_over_screen()

        pygame.display.update()
        clock.tick(FPS)


def start_screen():
    while True:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 26)
        text = font.render("Для старта нажмите на любую кнопку", True, GREEN)
        screen.blit(text, (50, screen_height // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game_loop()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def game_over_screen():
    while True:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 23)
        text = font.render("Нажмите R для перезапуска или Q для выхода", True, RED)
        screen.blit(text, (25, screen_height // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


start_screen()