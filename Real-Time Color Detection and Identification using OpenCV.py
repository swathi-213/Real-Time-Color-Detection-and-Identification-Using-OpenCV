import cv2


def get_color_name(h, s, v):
    if v < 50:
        return "Black"
    if v > 200 and s < 30:
        return "White"
    if s < 40 and 50 <= v <= 200:
        return "Gray"

    # Extended color mapping
    if 0 <= h <= 10:
        if s > 100 and v > 100:
            return "Red"
        else:
            return "Maroon"
    if 11 <= h <= 20:
        if s > 150:
            return "Orange"
        else:
            return "Brown"
    if 21 <= h <= 30:
        return "Yellow"
    if 31 <= h <= 45:
        return "Olive"
    if 46 <= h <= 70:
        return "Green"
    if 71 <= h <= 85:
        return "Dark Green"
    if 86 <= h <= 95:
        return "Cyan"
    if 96 <= h <= 110:
        return "Teal"
    if 111 <= h <= 130:
        return "Blue"
    if 131 <= h <= 145:
        return "Light Blue"
    if 146 <= h <= 160:
        return "Purple"
    if 161 <= h <= 170:
        return "Pink"

    # Skin tone (more accurate range)
    if 5 <= h <= 25 and 40 <= s <= 130 and 100 <= v <= 255:
        return "Skin"

    # Fallback
    return "Unknown"

# Start camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access camera.")
    exit()

prev_color = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    h_frame, w_frame, _ = frame.shape
    center_x, center_y = w_frame // 2, h_frame // 2

    # Convert to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = hsv_frame[center_y, center_x]

    # Get color name
    color_name = get_color_name(h, s, v)

    # Draw box
    cv2.rectangle(frame, (center_x - 5, center_y - 5), (center_x + 5, center_y + 5), (255, 255, 255), 2)
    cv2.putText(frame, f"{color_name}", (center_x - 70, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Color Detector", frame)

    # Break loop with ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
