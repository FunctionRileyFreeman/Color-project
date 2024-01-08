import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 300
screen = pygame.display.set_mode((width, height))

# Define colors
colors = {
    "H": (210, 180, 140),   # Hazel
    "E": (0, 0, 0),         # Ebony
    "L": (50, 205, 50),     # Lime Green
    "O": (230, 190, 255),   # Opal
    "W": (123, 191, 123),   # Willow Green
    "R": (255, 0, 0),       # Red
    "D": (240, 225, 48),    # Dandelion
    # Additional colors for remaining letters (same logic applied)
    "A": (255, 0, 0),       # Apple Red
    "B": (0, 0, 255),       # Blue
    "C": (255, 255, 0),     # Canary Yellow
    "F": (34, 139, 34),     # Forest Green
    "G": (128, 128, 128),   # Grey
    "I": (75, 0, 130),      # Indigo
    "J": (165, 42, 42),     # Java (Brown)
    "K": (255, 235, 205),   # Khaki
    "M": (255, 0, 255),     # Magenta
    "N": (165, 42, 42),     # Nut Brown
    "P": (128, 0, 128),     # Purple
    "Q": (218, 112, 214),   # Quartz (Pink)
    "S": (192, 192, 192),   # Silver
    "T": (0, 128, 128),     # Teal
    "U": (100, 149, 237),   # Ultramarine
    "V": (238, 130, 238),   # Violet
    "X": (0, 123, 104),     # Xanadu (a shade of green)
    "Y": (255, 255, 0),     # Yellow
    "Z": (57, 255, 20),     # Zucchini (Green)
}

# Function to draw the encoded message
def draw_encoded_message(message, grid_size):
    for i, char in enumerate(message):
        if char != " ":
            upper_char = char.upper()  # Convert to uppercase for color mapping
            color = colors.get(upper_char, (255, 255, 255))  # Default to white if color not found
            pygame.draw.rect(screen, color, (i * grid_size, 100, grid_size, grid_size))
            if char.isupper():
                pygame.draw.rect(screen, (0, 0, 0), (i * grid_size, 100, grid_size, grid_size), 3)

# Text input box settings
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(50, 50, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    screen.fill((255, 255, 255))  # Clear the screen
                    draw_encoded_message(text, 50)  # Draw the message in cipher
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Render the input box and current text
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
