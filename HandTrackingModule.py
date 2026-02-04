import cv2
import mediapipe as mp
import time



class handDetector():
    """
    A class to handle hand detection and landmark tracking using MediaPipe.
    """
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame, draw = True):
        """
        Processes a frame to find hands and optionally draws the connections.
        """
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def findPosition(self, frame, handNo = 0, draw = True):
        """
        Extracts the pixel coordinates of all 21 hand landmarks.
        """
        landmarks = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                center_x, center_y = int(lm.x * w), int(lm.y * h)
                landmarks.append([id, center_x, center_y])
                if draw:
                    cv2.circle(frame, (center_x, center_y), 10, (34, 125, 55), cv2.FILLED)
        return landmarks






def main():
    """
    Example usage script to test the module in real-time.
    """
    pTime = 0
    cTime = 0
    webcam = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = webcam.read()
        img = detector.findHands(img)
        landmarks = detector.findPosition(img)
        if len(landmarks) != 0 :
            print(landmarks[8])


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 128, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()