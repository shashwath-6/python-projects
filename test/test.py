import face_recognition
import cv2
import pickle
import numpy as np

# === Load encodings ===
with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)
known_encodings = data["encodings"]
known_names = data["names"]

# === Start webcam ===
video_capture = cv2.VideoCapture(0)

print("🎥 Starting camera. Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Unknown"
        confidence_text = ""

        # Compare face to known encodings
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.6)

        if True in matches:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]
                confidence = 1 - face_distances[best_match_index]
                confidence_text = f"{name} ({confidence:.2f})"
        else:
            confidence_text = "Unknown"

        # Scale back up face locations since frame was scaled to 1/4
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, confidence_text, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 0, 0), 1)

    # Show the result
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
