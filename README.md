# PengenalanAngka

Proyek ini adalah sistem pengenalan digit real-time menggunakan OpenCV dan Tensorflow/Keras. Sistem menangkap video langsung dari kamera dan melakukan pengenalan digit pada area bingkai yang dipotong. Model dilatih pada dataset MNIST untuk mengenali angka tulisan tangan.

Proyek ini membutuhkan instalasi pustaka OpenCV, Tensorflow, Keras, dan numpy. Model terlatih dimuat dari file .h5 yang disimpan. Kode melakukan prapemrosesan gambar pada bingkai yang diambil, memangkas area yang diminati, dan menerapkan model terlatih untuk memprediksi digit.

Proyek ini dapat dijalankan pada CPU dan GPU. Untuk menginstal pustaka yang diperlukan, pengguna dapat menjalankan perintah berikut di terminal:

# pip instal opencv-python numpy tensorflow-cpu keras

Pengguna juga dapat menginstal Tensorflow versi GPU dengan menjalankan pip install tensorflow sebagai gantinya.

Kode tersedia di file main.py. File model.h5 berisi model yang dilatih, dan file demo.mp4 berisi video sampel yang mendemonstrasikan kemampuan proyek. Detail dan instruksi proyek disediakan dalam file README.md.
