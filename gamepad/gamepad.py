import pygame
import pyautogui

pygame.init()

# Initialize the gamepad
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()


# Set up the key mapping
KEY_MAP = {
    pygame.JOYBUTTONUP: {
        0: 'enter',  # Release "Enter" key on button up
        # Add more button release mappings here
    },
    pygame.JOYBUTTONDOWN: {
        0: 'enter',  # Press "Enter" key on A button down
        # Add more button press mappings here
    },
}

while True:
    for event in pygame.event.get():
        if event.type in KEY_MAP:
            button = KEY_MAP[event.type].get(event.button)
            if button:
                if event.type == pygame.JOYBUTTONDOWN:
                    pyautogui.press(button)
                else:  # pygame.JOYBUTTONUP
                    pyautogui.keyUp(button)