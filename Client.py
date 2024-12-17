from Regular_Button import Regular_Button
from Control_Button import Control_Button
from Click_Handler import Click_Handler

up_button = Control_Button("up", 5, 6)
down_button = Control_Button("down", 5, 4)
left_button = Control_Button("left", 4, 5)
right_button = Control_Button("right", 6, 5)

button1 = Regular_Button("Button 1", 1, 1)
button2 = Regular_Button("Button 2", 2, 2)
button3 = Regular_Button("Button 3", 3, 3)

click_handler = Click_Handler()
click_handler.add_button(up_button)
click_handler.add_button(down_button)
click_handler.add_button(left_button)
click_handler.add_button(right_button)
click_handler.add_button(button1)
click_handler.add_button(button2)
click_handler.add_button(button3)

click_handler.click(5, 6)
print("--------------------------------")
click_handler.click(6, 5)
print("--------------------------------")
click_handler.click(5, 4)
print("--------------------------------")
click_handler.click(4, 5)