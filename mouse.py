import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0

while True:
    _, image = cap.read()
    image_height, image_width, _= image.shape
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    res = capture_hands.process(rgb_image)
    hands = res.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_height)
                y = int(lm.y * image_height)
                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)
                    # cv2.circle(image,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    # cv2.circle(image, (x,y), 10, (0,255,255))
        dist = y2 -y1
        if(dist < 30):
            pyautogui.click()
    cv2.imshow('Hand movement', image)
    key = cv2.waitKey(1)
    if key == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
