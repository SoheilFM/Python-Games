#pip install pygame
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up the paddles
paddle_width = 20
paddle_height = 100
paddle_speed = 5
left_paddle_pos = pygame.Rect(50, (screen_height - paddle_height) / 2, paddle_width, paddle_height)
right_paddle_pos = pygame.Rect(screen_width - 50 - paddle_width, (screen_height - paddle_height) / 2, paddle_width, paddle_height)

# Set up the ball
ball_pos = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
ball_speed_x = 5
ball_speed_y = 5

# Set up the score
font = pygame.font.Font(None, 50)
left_score = 0
right_score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_pos.top > 0:
        left_paddle_pos.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and left_paddle_pos.bottom < screen_height:
        left_paddle_pos.move_ip(0, paddle_speed)
    if keys[pygame.K_UP] and right_paddle_pos.top > 0:
        right_paddle_pos.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and right_paddle_pos.bottom < screen_height:
        right_paddle_pos.move_ip(0, paddle_speed)

    # Move the ball
    ball_pos.move_ip(ball_speed_x, ball_speed_y)

    # Check for collisions with the walls
    if ball_pos.top < 0 or ball_pos.bottom > screen_height:
        ball_speed_y *= -1
    if ball_pos.left < 0:
        right_score += 1
        ball_pos = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
        ball_speed_x *= -1
    if ball_pos.right > screen_width:
        left_score += 1
        ball_pos = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
        ball_speed_x *= -1

    # Check for collisions with the paddles
    if ball_pos.colliderect(left_paddle_pos) or ball_pos.colliderect(right_paddle_pos):
        ball_speed_x *= -1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddles
    pygame.draw.rect(screen, (255, 255, 255), left_paddle_pos)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle_pos)

    # Draw the ball
    pygame.draw.ellipse(screen, (255, 255, 255), ball_pos)

    # Draw the score
    left_text = font.render(str(left_score), True, (255, 255, 255))
