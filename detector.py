import cv2
from config import DANGER_ZONE, ALERT_MESSAGE, SAFE_MESSAGE

def is_inside_danger_zone(person_x, person_y):
    """
    Checks if the detected coordinates fall within the defined danger zone.
    """
    dz = DANGER_ZONE
    in_x_range = dz["x_start"] < person_x < (dz["x_start"] + dz["width"])
    in_y_range = dz["y_start"] < person_y < (dz["y_start"] + dz["height"])
    
    return in_x_range and in_y_range

def run_simulation():
    """
    Simulates a camera feed processing objects.
    """
    print("--- SafeZone AI: Monitoring System Active ---")
    
    # Mock data: coordinates (x, y) of a detected person
    # (250, 200) is inside the zone defined in config.py
    detected_person_coords = (250, 200)
    
    if is_inside_danger_zone(*detected_person_coords):
        print(ALERT_MESSAGE)
        # In a real system, this would trigger an alarm or send a notification.
    else:
        print(SAFE_MESSAGE)

if __name__ == "__main__":
    run_simulation()
