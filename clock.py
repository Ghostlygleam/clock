import pygame
import datetime

pygame.init()

width, height = 1000, 900
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Mickey Mouse Clock")

WHITE = (255, 255, 255)

# Loading images
clock_face = pygame.image.load("src/main-clock.png").convert_alpha()
sec_hand = pygame.image.load("src/left-hand.png").convert_alpha()   # Second hand
min_hand = pygame.image.load("src/right-hand.png").convert_alpha()  # Minute hand

# Function to rotate the image
def rotate_image(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

# Function to draw the hands
def draw_hand(image, angle, position):
    rotated_image, rect = rotate_image(image, angle, position)
    screen.blit(rotated_image, rect)

def draw_bg(center):
    screen.fill(WHITE)
    clock_face_rect = clock_face.get_rect(center=center)
    screen.blit(clock_face, clock_face_rect.topleft)

def draw_time(center):
    now = datetime.datetime.now()
    second_angle = -now.second * 6  # 360/60 = 6 degrees per second
    minute_angle = -now.minute * 6  # 360/60 = 6 degrees per minute

    draw_hand(sec_hand, second_angle, center)
    draw_hand(min_hand, minute_angle, center)

run_clock = True
# Game loop
while run_clock:
    # Calculate the new center every frame to handle window resizing
    center = (screen.get_width() // 2, screen.get_height() // 2)
    
    draw_bg(center)
    draw_time(center)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_clock = False

    pygame.display.update()
pygame.quit()
