# 🤚 Hand Gesture Volume Controller

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.9-orange.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Control your Windows volume with just your hands—no keyboard, no mouse, just gestures!** ✨

</div>

---

## 🎬 Demo

<div align="center">

### 🤏 Volume Control
![Volume Control Demo](1.gif)

### ✊ Mute Gesture
![Mute Demo](2.gif)

### 👋 Full Demo
![Complete Demo](3.gif)

</div>

---

## 🎯 What's This?

Ever wanted to control your computer like Tony Stark? This app uses your webcam and AI to let you adjust volume with simple hand gestures. Pinch to change volume, make a fist to mute. That's it!

## ✨ Features

| Gesture | Action | Description |
|---------|--------|-------------|
| 🤏 **Pinch** | Volume Control | Bring thumb and index finger closer/apart to decrease/increase volume |
| ✊ **Fist** | Mute Toggle | Close all fingers to instantly mute/unmute |
| 👁️ **Visual Feedback** | Hand Tracking | See your hand landmarks tracked in real-time |
| 🎚️ **Smooth Transitions** | Smart Algorithm | No jarring volume jumps—everything's smooth and natural |
| 🪟 **Windows Integration** | Native Overlay | Triggers the Windows volume overlay automatically |

## 🚀 Quick Start

### Prerequisites

- Windows 10/11
- Python 3.7+
- A working webcam
- Decent lighting (helps with hand detection)

### Installation

```bash
# 1. Clone this repo
git clone https://github.com/Younes-Barkat/Hand-Volume-Control.git
cd gesture-volume-control

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run it!
python volumeHandControl.py
```

That's it! Your webcam will open and you can start controlling volume with your hands.

## 🎮 How to Use

1. **Launch the app** - Run `python volumeHandControl.py`
2. **Show your hand** - Position your hand in front of the webcam
3. **Control away!**
   - 🤏 **Pinch gesture**: Move thumb and index finger to adjust volume
   - ✊ **Fist gesture**: Close all fingers to mute
   - 👋 **Open hand**: Unmute and resume control
4. **Exit** - Press `Q` or close the window

### Pro Tips 💡

- Keep your hand within the camera frame
- Make sure you have good lighting
- Smooth movements work better than jerky ones
- The mute gesture requires all fingers to be closed

## 🛠️ Tech Stack

- **OpenCV** - Camera capture and video processing
- **MediaPipe** - Google's ML solution for hand tracking
- **NumPy** - Numerical operations
- **Pycaw** - Windows Core Audio API wrapper
- **Pynput** - Keyboard simulation for Windows overlay

## 📁 Project Structure

```
gesture-volume-control/
│
├── volumeHandControl.py      # Main application
├── HandTrackingModule.py      # Hand detection module
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # You are here!
├── 1.gif                      # Volume control demo
├── 2.gif                      # Mute gesture demo
└── 3.gif                      # Full feature demo
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Webcam not detected | Close other apps using the camera (Teams, Zoom, etc.) |
| Hand not recognized | Improve lighting or move closer to camera |
| Volume too sensitive | The app has built-in smoothing—try slower movements |
| App crashes on start | Make sure all dependencies are installed correctly |

## 🤝 Contributing

Got ideas? Found a bug? Contributions are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Author

**Younes Barkat**

- GitHub: [@Younes-Barkat](https://github.com/Younes-Barkat)
- Links: [linktr.ee/Younes_Barkat](https://linktr.ee/Younes_Barkat)

---

<div align="center">

⭐ **If you found this useful, give it a star!** ⭐

Made with ❤️ and Python

</div>
# Hand-Volume-Control
# VolumeHandControl
# Hand-Volume-Control
