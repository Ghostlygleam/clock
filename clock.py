import pygame
import datetime
import math

pygame.init()

width, height = 600, 600
center = (width // 2, height // 2)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Mickey Mouse Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Loading images
clock_face = pygame.image.load("src/main-clock.png").convert_alpha()
sec_hand = pygame.image.load("src/left-hand.png").convert_alpha()   # Second hand
min_hand = pygame.image.load("src/right-hand.png").convert_alpha()  # Minute hand

# Measuring image sizes
clock_face_rect = clock_face.get_rect(center=center)
right_hand_rect = sec_hand.get_rect(center=center)
left_hand_rect = min_hand.get_rect(center=center)

# Function to rotate the image
def rotate_image(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

# Function to draw the hands
def draw_hand(image, angle, position):
    rotated_image, rect = rotate_image(image, angle, position)
    screen.blit(rotated_image, rect)

def draw_bg():
    screen.fill(WHITE)
    screen.blit(clock_face, clock_face_rect.topleft)

def draw_time():
    now = datetime.datetime.now()
    second_angle = -now.second * 6  # 360/60 = 6 degrees per second
    minute_angle = -now.minute * 6  # 360/60 = 6 degrees per minute

    # Adjusting the initial angle for both hands to 12 o'clock
    second_angle -= 90  # Default angle 0 degrees is right, -90 degrees is up
    minute_angle -= 90

    draw_hand(sec_hand, second_angle, center)
    draw_hand(min_hand, minute_angle, center)

run_clock = True
# Game loop
while run_clock:
    draw_bg()
    draw_time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_clock = False

    pygame.display.update()
pygame.quit()
