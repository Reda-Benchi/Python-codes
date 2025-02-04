# My first program

# This bot will be used to "complete a quest" in World of Warcraft
# where a frequency is required to click with the mouse pointer over a longer period of time

import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Define the key that will toggle the clicking behavior (in this case, the 'T' key)
TOGGLE_KEY = KeyCode(char="t")

# Initialize a flag that tracks whether the bot should be clicking or not
clicking = False

# Create a mouse controller object to simulate mouse actions
mouse = Controller()

# Function to simulate the mouse clicks while 'clicking' is True
def clicker():
    while True:
        # If clicking is enabled, simulate a left-click every 0.05 seconds
        if clicking:
            mouse.click(Button.left, 1)  # Left-click with 1 count
        time.sleep(0.05)  # Wait for 0.05 seconds before checking again

# Function to handle key press events and toggle the clicking behavior
def toggle_event(key):
    if key == TOGGLE_KEY:  # Check if the pressed key is the toggle key (T)
        global clicking
        clicking = not clicking  # Toggle the 'clicking' flag (True or False)

# Start the clicking function in a separate thread so it runs in the background
click_thread = threading.Thread(target=clicker)
click_thread.start()

# Start listening for key presses
with Listener(on_press=toggle_event) as listener:
    listener.join()  # Keep the listener running until the program is stopped
