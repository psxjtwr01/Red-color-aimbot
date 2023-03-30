from color_detect import *
import cv2
import mouse
import PySimpleGUI as sg
import keyboard
import time
# Set up window
sg.theme_text_color("white")
sg.theme_input_text_color("white")
sg.theme_button_color(("white", "#3f6289"))
sg.theme_slider_color("#3f6289")
sg.set_options(font=("Helvetica", 11))

# Load settings from JSON file

# Create GUI layout
print("Loading settings...")
time.sleep(1)
print("Settings loaded.")
time.sleep(1)
print("Creating layout...")
time.sleep(1)
window = sg.Window(
    "Color Detector",
    layout,
    keep_on_top=True,
    alpha_channel=0.9,
    auto_size_buttons=True,
    auto_size_text=True,
)
print("Layout created.")
time.sleep(2)
print("\03 WELCOME TO AIMBOT \03")
time.sleep(1)
sg.theme("lightgray")
window.set_icon("./images.png")
speed = 10
radius = 500
while True:
    event, values = window.read(timeout=0)

    # Check if SHIFT is pressed
    if keyboard.is_pressed("shift"):
        # Detect color and move mouse to coordinates
        x, y, pixel_color = detect_color(speed, radius)

        if x is not None and y is not None:
            pyautogui.moveTo(x, y)
            # pyautogui.dragTo(x=x,y=y,duration=0.1)

            # Check if user has enabled click on red
            if values["-CLICK_ON_RED-"]:
                mouse.click()

    if event == "-SPEED-":
        speed = int(values["-SPEED-"])

    if event == "-RADIUS-":
        radius = int(values["-RADIUS-"])

    if event == "-CLICK_ON_RED-":
        click_on_red = values["-CLICK_ON_RED-"]

    if event == "-CROSSHAIR-":
        crosshair_enabled = values["-CROSSHAIR-"]

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

cv2.destroyAllWindows()
