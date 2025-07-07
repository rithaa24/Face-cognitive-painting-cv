import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import os

# Initialize variables for drawing points
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
opoints = [deque(maxlen=1024)]
brpoints = [deque(maxlen=1024)]
pippoints = [deque(maxlen=1024)]
cpoints = [deque(maxlen=1024)]
bkpoints = [deque(maxlen=1024)]
mrpoints = [deque(maxlen=1024)]
grpoints = [deque(maxlen=1024)]
prpoints = [deque(maxlen=1024)]

colorIndex = 0
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), 
    (0, 165, 255), (42, 42, 165), (147, 20, 255), (255, 255, 0),
    (0, 0, 0), (0, 0, 128), (128, 128, 128), (128, 0, 128)
]

# Initialize color indices
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0
orange_index = 0
brown_index = 0
pink_index = 0
cyan_index = 0
black_index = 0
maroon_index = 0
grey_index = 0
purple_index = 0

# Canvas setup
canvas_width, canvas_height = 1280, 720
paintWindow = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

# Color button dimensions and positions
button_width, button_height = 80, 80
button_margin = 10

buttons = {
    'CLEAR': (10, button_margin),
    'SAVE': (canvas_width - button_width - 10, button_margin),  # Move Save button to the right
    'BLUE': (100, button_margin),
    'GREEN': (190, button_margin),
    'RED': (280, button_margin),
    'YELLOW': (370, button_margin),
    'ORANGE': (460, button_margin),
    'BROWN': (550, button_margin),
    'PINK': (640, button_margin),
    'CYAN': (730, button_margin),
    'BLACK': (820, button_margin),
    'MAROON': (910, button_margin),
    'GREY': (1000, button_margin),
    'PURPLE': (1090, button_margin)
}

# Draw color buttons with styling and labels
def draw_buttons(image):
    for index, (label, (x, y)) in enumerate(buttons.items()):
        if label in ['CLEAR', 'SAVE']:
            color = (255, 255, 255)  # Set color to white for non-colored buttons
        else:
            color = colors[list(buttons.keys()).index(label) - 2]  # Use index to get color from list

        cv2.rectangle(image, (x, y), (x + button_width, y + button_height), color, -1)  # Fill with color
        cv2.rectangle(image, (x, y), (x + button_width, y + button_height), (0, 0, 0), 2)  # Border
        text_color = (0, 0, 0) if color != (0, 0, 0) else (255, 255, 255)  # Black button text is white
        cv2.putText(image, label, (x + 5, y + button_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1, cv2.LINE_AA)

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mpDraw = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible.")
    exit()

# Get the default resolution of the camera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a named window for the camera
cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Camera', width, height)  # Resize to camera resolution

# Initialize save count
save_count = 1

while True:
    # Read each frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Resize frame to match canvas size
    frame_resized = cv2.resize(frame, (canvas_width, canvas_height))

    # Flip the frame vertically
    frame_resized = cv2.flip(frame_resized, 1)
    framergb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # Post-process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * canvas_width)
                lmy = int(lm.y * canvas_height)

                landmarks.append([lmx, lmy])

            # Draw landmarks and connections
            mpDraw.draw_landmarks(frame_resized, handslms, mpHands.HAND_CONNECTIONS)

            thumb = (landmarks[4][0], landmarks[4][1])
            center = (landmarks[8][0], landmarks[8][1])

            # Check if the index finger is near the top of the screen (tool selection)
            if center[1] <= 80:
                if 10 <= center[0] <= 90:  # Clear Button
                    bpoints = [deque(maxlen=1024)]
                    gpoints = [deque(maxlen=1024)]
                    rpoints = [deque(maxlen=1024)]
                    ypoints = [deque(maxlen=1024)]
                    opoints = [deque(maxlen=1024)]
                    brpoints = [deque(maxlen=1024)]
                    pippoints = [deque(maxlen=1024)]
                    cpoints = [deque(maxlen=1024)]
                    bkpoints = [deque(maxlen=1024)]
                    mrpoints = [deque(maxlen=1024)]
                    grpoints = [deque(maxlen=1024)]
                    prpoints = [deque(maxlen=1024)]

                    blue_index = 0
                    green_index = 0
                    red_index = 0
                    yellow_index = 0
                    orange_index = 0
                    brown_index = 0
                    pink_index = 0
                    cyan_index = 0
                    black_index = 0
                    maroon_index = 0
                    grey_index = 0
                    purple_index = 0
                    paintWindow[80:, :, :] = 255
                elif canvas_width - button_width - 10 <= center[0] <= canvas_width - 10:  # Save Button
                    while True:
                        filename = f'drawing_{save_count}.png'
                        if not os.path.exists(filename):
                            break
                        save_count += 1
                    cv2.imwrite(filename, paintWindow)
                    print(f'Saved drawing to {filename}')
                elif 100 <= center[0] <= 180:  # Blue Button
                    colorIndex = 0
                elif 190 <= center[0] <= 270:  # Green Button
                    colorIndex = 1
                elif 280 <= center[0] <= 360:  # Red Button
                    colorIndex = 2
                elif 370 <= center[0] <= 450:  # Yellow Button
                    colorIndex = 3
                elif 460 <= center[0] <= 540:  # Orange Button
                    colorIndex = 4
                elif 550 <= center[0] <= 630:  # Brown Button
                    colorIndex = 5
                elif 640 <= center[0] <= 720:  # Pink Button
                    colorIndex = 6
                elif 730 <= center[0] <= 810:  # Cyan Button
                    colorIndex = 7
                elif 820 <= center[0] <= 900:  # Black Button
                    colorIndex = 8
                elif 910 <= center[0] <= 990:  # Maroon Button
                    colorIndex = 9
                elif 1000 <= center[0] <= 1080:  # Grey Button
                    colorIndex = 10
                elif 1090 <= center[0] <= 1170:  # Purple Button
                    colorIndex = 11
            else:
                if thumb[1] <= center[1]:
                    if colorIndex == 0:
                        bpoints[blue_index].appendleft(center)
                    elif colorIndex == 1:
                        gpoints[green_index].appendleft(center)
                    elif colorIndex == 2:
                        rpoints[red_index].appendleft(center)
                    elif colorIndex == 3:
                        ypoints[yellow_index].appendleft(center)
                    elif colorIndex == 4:
                        opoints[orange_index].appendleft(center)
                    elif colorIndex == 5:
                        brpoints[brown_index].appendleft(center)
                    elif colorIndex == 6:
                        pippoints[pink_index].appendleft(center)
                    elif colorIndex == 7:
                        cpoints[cyan_index].appendleft(center)
                    elif colorIndex == 8:
                        bkpoints[black_index].appendleft(center)
                    elif colorIndex == 9:
                        mrpoints[maroon_index].appendleft(center)
                    elif colorIndex == 10:
                        grpoints[grey_index].appendleft(center)
                    elif colorIndex == 11:
                        prpoints[purple_index].appendleft(center)

    # Draw points on the canvas
    points = [bpoints[blue_index], gpoints[green_index], rpoints[red_index], ypoints[yellow_index],
              opoints[orange_index], brpoints[brown_index], pippoints[pink_index], cpoints[cyan_index],
              bkpoints[black_index], mrpoints[maroon_index], grpoints[grey_index], prpoints[purple_index]]

    for point_set, color in zip(points, colors):
        for i in range(1, len(point_set)):
            if point_set[i - 1] is None or point_set[i] is None:
                continue
            cv2.line(paintWindow, point_set[i - 1], point_set[i], color, 2)  # Pen thickness reduced to 2

    # Overlay drawing on the camera feed
    frame_with_buttons = frame_resized.copy()
    frame_with_buttons = cv2.addWeighted(frame_with_buttons, 1.0, paintWindow, 0.5, 0)  # Blend image with some transparency

    # Draw buttons on the frame
    draw_buttons(frame_with_buttons)

    # Show the frames
    cv2.imshow('Camera', frame_with_buttons)
    cv2.imshow('Painting', paintWindow)

    # Exit the application when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
