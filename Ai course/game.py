import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture (Webcam)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize Hand Detector (confidence threshold 0.8, single hand)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Game Variables
snake_points = []  # Stores the history of finger positions (body)
food_pos = [400, 400]
score = 0
length_limit = 20  # Initial length of the snake

while True:
    success, img = cap.read()
    if not success:
        print("Error: Camera feed not available.")
        break

    # Flip image horizontally for a mirror effect
    img = cv2.flip(img, 1)
    
    # Find hands and landmarks
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        
        # Get index fingertip coordinates (Landmark 8)
        index_finger = (lmList[8][0], lmList[8][1])
        snake_points.append(index_finger)

        # Control the snake's body length based on score
        current_length = length_limit + (score * 5)
        if len(snake_points) > current_length:
            snake_points.pop(0)

        # Check for food collision (Distance formula)
        distance = np.hypot(index_finger[0] - food_pos[0], index_finger[1] - food_pos[1])
        if distance < 35:
            score += 1
            # Spawn new random food within screen bounds
            food_pos = [np.random.randint(150, 1100), np.random.randint(150, 550)]

    # Draw the snake body segments
    for i in range(1, len(snake_points)):
        cv2.line(img, snake_points[i - 1], snake_points[i], (0, 255, 0), 20)

    # Draw the food item
    cv2.circle(img, tuple(food_pos), 18, (0, 0, 255), cv2.FILLED)

    # Display the current score on screen
    cv2.putText(img, f"Score: {score}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

    # Show the game window
    cv2.imshow("Hand-Controlled Snake Game", img)

    # Press 'q' to exit the game
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up resources
cap.release()
cv2.destroyAllWindows()