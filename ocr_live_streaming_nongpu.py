import cv2
import pytesseract

# Fungsi untuk melakukan preprocessing gambar
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Thresholding
    return binary

# Fungsi untuk melakukan OCR
def recognize_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Buka video stream dari kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak dapat membuka kamera.")
    exit()

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Tidak dapat membaca frame dari kamera.")
        break

    # Preprocessing frame
    preprocessed_frame = preprocess_image(frame)

    # OCR pada frame
    text = recognize_text(preprocessed_frame)
    print("Text pada frame:", text)

    # Tampilkan frame asli dan frame yang telah dipreproses
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Preprocessed Frame', preprocessed_frame)

    # Berhenti jika pengguna menekan 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release kamera dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()
