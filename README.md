# 🚗 BoxCar2D Decoder Guide

Welcome! This tool is designed to take the "secret code" (encoded data) of a car from the BoxCar2D simulation and turn it into something a human can actually read and understand.

## 📋 What does this do?
In BoxCar2D, every car is defined by a long string of random-looking characters (its "genome"). This genome contains all the instructions for building that specific car, including:
- **The Body Shape**: Where each corner (vertex) of the car is located.
- **The Wheels**: Which corners have wheels, how big they are, and how heavy they are.
- **The Colors**: What color the car is painted.

This script "decodes" that string and gives you a clear report of exactly what that car looks like.

---

## 🚀 How to use it

### 1. Preparation
- Make sure you have **Python** installed on your computer.
- Ensure the file `decoder.py` is in your folder.

### 2. Add your Car Data
- Open `decoder.py` with any text editor (like Notepad, TextEdit, or VS Code).
- Look for the line that starts with `data = "..."`.
- Replace the long string inside the quotation marks with the code of the car you want to decode.
- **Save the file.**

### 3. Run the Decoder
- Open your **Terminal** or **Command Prompt**.
- Navigate to this folder.
- Type the following command and press Enter:
  ```bash
  python decoder.py
  ```

---

## 📄 What happens next?
After you run the script, it will create two new files for you automatically:

1.  **`car_[ID]_report.txt` (The Human-Friendly Report)**
    - This is the best file to open if you just want to see the details.
    - It lists the coordinates of the body, which wheels are attached where, and the car's colors in a clear list.

2.  **`car_[ID].json` (The Machine-Readable File)**
    - This file is used if you want to plug the data into another program or website. It's structured specifically for computers.

**Note:** The `[ID]` in the filename is a unique code generated from the car's data. If you decode a different car, it will create a new set of files with a different ID, so you won't lose your previous work!

---

## ❓ Troubleshooting
- **"Python is not recognized"**: You might need to install Python or add it to your computer's "PATH".
- **Error in the code**: Make sure you didn't accidentally delete the quotation marks around the `data` string!
