import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 200
screen = pygame.display.set_mode((width, height))

# Define colors
colors = {
    "H": (210, 180, 140),  # Hazel for 'H' and 'h'
    "E": (0, 0, 0),        # Ebony for 'E' and 'e'
    "L": (50, 205, 50),    # Lime Green for 'L' and 'l'
    "O": (230, 190, 255),  # Opal for 'O' and 'o'
    "W": (123, 191, 123),  # Willow Green for 'W' and 'w'
    "R": (255, 0, 0),      # Red for 'R' and 'r'
    "D": (240, 225, 48)    # Dandelion for 'D' and 'd'
}

# Message to encode
message = "Hello World"
grid_size = 50

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the boxes
    for i, char in enumerate(message):
        if char != " ":
            upper_char = char.upper()  # Convert to uppercase for color mapping
            pygame.draw.rect(screen, colors[upper_char], (i * grid_size, 50, grid_size, grid_size))
            if char.isupper():
                pygame.draw.rect(screen, (0, 0, 0), (i * grid_size, 50, grid_size, grid_size), 3)  # Black border for capitalized letters

    pygame.display.flip()

pygame.quit()
sys.exit()
