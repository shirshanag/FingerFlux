# FingerFlux ✋

A real-time finger counting and hand tracking system built using Computer Vision.

## 🚀 Overview

FingerFlux is a hand gesture recognition project that detects hands in real time and counts raised fingers using landmark estimation. The project uses live webcam input and processes frames to identify finger states efficiently.

This project demonstrates:

* Real-time Computer Vision
* Hand Landmark Detection
* Gesture Analysis
* OpenCV Integration
* MediaPipe Hand Tracking

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## ✨ Features

* Real-time hand detection
* Finger counting (0-5)
* Landmark visualization
* Webcam integration
* Fast and lightweight pipeline

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/FingerFlux.git
cd FingerFlux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python FingerCounter.py
```

---

## 🧠 How It Works

The system uses MediaPipe Hands to detect hand landmarks from webcam frames.

Finger states are determined by comparing landmark coordinates and identifying which fingers are raised.

The total number of raised fingers is then displayed in real time.

---

## 📈 Future Improvements

* Dynamic gesture recognition
* Gesture-controlled applications
* Multi-hand tracking
* Sign language preprocessing
* FPS optimization dashboard

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by Shirsha Nag.
