import cv2
print("CUDA Support in OpenCV:", cv2.cuda.getCudaEnabledDeviceCount() > 0)
