🕵️ STARK OSINT CLI

___

A powerful Command-Line Interface (CLI) tool for Open Source Intelligence (OSINT) operations, featuring concurrent lookups, data tracing, and image analysis. This guide provides a complete, step-by-step walkthrough for setting up and running the tool on various operating systems.

🚀 Features
Concurrent Phone OSINT: Traces number details (Source 1) and checks against a leaked database (Source 2).

Concurrent Vehicle Info: Retrieves vehicle registration details using public APIs (Source 1) and a scraped database (Source 2).

Financial & Network Lookups: Supports IP address geolocation and IFSC code lookups (Indian Bank Codes).

Image Analysis: Extracts EXIF metadata and performs OCR (Text Extraction) from local image files.

⚙️ Installation Guide by Operating System
1. For Linux (Debian/Ubuntu)
Follow these steps from a terminal to set up the tool on a Debian or Ubuntu-based system.

Step 1: Get the Code and Install Python Dependencies
First, clone the repository and navigate into the directory. Then, install the required Python libraries.

Bash

sudo apt update
sudo apt install git python3 python3-pip
git clone [YOUR_REPO_URL] starkosint
cd starkosint
pip3 install -r requirements.txt
# Alternatively, if you don't have a requirements.txt file, use this command:
pip3 install requests beautifulsoup4 numpy opencv-python Pillow pytesseract exifread colorama
Step 2: Install System Dependencies for OCR
Install Tesseract OCR and other libraries necessary for image processing.

Bash

sudo apt install tesseract-ocr libsm6 libxext6 libxrender-dev build-essential
Step 3: Configure API Key
Open the starkosint.py file in a text editor and replace the placeholder API key.

Bash

nano starkosint.py
Find the API_TOKEN line and update it:

Python

# === CONFIGURATION FOR LEAK OSINT (Source 2) ===
API_TOKEN = "YOUR_ACTUAL_API_TOKEN_HERE"
Step 4: Run the Tool
You can now execute the script from the main project directory.

Bash

python3 starkosint.py
2. For Termux (Android)
This guide is specifically for setting up and running the tool on an Android device using the Termux terminal emulator.

Step 1: Get the Code and Install Python Dependencies
Bash

pkg update && pkg upgrade -y
pkg install git python python-pip
git clone [YOUR_REPO_URL] starkosint
cd starkosint
pip install -r requirements.txt
# Alternatively:
pip install requests beautifulsoup4 numpy opencv-python Pillow pytesseract exifread colorama
Step 2: Install System Dependencies for OCR
Install Tesseract OCR and other core packages for image processing.

Bash

pkg install tesseract-ocr clang make libjpeg-turbo-dev zlib-dev
Step 3: Configure API Key
Use a text editor like nano to edit the script.

Bash

nano starkosint.py
Find and update the API_TOKEN variable with your key:

Python

# === CONFIGURATION FOR LEAK OSINT (Source 2) ===
API_TOKEN = "YOUR_ACTUAL_API_TOKEN_HERE"
Step 4: Run the Tool
Bash

python starkosint.py
3. For macOS
This guide assumes you have Homebrew installed.

Step 1: Get the Code and Install Python Dependencies
Bash

git clone [YOUR_REPO_URL] starkosint
cd starkosint
pip3 install -r requirements.txt
# Alternatively:
pip3 install requests beautifulsoup4 numpy opencv-python Pillow pytesseract exifread colorama
Step 2: Install System Dependencies for OCR
Install Tesseract via Homebrew.

Bash

brew install tesseract
Step 3: Configure API Key
Open the starkosint.py file with your preferred editor and update the API token.

Bash

nano starkosint.py
Update the API_TOKEN line:

Python

# === CONFIGURATION FOR LEAK OSINT (Source 2) ===
API_TOKEN = "YOUR_ACTUAL_API_TOKEN_HERE"
Step 4: Run the Tool
Bash

python3 starkosint.py
4. For Windows
This guide covers everything a Windows user needs to get the tool running, including the Tesseract setup.

Step 1: Install Git and Python
Download and install Git from https://git-scm.com/.

Download and install Python 3 from https://www.python.org/downloads/. Make sure to check the "Add Python to PATH" option during installation.

Step 2: Get the Code and Install Python Dependencies
Open a Command Prompt or PowerShell, then execute these commands.

Bash

git clone [YOUR_REPO_URL] starkosint
cd starkosint
pip install -r requirements.txt
# Alternatively:
pip install requests beautifulsoup4 numpy opencv-python Pillow pytesseract exifread colorama
Step 3: Install Tesseract OCR
Download the official Tesseract OCR installer from the UB Mannheim GitHub page: https://github.com/UB-Mannheim/tesseract/wiki

Run the installer. During installation, you must select "Add Tesseract to PATH" to make it accessible from the command line.

Note the installation directory, typically C:\Program Files\Tesseract-OCR\.

Step 4: Configure API Key and Tesseract Path in Script
Open starkosint.py in a text editor (e.g., Notepad++ or VS Code).

Find the API_TOKEN line and update it:

Python

# === CONFIGURATION FOR LEAK OSINT (Source 2) ===
API_TOKEN = "YOUR_ACTUAL_API_TOKEN_HERE"
Locate the line that sets the Tesseract path and update it to match your installation path. This is a critical step for Windows.

Python

# Find this line:
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# And change it to:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Step 5: Run the Tool
Bash

python starkosint.py
🏃 Usage Guide
After following the installation steps for your specific OS, run the script from the main starkosint directory.

File Input (Option 5: Analyze Image)
When you choose Option 5 (Analyze Image), the tool will prompt for the full file path to the image on your local file system.

Environment	Example Path	Notes
Linux/macOS	/home/user/images/photo.png	Use absolute or relative paths.
Windows	C:\Users\YourName\Desktop\image.jpg	Use the full path shown in File Explorer.
Termux	/sdcard/DCIM/camera.jpg	Requires running termux-setup-storage and granting storage permissions first.
🛑 Disclaimer
This tool is provided for educational and authorized security testing purposes only. The use of data from scraped databases may have legal implications. The developer is not responsible for any misuse. Use responsibly and ethically.
