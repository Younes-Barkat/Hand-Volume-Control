import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities 
from pynput.keyboard import Controller, Key

############################
wCam, hCam = 640, 480 # --- Camera Settings ---
############################

# --- Audio Setup via PyCaw ---
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
volRange = volume.GetVolumeRange() # Returns (minVol, maxVol, volumeStep)
minVol = volRange[0]
maxVol = volRange[1]

webcam = cv2.VideoCapture(0)
webcam.set(3, wCam)
webcam.set(4, hCam)

# --- Initialization ---
pTime = 0
detector = htm.handDetector(detectionCon=0.75) # Higher confidence for better stability
smoothness = 8 # Higher value = slower, more professional volume transitions
prevVol = 0

keyboard = Controller()
lastKeyPress = 0

while True:
    success, frame = webcam.read()
    # 1. Detect Hands and Landmarks
    frame = detector.findHands(frame)
    landmarks = detector.findPosition(frame, draw=False)

    if len(landmarks) != 0:
        # Get coordinates for Thumb Tip (4) and Index Tip (8)
        thumb_x, thumb_y = landmarks[4][1], landmarks[4][2]
        index_x, index_y = landmarks[8][1], landmarks[8][2]
        center_x, center_y = (thumb_x + index_x) // 2, (thumb_y + index_y) // 2
        # Drawing the volume controller HUD on the hand
        cv2.circle(frame, (thumb_x, thumb_y), 10, (34, 230, 0), cv2.FILLED)
        cv2.circle(frame, (index_x, index_y), 10, (34, 230, 0), cv2.FILLED)
        cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (34, 230, 0), 3)
        cv2.circle(frame, (center_x, center_y), 10, (34, 230, 0), cv2.FILLED)
        # Calculate the distance between fingers for volume scaling
        finger_distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

        # 2. Gesture Logic: Fist Detection for Mute
        # Compares finger tips (ID 8,12,16,20) to knuckles (6,10,14,18)
        if (landmarks[8][2] > landmarks[6][2] and
                landmarks[12][2] > landmarks[10][2] and
                landmarks[16][2] > landmarks[14][2] and
                landmarks[20][2] > landmarks[18][2]):

            volume.SetMute(1, None)
            cv2.putText(frame, "MUTED", (250, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        else:
            volume.SetMute(0, None)
            # Map finger distance (50-200px) to system volume range (dB)
            vol = np.interp(finger_distance, [50, 200], [minVol, maxVol])
            # Apply smoothing and validity check to prevent 'shaking' volume
            if finger_distance > 25:
                diff = vol - prevVol
                if abs(diff) > 0.3:
                    currentVol = prevVol + (diff / smoothness)
                    volume.SetMasterVolumeLevel(currentVol, None)
                    prevVol = currentVol
                    # Trigger the native Windows volume overlay for visual confirmation
                    # We double-tap Mute quickly to show the UI without changing state
                    currentTime = time.time()
                    if currentTime - lastKeyPress > 0.8:
                        # Quick mute/unmute to show overlay without changing level
                        keyboard.press(Key.media_volume_mute)
                        keyboard.release(Key.media_volume_mute)
                        time.sleep(0.01)
                        keyboard.press(Key.media_volume_mute)
                        keyboard.release(Key.media_volume_mute)
                        lastKeyPress = currentTime
        # Visual indicator for 0% volume (fingers touching)
        if finger_distance < 50:
            cv2.circle(frame, (center_x, center_y), 10, (0, 255, 255), cv2.FILLED)
    else:
        # Prompt user if hand leaves the camera frame
        cv2.putText(frame, "No Hand Detected", (200, 240), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    # 3. FPS Performance Display
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow("Hand Volume Control", frame)
    
    # Safely close the app with 'Q' or by clicking the 'X' button
    key = cv2.waitKey(1)
    if key == ord('q') or cv2.getWindowProperty("Hand Volume Control", cv2.WND_PROP_VISIBLE) < 1:
        break

webcam.release()
cv2.destroyAllWindows()