from board import boards
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
color = 'blue'
PI = math.pi
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
player_x = 450
player_y = 663
direction = 0
counter = 0

def draw_board(level):
    num1 = ((HEIGHT - 50) // len(level))  # Adjusted to use the actual level height
    num2 = (WIDTH // len(level[0])) if level and level[0] else 1  # Avoid division by zero
    for i in range(len(level)):
        for j in range(len(level[i])):
            
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + int(0.5 * num2), i * num1 + int(0.5 * num1)), 4)
            
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + int(0.5 * num2), i * num1 + int(0.5 * num1)), 10)
            
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + int(0.5 * num2), i * num1),
                (j * num2 + int(0.5 * num2), i * num1 + num1), 3)
            
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                (j * num2 + int(num2), i * num1 + (0.5 * num1)), 3)    

            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5*num1)), num2, num1], 0, PI/2,3)

            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)) - 2, (i * num1 + (0.5*num1)), num2, num1], PI/2,3)

            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4*num1)), num2, num1], PI, 3*PI/2,3)

            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4*num1)), num2, num1], 3*PI / 2, 2*PI,3)

            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                (j * num2 + int(num2), i * num1 + (0.5 * num1)), 3)    
    

def draw_player():
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5],True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90, (player_x, player_y)))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5],270), (player_x, player_y))
    
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)
    draw_player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
