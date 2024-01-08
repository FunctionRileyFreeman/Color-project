import pygame
import sys
import pyperclip
import string

# Initialize Pygame
pygame.init()

# Set the dimensions of the window to the current display size
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h

# Create a borderless fullscreen window
screen = pygame.display.set_mode((width, height), pygame.NOFRAME | pygame.FULLSCREEN)

# Define colors
colors = {
    "A": (255, 0, 0),  # Apple Red
    "B": (0, 0, 255),  # Blue
    "C": (255, 255, 0),  # Canary Yellow
    "D": (240, 225, 48),  # Dandelion
    "E": (0, 0, 0),  # Ebony
    "F": (34, 139, 34),  # Forest Green
    "G": (128, 128, 128),  # Grey
    "H": (210, 180, 140),  # Hazel
    "I": (75, 0, 130),  # Indigo
    "J": (165, 42, 42),  # Java (Brown)
    "K": (255, 235, 205),  # Khaki
    "L": (50, 205, 50),  # Lime Green
    "M": (255, 0, 255),  # Magenta
    "N": (165, 42, 42),  # Nut Brown
    "O": (230, 190, 255),  # Opal
    "P": (128, 0, 128),  # Purple
    "Q": (218, 112, 214),  # Quartz (Pink)
    "R": (255, 0, 0),  # Red
    "S": (192, 192, 192),  # Silver
    "T": (0, 128, 128),  # Teal
    "U": (100, 149, 237),  # Ultramarine
    "V": (238, 130, 238),  # Violet
    "W": (123, 191, 123),  # Willow Green
    "X": (0, 123, 104),  # Xanadu (a shade of green)
    "Y": (255, 255, 0),  # Yellow
    "Z": (57, 255, 20),  # Zucchini (Green)
}


# Function to draw the encoded message with custom designs for ",", "-", and "#"
def draw_encoded_message(message, grid_size):
    for i, char in enumerate(message):
        upper_char = char.upper()
        color = colors.get(upper_char, (255, 255, 255))
        x_pos = (i % (width // grid_size)) * grid_size
        y_pos = (i // (width // grid_size)) * grid_size + 100

        # Draw clear backdrop square
        pygame.draw.rect(screen, (255, 255, 255), (x_pos, y_pos, grid_size, grid_size))

        # Draw custom designs for ",", "-", and "#"
        if char == ",":
            pygame.draw.arc(screen, (0, 0, 0), (x_pos, y_pos + grid_size - 15, grid_size, 15), 0, 3.14159265359, 2)
        elif char == "-":
            pygame.draw.line(screen, (0, 0, 0), (x_pos, y_pos + grid_size // 2),
                             (x_pos + grid_size, y_pos + grid_size // 2), 2)
        elif char == "#":
            line_thickness = 2
            pygame.draw.line(screen, (0, 0, 0), (x_pos + line_thickness, y_pos + line_thickness),
                             (x_pos + grid_size - line_thickness, y_pos + line_thickness), line_thickness)
            pygame.draw.line(screen, (0, 0, 0), (x_pos + line_thickness, y_pos + grid_size // 4),
                             (x_pos + grid_size - line_thickness, y_pos + grid_size // 4), line_thickness)
            pygame.draw.line(screen, (0, 0, 0), (x_pos + line_thickness, y_pos + grid_size // 2),
                             (x_pos + grid_size - line_thickness, y_pos + grid_size // 2), line_thickness)
            pygame.draw.line(screen, (0, 0, 0), (x_pos + line_thickness, y_pos + grid_size // 4 * 3),
                             (x_pos + grid_size - line_thickness, y_pos + grid_size // 4 * 3), line_thickness)

        # Draw the design for "!"
        elif char == "!":
            pygame.draw.line(screen, (0, 0, 0), (x_pos + grid_size // 2, y_pos + grid_size // 2),
                             (x_pos + grid_size // 2, y_pos + grid_size - 2), 2)

        # Draw the design for "."
        elif char == ".":
            pygame.draw.circle(screen, (0, 0, 0), (x_pos + grid_size // 2, y_pos + grid_size - 2), 2)

        # Draw the letter in the square
        elif char != " " and char not in string.punctuation:
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
input_completed = True  # Flag to control input state

grid_size = 20  # Smaller grid size

# Clear the screen once at the beginning
screen.fill((255, 255, 255))
pygame.display.flip()

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos) and input_completed:
                active = True  # Set the input box to active when clicked
                input_completed = False
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    if text:
                        draw_encoded_message(text, grid_size)
                        pygame.display.flip()
                    # Don't clear the text when Enter is pressed, but deactivate the input box
                    active = False
                    input_completed = True
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

    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
