import json
import os

# Check if file exists
if os.path.isfile("info.json"):
    with open("info.json", "r") as f:
        data = json.load(f)
    # Set variables to settings
    speed = data["speed"]
    radius = data["radius"]
    crosshair_enabled = data["crosshair_enabled"]
else:
    # Set default values
    speed = 10
    radius = 20
    crosshair_enabled = False