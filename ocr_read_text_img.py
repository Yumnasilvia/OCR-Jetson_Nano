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

# Load gambar
image_path = 'image.png'  # Ganti dengan path gambar Anda
image = cv2.imread(image_path)

# Preprocessing gambar
preprocessed_image = preprocess_image(image)

# OCR pada gambar
text = recognize_text(preprocessed_image)
print("Text pada gambar:", text)

# Tampilkan gambar
cv2.imshow('Original Image', image)
cv2.imshow('Preprocessed Image', preprocessed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
