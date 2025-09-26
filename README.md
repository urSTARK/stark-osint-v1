# 🕵️ STARK OSINT CLI

A versatile Command-Line Interface (CLI) tool for Open Source Intelligence (OSINT) operations, featuring concurrent lookups, data tracing, and image analysis. This version is optimized for **local terminals** and **Termux** environments.

---

## 🚀 Features

* **Concurrent Phone OSINT:** Traces number details (Source 1) and checks against a leaked database (Source 2).
* **Concurrent Vehicle Info:** Retrieves vehicle registration details using public APIs (Source 1) and a scraped database (Source 2).
* **Financial & Network Lookups:** Supports IP address geolocation and IFSC code lookups (Indian Bank Codes).
* **Image Analysis:** Extracts **EXIF metadata** and performs **OCR (Text Extraction)** from local image files.

---

## ⚙️ Setup and Installation

### Prerequisites

You need **Python 3.x** installed.

### 1. Installation Steps (General Linux/macOS)

1.  **Clone the repository (or save the script):**
    ```bash
    git clone [YOUR_REPO_URL]
    cd [your-project-directory]
    # Or simply save the code as osint_cli.py
    ```

2.  **Install System Dependencies (Crucial for OCR):**
    The tool relies on Tesseract for OCR and OpenCV for image processing.

    * **Debian/Ubuntu/Termux:**
        ```bash
        sudo apt update
        sudo apt install tesseract-ocr libsm6 libxext6 libxrender-dev python3-dev build-essential
        ```
    * **macOS (using Homebrew):**
        ```bash
        brew install tesseract
        # OpenCV dependencies are complex, may be handled by pip, but keep in mind build issues.
        ```

3.  **Install Python Libraries:**
    ```bash
    pip install requests beautifulsoup4 numpy opencv-python Pillow pytesseract exifread colorama
    ```

---

## 📱 Termux Setup Guide (Android)

If you are running this tool on an Android device using **Termux**, follow these specific steps for dependencies, as the paths are different.

1.  **Install Core Termux Packages:**
    ```bash
    pkg update && pkg upgrade -y
    pkg install python tesseract-ocr clang make libjpeg-turbo-dev zlib-dev
    ```

2.  **Install Python Libraries:**
    ```bash
    pip install requests beautifulsoup4 numpy opencv-python Pillow pytesseract exifread colorama
    ```

3.  **Update Tesseract Path (If needed):**
    The script assumes the Tesseract executable is at `/usr/bin/tesseract`. In Termux, it's often directly accessible. If you encounter OCR errors, manually check and update this line in the script (`osint_cli.py`):

    ```python
    # Change this line in the script if Tesseract is not found:
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    # Termux usually links it correctly, but you might need:
    # pytesseract.pytesseract.tesseract_cmd = 'tesseract'
    ```

---

## 🔑 Configuration

Before running, you must set your API key for the leaked database lookups.

1.  Open the script (`osint_cli.py`).
2.  Locate the `API_TOKEN` variable and replace the placeholder value with your actual token.

    ```python
    # === CONFIGURATION FOR LEAK OSINT (Source 2) ===
    # NOTE: Replace with your actual token for use!
    API_TOKEN = "YOUR_ACTUAL_API_TOKEN_HERE" 
    ```

---

## 🏃 Usage

Run the script directly from your terminal:

```bash
python3 osint_cli.py
```
___ 

# File Upload (Option 5: Analyze Image)
Since this is a terminal-based script, when you select the "Analyze Image" option, the tool will prompt you to enter the full file path to the image on your local machine or in the Termux file system.

- Linux/macOS Example Path: `/home/user/Pictures/target_image.jpg`

- Termux Example Path: You can access your phone's storage (after running termux-setup-storage) using: `/sdcard/Download/target_photo.jpeg`

***Enter the path carefully when prompted:***

```
--- Image File Path Required ---
Enter the path to the image file: /home/stark/image.jpg
```

#🛑 Disclaimer
- This tool is provided for educational and authorized security testing purposes only. The use of leaked or publicly scraped data may have legal implications in certain jurisdictions. The developer is not responsible for any misuse. Use responsibly and ethically.
