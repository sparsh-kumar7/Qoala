# Thai ID OCR App with Django, PyTesseract, and OpenCV

# Overview
Welcome to the Thai ID OCR App, a Django-based application that performs Optical Character Recognition (OCR) on Thai ID card images. PyTesseract is used for OCR, and OpenCV is employed for image preprocessing to enhance readability. The application allows users to extract information from Thai ID cards, save the results in a database, and perform operations such as updating or deleting stored ID cards.

# Link 
Correctly Hosted Working LINK : https://ocr-thai-production-7e36.up.railway.app/

# Technologies Used
1. Django for web application development
2. PyTesseract for OCR
3. OpenCV for image preprocessing
4. Database: SQLite (default with Django)
5. Other dependencies: See requirements.txt

# Setup Instructions
1. Clone the repository:
   ```
   git clone <[repository_url](https://github.com/sparsh-kumar7/Qoala)https://github.com/sparsh-kumar7/Qoala>
   cd thai-id-ocr-app

   ```
2. Create Virtual Environment:
   ```
   python -m venv .venv
   ```
3. Start Virtual Environment (macOS & windows):
   ```
   source venv/bin/activate
   ```
   ```
   venv\Scripts\activate

   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt

   ```
5. Run migrations:
   ```
   python manage.py migrate

   ```
6. Start the Django development server:
   ```
   python manage.py runserver

   ```

# User Interface
1. Upload a Thai ID card image (PNG, JPEG, JPG) for OCR.
2. View the extracted information (name, last name, identification number, date of birth, date of issue, date of expiry) in JSON format.

# Advanced Features
1. Error handling for unreadable or unclear ID cards.
2. Code comments for better understanding.

# Snapshots
<img width="1440" alt="Screenshot 2023-12-26 at 4 25 28 AM" src="https://github.com/sparsh-kumar7/Qoala/assets/85250933/a9ffb7c0-caf8-43a8-b500-5fc3a0506cff">
<img width="1440" alt="Screenshot 2023-12-26 at 4 29 08 AM" src="https://github.com/sparsh-kumar7/Qoala/assets/85250933/e0c51f9e-9c61-475c-b9d4-bec99bfc28a0">
<img width="1440" alt="Screenshot 2023-12-26 at 11 49 10 AM" src="https://github.com/sparsh-kumar7/Qoala/assets/85250933/79f78f48-c823-4c32-ab36-21bdf1103f84">


