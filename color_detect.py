import cv2
import pyautogui
import numpy as np
import PySimpleGUI as sg
layout = [        [
            sg.TabGroup(
                [
                    [
                        sg.Tab(
                            "Settings",
                            [
                                [sg.Text("Hold SHIFT to detect red color")],
                                [
                                    sg.Text(
                                        "Smoothing (lower for lower smooth also speed)"
                                    ),
                                    sg.Slider(
                                        range=(1, 10),
                                        default_value=10,
                                        orientation="h",
                                        key="-SPEED-",
                                        enable_events=True,
                                    ),
                                ],
                                [
                                    sg.Text("Detection Radius (pixels)"),
                                    sg.Slider(
                                        range=(5, 500),
                                        default_value=500,
                                        orientation="h",
                                        key="-RADIUS-",
                                        enable_events=True,
                                    ),
                                ],
                            ],
                            pad=(15, 15),
                            border_width=1,
                        ),
                        sg.Tab(
                            "Click Bot",
                            [
                                [
                                    sg.Checkbox(
                                        "Click on red",
                                        default=False,
                                        key="-CLICK_ON_RED-",
                                        font=("Helvetica", 12),
                                    )
                                ]
                            ],
                            pad=(15, 15),
                            border_width=1,
                        ),
                        sg.Tab(
                            "Crosshair",
                            [
                                [
                                    sg.Text(
                                        "Note this code does absolutely nothing if you have suggestions send in discord"
                                    ),
                                ],
                                [
                                    sg.Checkbox(
                                        "Toggle crosshair",
                                        default=False,
                                        key="-TOGGLE_CROSSHAIR-",
                                        font=("Helvetica", 12),
                                    )
                                ],
                            ],
                            pad=(15, 15),
                            border_width=1,
                        ),
                        sg.Tab(
                            "Info and contacts",
                            [
                                [
                                    sg.Text(
                                        "Themes made by graphics designer from team SHXDOW",
                                        font=("Helvetica", 12),
                                    )
                                ],
                                [sg.Text("Made by drexxy", font=("Helvetica", 12))],
                            ],
                            pad=(15, 15),
                            border_width=1,
                        ),
                        sg.Tab(
                            "Extra",
                            [
                                [
                                    sg.Text(
                                        "here are no extras yet",
                                        font=("Helvetica", 12),
                                    )
                                ],
                                [
                                    sg.Text(
                                        "Discord is discord.gg/R7yNAG9RFJ",
                                        font=("Helvetica", 12),
                                    )
                                ],
                            ],
                            pad=(15, 15),
                            border_width=1,
                        ),
                    ]
                ],
                expand_x=True,
                tab_location="left",
                tab_background_color="#3f6289",
                tab_border_width=3,
                font=("Helvetica", 12),
                size=500,
                pad=(50, 50),
            )
        ]
    ]
def detect_color(speed, radius):
    # Take a screenshot and convert to numpy array
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Define color thresholds for red (larger scale)
    lower_red = np.array([0, 0, 150])
    upper_red = np.array([100, 100, 255])

    # Create mask for only red pixels
    mask = cv2.inRange(screenshot, lower_red, upper_red)

    # Apply smoothing to mask
    mask = cv2.blur(mask, (speed, speed))

    # Find coordinates of first red pixel within detection radius
    x, y = pyautogui.position()
    x_min = max(x - radius, 0)
    x_max = min(x + radius, pyautogui.size().width)
    y_min = max(y - radius, 0)
    y_max = min(y + radius, pyautogui.size().height)
    y, x = np.where(mask[y_min:y_max, x_min:x_max] == 255)
    if len(y) > 0 and len(x) > 0:
        x_avg = int(np.mean(x)) + x_min
        y_avg = int(np.mean(y)) + y_min

        # Get color of detected pixel
        pixel_color = screenshot[y_avg, x_avg]

        # Check if color is within specified range of red
        if 100 <= pixel_color[0] <= 255 and 0 <= pixel_color[1] <= 100 and 25 <= pixel_color[2] <= 150:
            return x_avg, y_avg, pixel_color

    return None, None, None

