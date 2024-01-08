import pygame
import sys
import string
import pyperclip

# Initialize Pygame
pygame.init()

# Set the dimensions of the window to the current display size
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h

# Create a borderless fullscreen window
screen = pygame.display.set_mode((width, height), pygame.NOFRAME | pygame.FULLSCREEN)

# Define colors
colors = {
    "A": (255, 0, 0),       # Apple Red
    "B": (0, 0, 255),       # Blue
    "C": (255, 255, 0),     # Canary Yellow
    "D": (240, 225, 48),    # Dandelion
    "E": (0, 0, 0),         # Ebony
    "F": (34, 139, 34),     # Forest Green
    "G": (128, 128, 128),   # Grey
    "H": (210, 180, 140),   # Hazel
    "I": (75, 0, 130),      # Indigo
    "J": (165, 42, 42),     # Java (Brown)
    "K": (255, 235, 205),   # Khaki
    "L": (50, 205, 50),     # Lime Green
    "M": (255, 0, 255),     # Magenta
    "N": (165, 42, 42),     # Nut Brown
    "O": (230, 190, 255),   # Opal
    "P": (128, 0, 128),     # Purple
    "Q": (218, 112, 214),   # Quartz (Pink)
    "R": (255, 0, 0),       # Red
    "S": (192, 192, 192),   # Silver
    "T": (0, 128, 128),     # Teal
    "U": (100, 149, 237),   # Ultramarine
    "V": (238, 130, 238),   # Violet
    "W": (123, 191, 123),   # Willow Green
    "X": (0, 123, 104),     # Xanadu (a shade of green)
    "Y": (255, 255, 0),     # Yellow
    "Z": (57, 255, 20),     # Zucchini (Green)
}

# Function to draw the encoded message with a smaller grid size
def draw_encoded_message(message, grid_size):
    for i, char in enumerate(message):
        if char in string.punctuation or char == " ":
            continue
        upper_char = char.upper()
        color = colors.get(upper_char, (255, 255, 255))
        x_pos = (i % (width // grid_size)) * grid_size
        y_pos = (i // (width // grid_size)) * grid_size + 100
        pygame.draw.rect(screen, color, (x_pos, y_pos, grid_size, grid_size))
        if char.isupper():
            pygame.draw.rect(screen, (0, 0, 0), (x_pos, y_pos, grid_size, grid_size), 3)

# Text input box settings
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(50, 50, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False

grid_size = 50  # Smaller grid size

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    screen.fill((255, 255, 255))
                    draw_encoded_message(text, grid_size)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    screen.fill((255, 255, 255))
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_v and (event.mod & pygame.KMOD_CTRL):
                    try:
                        text += pyperclip.paste()
                    except Exception as e:
                        print("Error pasting text:", e)
                else:
                    text += event.unicode

    # Render the input box and current text
    txt_surface = font.render(text, True, color)
    input_box.w = max(200, txt_surface.get_width() + 10)
    screen.fill((255, 255, 255))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
