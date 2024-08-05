import cv2
import pytesseract
import numpy as np

# Fungsi untuk melakukan preprocessing gambar menggunakan GPU
def preprocess_image(image):
    gpu_frame = cv2.cuda_GpuMat()
    gpu_frame.upload(image)
    
    gpu_gray = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2GRAY)
    
    # Menggunakan Bilateral Filter sebagai pengganti Gaussian Blur
    gpu_blurred = cv2.cuda.bilateralFilter(gpu_gray, 15, 75, 75)
    
    # Menggunakan Thresholding
    _, gpu_thresh = cv2.cuda.threshold(gpu_blurred, 150, 255, cv2.THRESH_BINARY)
    
    # Menggunakan Erosion dan Dilation dengan filter2D
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    gpu_kernel = cv2.cuda_GpuMat()
    gpu_kernel.upload(kernel)

    gpu_eroded = cv2.cuda.createMorphologyFilter(cv2.MORPH_ERODE, cv2.CV_8UC1, kernel).apply(gpu_thresh)
    gpu_dilated = cv2.cuda.createMorphologyFilter(cv2.MORPH_DILATE, cv2.CV_8UC1, kernel).apply(gpu_eroded)
    
    # Download hasil ke CPU
    preprocessed_image = gpu_dilated.download()
    return preprocessed_image

# Fungsi untuk melakukan OCR dengan bahasa Indonesia
def recognize_text(image):
    text = pytesseract.image_to_string(image, lang='ind')
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

    # Preprocessing frame menggunakan GPU
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
