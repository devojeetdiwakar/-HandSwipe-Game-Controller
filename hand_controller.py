import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Store previous finger position
prev_x, prev_y = 0, 0
swipe_threshold = 40  # Minimum movement to register a swipe
last_swipe_time = 0
cooldown = 0.5  # Cooldown in seconds between gestures

print("Starting Hand Gesture Game Controller. Press ESC to exit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe
    result = hands.process(rgb_frame)

    # Draw landmarks and detect gestures
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the index finger tip coordinates
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = frame.shape
            cx, cy = int(index_tip.x * w), int(index_tip.y * h)

            # Draw a circle at the fingertip
            cv2.circle(frame, (cx, cy), 12, (255, 0, 255), cv2.FILLED)

            # Detect swipe direction
            dx = cx - prev_x
            dy = cy - prev_y
            current_time = time.time()

            if current_time - last_swipe_time > cooldown:
                if abs(dx) > swipe_threshold:
                    if dx > 0:
                        print("Swipe Right → (Sends ← key due to mirroring)")
                        pyautogui.press('left')  # mirrored
                    else:
                        print("Swipe Left ← (Sends → key due to mirroring)")
                        pyautogui.press('right')
                    last_swipe_time = current_time

                elif abs(dy) > swipe_threshold:
                    if dy > 0:
                        print("Swipe Down ↓")
                        pyautogui.press('down')
                    else:
                        print("Swipe Up ↑")
                        pyautogui.press('up')
                    last_swipe_time = current_time

            # Update previous position
            prev_x, prev_y = cx, cy

    # Show the frame
    cv2.imshow("Hand Gesture Game Controller", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
