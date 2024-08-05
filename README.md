
# OCR-Jetson_Nano

Installation tutorial and writing detection program using OCR. Optical Character Recognition (OCR) is a technology that extracts text from images. This technology scans GIF, JPG, PNG, and TIFF images.


## Tutorial for installing OCR on Jetson Nano
1. Install opencv-cuda
- Uninstall Existing OpenCV:
``` bash
pip3 uninstall opencv-python opencv-python-headless opencv-contrib-python
```
- Download OpenCV and OpenCV Contrib source code:
``` bash
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```
- Create a build directory and go into it:
``` bash
cd opencv
mkdir build
cd build
```
- Configure a build with CUDA support:
``` bash
cmake -D CMAKE_BUILD_TYPE=Release \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D WITH_CUDA=ON \
      -D ENABLE_FAST_MATH=1 \
      -D CUDA_FAST_MATH=1 \
      -D WITH_CUBLAS=1 \
      -D OPENCV_DNN_CUDA=ON \
      -D BUILD_opencv_cudacodec=OFF \
      -D CUDA_ARCH_BIN=7.5 \ # Sesuaikan dengan arsitektur GPU Anda
      -D WITH_CUDNN=ON \
      -D OPENCV_ENABLE_NONFREE=ON \
      ..
```
- Compile and install OpenCV:
``` bash
make -j$(nproc)
sudo make install
sudo ldconfig
```

2. Install OCR
- Run the following command in the terminal to install Tesseract OCR:
``` bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```
- Install the Indonesian version of the OCR framework:
``` bash
sudo apt install tesseract-ocr-ind
```

## Running Program
1. Testing Cuda
``` bash
python3 testing_cuda.py
```
2. OCR Original Version
``` bash
python3 ocr_read_text_img.py
python3 ocr_live_streaming_nongpu.py
```
3. OCR Indonesia Language Version
``` bash
python3 ocr_live_streaming_nongpu(Indo).py
python3 ocr_live_streaming_gpu(Indo).py
```
## Authors

- [@Yumnasilvia](https://www.github.com/Yumnasilvia)

