import face_recognition
import os
import pickle

# === CONFIG ===
dataset_path = "faces"             # Folder with 100–200 images
output_file = "encodings.pkl"      # Where to save face encodings

# === STORAGE ===
all_encodings = []
all_names = []

# === PROCESS EACH IMAGE ===
for filename in os.listdir(dataset_path):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    path = os.path.join(dataset_path, filename)
    name = os.path.splitext(filename)[0]  # Use filename as name

    print(f"Processing {filename} as '{name}'...")

    try:
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            all_encodings.append(encodings[0])
            all_names.append(name)
        else:
            print(f"⚠️  No face found in {filename}")
    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")

# === SAVE TO FILE ===
data = {
    "encodings": all_encodings,
    "names": all_names
}

with open(output_file, "wb") as f:
    pickle.dump(data, f)

print(f"\n✅ Encodings saved to '{output_file}'")
print(f"🧠 People saved: {len(all_names)}")
