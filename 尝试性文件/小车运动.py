import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Car Game")

# Set the background color of the window
background_color = (255, 255, 255)

# Set the position of the car
car_position = [200, 200]

# Set the speed of the car
car_speed = 0.1

# Load the car image
car_image = pygame.image.load("car.png")

# Display the animation of the car's movement
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_position[0] -= car_speed
    if keys[pygame.K_RIGHT]:
        car_position[0] += car_speed
    if keys[pygame.K_UP]:
        car_position[1] -= car_speed
    if keys[pygame.K_DOWN]:
        car_position[1] += car_speed

    screen.fill(background_color)

    screen.blit(car_image, car_position)

    pygame.display.update()

