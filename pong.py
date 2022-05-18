# This imports the required Python module.
import pygame
from pygame import gfxdraw
import random

# This defines the game screen.
pygame.init()
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# This defines the background colour for the game screen
# and prop colour for everything else on the Pong game.
bg_color = pygame.Color("#001219")
prop_color = pygame.Color("#fefae0")

# This sets the ball and paddle sizes.
ball_radius = 15
player_width, player_height = 10, 150

# This determines the position of the ball
# and paddles on the screen on startup.
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height
                   // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
player1 = pygame.Rect(0, screen_height // 2 - player_height
                      // 2, player_width, player_height)
player2 = pygame.Rect(screen_width - player_width, screen_height
                      // 2 - player_height // 2, player_width, player_height)

# Variables to determines ball movement.
# Variables to determines player movement.
# Variables to represent the score for each player.
ball_speed_x, ball_speed_y = 10, 10
player_speed = 10
player1_delta, player2_delta = 0, 0
player1_score, player2_score = 0, 0

# This limits the speed of the ball during game.
# Sets font style and size for score keeping.
clock = pygame.time.Clock()
font = pygame.font.SysFont("inkfree", 35)

# The infinite loop keeps the game screen open until exiting the window.
# Determines actions for events, e.g. if user presses the up key,
# player 2 paddle moves up.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player1_delta = player_speed
            if event.key == pygame.K_w:
                player1_delta = -player_speed
            if event.key == pygame.K_DOWN:
                player2_delta = player_speed
            if event.key == pygame.K_UP:
                player2_delta = -player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player1_delta = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player2_delta = 0

    # This sets constraints for paddles on screen.
    player1.y += player1_delta
    player2.y += player2_delta
    player1.top = max(0, player1.top)
    player2.top = max(0, player2.top)
    player1.bottom = min(screen_height, player1.bottom)
    player2.bottom = min(screen_height, player2.bottom)

    # This updates the position of the ball.
    # So the ball will move 10 units forward along the x and y axes.
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # This sets the constraints of the game screen for the ball.
    # On hitting the screen constraints the ball changes direction.
    # On scoring a point, the ball resets at the centre of the screen,
    # and sets off in a random direction.
    # If the ball hits the left of the screen, player 2 records a point.
    # If the ball hits the right of the screen, player 1 records a point.
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            player2_score += 1
        else:
            player1_score += 1
        ball.center = (screen_width // 2, screen_height // 2)
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])

    # Similarly, on hitting the paddle, the ball changes direction.
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # This configures the screen appearance,
    # e.g. pygame.draw.aaline sets up the centre line
    # and gfxdraw.aacircle draws the centre circle.
    # For reference (screen_width // 2, screen_height // 2)
    # is the centre of the screen.
    screen.fill(bg_color)
    player1_text = font.render('Player A: {}'.format(player1_score),
                               True, prop_color)
    player1_text_rect = player1_text.get_rect()
    player1_text_rect.center = (screen_width // 4, 20)
    screen.blit(player1_text, player1_text_rect)
    player2_text = font.render('Player B: {}'.format(player2_score),
                               True, prop_color)
    player2_text_rect = player2_text.get_rect()
    player2_text_rect.center = (screen_width - screen_width // 4, 20)
    screen.blit(player2_text, player2_text_rect)
    pygame.draw.aaline(screen, prop_color, (screen_width // 2, 0),
                       (screen_width // 2, screen_height))
    gfxdraw.aacircle(screen, screen_width // 2, screen_height // 2, 200,
                     prop_color)
    pygame.draw.rect(screen, prop_color, player1)
    pygame.draw.rect(screen, prop_color, player2)
    gfxdraw.filled_circle(screen, ball.centerx, ball.centery, ball_radius,
                          prop_color)
    pygame.display.update()
    clock.tick(60)
