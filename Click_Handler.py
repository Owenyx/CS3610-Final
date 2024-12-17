from Control_Button import Control_Button
from Subscriber import Subscriber

# Subject that is observed
class Click_Handler:
    def __init__(self):
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def remove_button(self, button):
        self.buttons.remove(button)

    # Click on a button at the given coordinates
    # If the button is a control button, notify all subscriber buttons of the direction pressed
    def click(self, x, y):
        for button in self.buttons:
            if button.x == x and button.y == y:
                button.click()
                if isinstance(button, Control_Button):
                    direction = button.text
                    self.notify(direction)

    # Notify all subscriber buttons of the direction pressed
    def notify(self, direction):
        for button in self.buttons:
            if isinstance(button, Subscriber):
                button.update(direction)

