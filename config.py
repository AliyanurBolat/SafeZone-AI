"""
SafeZone AI Configuration File
Defines safety parameters and detection zones.
"""

# Coordinates for the Danger Zone (x, y, width, height)
# These represent a specific area on the factory floor camera feed.
DANGER_ZONE = {
    "x_start": 100,
    "y_start": 150,
    "width": 400,
    "height": 300
}

# Detection Sensitivity
# 0.5 means the AI must be 50% sure it's a person to trigger an alert.
MIN_CONFIDENCE = 0.5

# Alert Messaging
ALERT_MESSAGE = "!!! DANGER: Unauthorized Entry into Restricted Zone !!!"
SAFE_MESSAGE = "Status: Monitoring - No violations detected."
