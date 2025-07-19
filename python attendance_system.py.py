import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import dlib
import time

# Initialize webcam video capture with optimized settings
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Load known face images and encodings
gaurav_image = face_recognition.load_image_file("photos/gaurav.jpg")
gaurav_encoding = face_recognition.face_encodings(gaurav_image)[0]

harsh_image = face_recognition.load_image_file("photos/harsh.jpg")
harsh_encoding = face_recognition.face_encodings(harsh_image)[0]

shreya_image = face_recognition.load_image_file("photos/shreya.jpg")
shreya_encoding = face_recognition.face_encodings(shreya_image)[0]

suruchi_mam_image = face_recognition.load_image_file("photos/suruchi_mam.jpg")
suruchi_mam_encoding = face_recognition.face_encodings(suruchi_mam_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    gaurav_encoding,
    harsh_encoding,
    shreya_encoding,
    suruchi_mam_encoding
]

known_faces_names = [
    "gaurav",
    "harsh",
    "shreya",
    "suruchi_mam"
]

# Initialize student list (attendance)
students = known_faces_names.copy()

# Variables for face recognition
face_locations = []
face_encodings = []
face_names = []
s = True

# Set up Dlib face detector and predictor for eye and head movement detection
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def detect_blinks(landmarks):
    left_eye = landmarks[36:42]
    right_eye = landmarks[42:48]

    def eye_aspect_ratio(eye):
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        return (A + B) / (2.0 * C)

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    return (left_ear + right_ear) / 2.0 < 0.2

def detect_head_movement(landmarks, prev_position):
    # Calculate the current head position based on landmarks (e.g., nose)
    current_position = np.mean(landmarks[27:36], axis=0)
    if prev_position is not None:
        movement = np.linalg.norm(current_position - prev_position)
        return movement > 2.0, current_position
    return False, current_position

# Get current date for the attendance file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create/open a CSV file for the attendance list
with open(current_date + '.csv', 'w+', newline='') as f:
    lnwriter = csv.writer(f)
    prev_position = None

    while True:
        # Capture a frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect face locations using the full frame size for better accuracy
        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) > 0:
            try:
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                face_names = []

                for face_encoding, location in zip(face_encodings, face_locations):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_faces_names[best_match_index]

                        (top, right, bottom, left) = location
                        dlib_rect = dlib.rectangle(left, top, right, bottom)
                        landmarks = predictor(gray, dlib_rect)
                        landmarks = np.array([(p.x, p.y) for p in landmarks.parts()])

                        blink_detected = detect_blinks(landmarks)
                        movement_detected, prev_position = detect_head_movement(landmarks, prev_position)

                        if blink_detected and movement_detected:
                            face_names.append(name)

                            if name in students:
                                students.remove(name)
                                print(f"Marked {name} as present")
                                current_time = datetime.now().strftime("%H-%M-%S")
                                lnwriter.writerow([name, current_time])
                        else:
                            print("Live movement or blink not detected, possibly a spoof attempt")
                            face_names.append("Unknown")

            except Exception as e:
                print(f"Error in face encoding: {e}")

        # Display the video frame with face recognition
        cv2.imshow("Anti-Proxy Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
