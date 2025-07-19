# 🛡️ Anti-Proxy Attendance System using Face Recognition

A **secure**, **intelligent**, and **real-time attendance system** powered by **facial recognition**. This system incorporates **blink detection** and **head movement tracking** to verify liveness and **prevent proxy attendance** using printed photos or recorded videos.

---

## 📸 Project Overview

This **Python-based** system uses webcam input to:

* 🧠 Detect and recognize faces of registered individuals
* 👁️ Verify physical presence using **blink detection** and **head movement**
* ✅ Mark attendance **only** when liveness is confirmed
* 🕒 Record names and timestamps in a **daily `.csv` file**

**Ideal for:** Classrooms, offices, and remote/hybrid environments.

---

## 🚀 Features

* ✅ **Real-time face detection and recognition**
* 👁️ **Blink detection** using Eye Aspect Ratio (EAR)
* 🧠 **Head movement tracking** via facial landmarks
* 🚫 **Anti-spoofing** to block photo/video-based fraud
* 🕒 **Attendance logging** with date and time in `.csv`
* 📁 **One `.csv` file per day** for organized records
* 🧼 **Clean and modular codebase** for easy expansion

---

## 📦 Technologies Used

| Technology            | Purpose                                    |
| --------------------- | ------------------------------------------ |
| **Python**            | Main language                              |
| **OpenCV**            | Video capture, frame processing            |
| **face\_recognition** | Face encoding and matching                 |
| **dlib**              | Facial landmarks for blink & head movement |
| **NumPy**             | Numerical computations                     |
| **CSV**               | Attendance file storage                    |
| **datetime**          | Date and time handling                     |

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/anti-proxy-attendance.git
cd anti-proxy-attendance
```

### 2. Install Requirements

Make sure **Python 3.7+** is installed.

```bash
pip install opencv-python face_recognition dlib numpy
```

> ⚠️ For **dlib**, you may need to install **CMake** and **Visual Studio Build Tools (Windows)** or run `brew install cmake` (Mac).

### 3. Download Shape Predictor

Download `shape_predictor_68_face_landmarks.dat` from:

📥 [https://github.com/davisking/dlib-models](https://github.com/davisking/dlib-models)

Place it in your **project root folder**.

### 4. Add Known Faces

Create a folder named `photos/` and add face images:

```
photos/
├── person1.jpg
├── person2.jpg
├── person3.jpg
```

Make sure the faces are **clearly visible** and **centered**.

---

## ▶️ Running the Project

```bash
python attendance_system.py
```

**Controls:** Press `q` to exit the application window.

---

## 📁 Output Example

Each run creates a `.csv` file named like `2025-07-19.csv`:

```
Name,Time
person1,09-12-01
person2,09-12-14
```

Only users who pass **face recognition**, **blink detection**, and **head movement checks** are recorded.

---

## 🧪 Anti-Spoofing Explained

| Check Type          | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| **Blink Detection** | Measures eye aspect ratio (EAR) for real eye movement |
| **Head Movement**   | Detects subtle head/nose shifts for depth             |
| **Face Match**      | Validates identity using stored encodings             |

✅ **Only when all checks pass, attendance is marked.**

---

## 📊 Performance Stats

| Metric                      | Result                         |
| --------------------------- | ------------------------------ |
| Face Recognition Accuracy   | \~93%                          |
| Blink Detection Accuracy    | \~95%                          |
| Anti-Spoofing Effectiveness | **High**                       |
| Frame Rate                  | \~6–8 FPS (hardware dependent) |

---

## 📌 Use Cases

* 👨‍🏫 **Educational institutions** for classroom attendance
* 🏢 **Office environments** for employee check-ins
* 📹 **Secure access control** systems
* 🧑‍💻 **Online/remote attendance** verification

---

## 🚧 Future Improvements

* 📱 Mobile app or **Android support**
* 🌐 **Cloud-based backend** and dashboard
* 🔐 **3D liveness detection** or IR-based sensing
* 📍 **Geofencing or GPS** location verification
* 🔗 Integration with **LMS/HRMS APIs**

---

## 🤝 Contributions

Pull requests are welcome!
For major changes, please **open an issue** first to discuss your ideas.

