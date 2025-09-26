🔎 Stark OSINT CLI
<!-- This image placeholder will be replaced with a cool banner once you have one! -->

![Stark OSINT CLI Banner]

A powerful, open-source command-line interface for conducting various OSINT (Open-Source Intelligence) lookups. This tool streamlines the process of gathering public data, from vehicle details to image metadata.

🌟 Features
- Concurrent Phone OSINT: Combines public phone number tracing with checks against leaked databases.

Vehicle Info Lookup: Finds vehicle registration, ownership, and other details from public APIs.

IP Address Geolocation: Provides detailed geographical and network information for any IP address.

IFSC Code Lookup: Retrieves bank and branch details for Indian IFSC codes.

Image Analysis: Extracts hidden EXIF metadata (timestamps, camera model, GPS data) and performs OCR (Optical Character Recognition) to find text within images.

🚀 Getting Started
To get the tool up and running, follow these simple steps.

Prerequisites
Python 3.6 or higher: Ensure you have Python installed on your system.

Tesseract OCR: This is a system-level dependency required for image analysis.

On Linux (Debian/Ubuntu):

sudo apt update
sudo apt install tesseract-ocr

On macOS (using Homebrew):

brew install tesseract

On Windows:
Download and install the Tesseract executable from https://tesseract-ocr.github.io/tessdoc/Downloads.html. Make sure to add the installation directory to your system's PATH.

Installation
Clone the repository from GitHub:

git clone [https://github.com/stark/osint-cli.git](https://github.com/stark/osint-cli.git)
cd osint-cli

Install the CLI tool using pip:

pip install .

This command will install all the necessary Python libraries and set up the osint_cli command.

🖥️ Usage
Run the tool directly from your terminal:

osint_cli

The CLI will present you with an interactive menu to choose your desired lookup type.

⚠️ Important Note on API Keys
The leak database functionality relies on an API key. For security and privacy, do not hardcode your API key in the source code.

It is highly recommended to use an environment variable to store your token.

1. Set the Environment Variable:
On Linux/macOS:

export LEAK_OSINT_API_TOKEN="your_api_token_here"

On Windows:

set LEAK_OSINT_API_TOKEN="your_api_token_here"

2. Update the osint_cli.py script:
Change the API token line to read from the environment variable instead of Google Colab's user data:

import os
API_TOKEN = os.environ.get('LEAK_OSINT_API_TOKEN')

if not API_TOKEN:
    print("Warning: LEAK_OSINT_API_TOKEN environment variable is not set. Leak lookups will not work.")

🤝 Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

📄 License
Distributed under the MIT License. See LICENSE for more information
