OSINT CLI Tool by Stark
This is a powerful command-line interface (CLI) tool for performing various OSINT (Open-Source Intelligence) lookups. It provides functionalities to trace phone numbers, retrieve vehicle information, look up IP addresses, and analyze image metadata and text.

Features
Concurrent Phone OSINT: Combines phone number tracing and leak checks from multiple sources.

Concurrent Vehicle Info: Fetches vehicle registration details from public APIs and scraped databases.

IP Address Lookup: Provides geographical and network information for any IP address.

IFSC Code Lookup: Retrieves bank and branch details for Indian IFSC codes.

Image Analysis: Extracts EXIF metadata and performs Optical Character Recognition (OCR) to find hidden text.

Leak Database Check: Searches a leaked database for information related to emails, usernames, and other queries.

Installation Instructions
Clone the Repository:

git clone [https://github.com/stark/osint-cli.git](https://github.com/stark/osint-cli.git)
cd osint-cli

Create a Virtual Environment (Recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install System Dependencies (Tesseract OCR):
The tool relies on Tesseract OCR. On Debian/Ubuntu systems, you can install it using:

sudo apt-get update
sudo apt-get install tesseract-ocr

Install Python Dependencies:
Use pip to install all the required libraries:

pip install .

Usage
Once installed, you can run the CLI from your terminal:

osint_cli

Follow the on-screen menu to select your desired OSINT operation.

Important Note on API Keys
This tool uses a hardcoded API token for the leaked database lookup. This is not a secure or sustainable practice for public distribution.

For personal use: You must replace API_TOKEN = userdata.get('Api') with your own token.

For public use: It is strongly recommended to use environment variables to manage your API key securely. An example of how to modify the code for this is:

import os
API_TOKEN = os.environ.get('LEAK_OSINT_API_TOKEN')
if not API_TOKEN:
    print("Warning: LEAK_OSINT_API_TOKEN environment variable is not set. Leak lookups will fail.")

You would then set the environment variable on your system.

License
This project is licensed under the MIT License.
