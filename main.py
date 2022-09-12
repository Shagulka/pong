#classic pong game with 3 difficulties

import pygame
import random
import time
import sys
import os
import math


#initialize pygame
pygame.init()

#set up the drawing window
screen = pygame.display.set_mode([800, 600])

#set up the clock
clock = pygame.time.Clock()

#set up the font
font = pygame.font.SysFont('Comic Sans MS', 30)

#set up the sounds
pygame.mixer.init()



#set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#set up the variables
paddle1_x = 10
paddle1_y = 250
paddle2_x = 780
paddle2_y = 250
paddle_width = 10
paddle_height = 100
ball_x = 400
ball_y = 300
ball_radius = 10
ball_x_speed = 0
ball_y_speed = 0
paddle1_score = 0
paddle2_score = 0
paddle1_speed = 0
paddle2_speed = 0

#set up the difficulty
difficulty = input('Choose a difficulty: easy, medium, hard: ')
if difficulty == 'easy':
    paddle1_speed = 5
    paddle2_speed = 5
    ball_x_speed = 5
    ball_y_speed = 5
elif difficulty == 'medium':
    paddle1_speed = 10
    paddle2_speed = 10
    ball_x_speed = 10
    ball_y_speed = 10
elif difficulty == 'hard':
    paddle1_speed = 15
    paddle2_speed = 15
    ball_x_speed = 15
    ball_y_speed = 15
else:
    print('Invalid difficulty. Please choose easy, medium, or hard.')
    sys.exit()

#set up the game loop
running = True
while running:
    #set up the screen
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    paddle1_score_text = font.render(str(paddle1_score), False, white)
    paddle2_score_text = font.render(str(paddle2_score), False, white)
    screen.blit(paddle1_score_text, (400, 10))
    screen.blit(paddle2_score_text, (400, 40))

    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= paddle1_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle1_speed
    if keys[pygame.K_UP]:
        paddle2_y -= paddle2_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle2_speed

    #check for paddle collisions
    if paddle1_y <= 0:
        paddle1_y = 0
    if paddle1_y >= 500:
        paddle1_y = 500
    if paddle2_y <= 0:
        paddle2_y = 0
    if paddle2_y >= 500:
        paddle2_y = 500

    #move the ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    #check for ball collisions
    if ball_y <= 10 or ball_y >= 590:
        ball_y_speed *= -1
  
    if ball_x <= 20 and ball_y >= paddle1_y and ball_y <= paddle1_y + 100:
        ball_x_speed *= -1
   
    if ball_x >= 780 and ball_y >= paddle2_y and ball_y <= paddle2_y + 100:
        ball_x_speed *= -1
     
    if ball_x <= 0:
        paddle2_score += 1
        ball_x = 400
        ball_y = 300
        ball_x_speed = 5
        ball_y_speed = 5
  
    if ball_x >= 800:
        paddle1_score += 1
        ball_x = 400
        ball_y = 300
        ball_x_speed = 5
        ball_y_speed = 5
  

    #update the display
    pygame.display.flip()

    #set the framerate
    clock.tick(60)

#done
pygame.quit()

