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

1. Tesseract-ocr has to be installed and added to path on your desktop pc to run the project. 

   For macOS :
   ```
   brew install tesseract
   ```
   For Windows :
   Download the installer for tesseract from the following link and use windows install wizard to install.
   ```
   https://github.com/UB-Mannheim/tesseract/wiki
   ```
   
3. Clone the repository:
   ```
   git clone <https://github.com/sparsh-kumar7/Qoala)https://github.com/sparsh-kumar7/Qoala>
   cd thai-id-ocr-app

   ```
4. Create Virtual Environment:
   ```
   python -m venv .venv
   ```
5. Start Virtual Environment:

   For macOS:
   ```
   source venv/bin/activate
   ```
   For Windows:
    ```
   venv\Scripts\activate

   ```
6. Install dependencies:
   ```
   pip install -r requirements.txt

   ```
7. Run migrations:
   ```
   python manage.py migrate

   ```
8. Start the Django development server:
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

The following steps occurred during image processing.
1. Inverted the image.

![PHOTO-2023-12-27-01-05-56](https://github.com/sparsh-kumar7/Qoala/assets/85250933/bd34bcd8-7e63-40e9-a366-8af296c7b6da)


2. Greyscaled the image.

![PHOTO-2023-12-27-01-05-56](https://github.com/sparsh-kumar7/Qoala/assets/85250933/086f5b2f-0278-4cb0-97c4-49ff3b86f670)


3. Changed it to black and white using thresholding.

![PHOTO-2023-12-27-01-05-55](https://github.com/sparsh-kumar7/Qoala/assets/85250933/95830a82-dc5f-4337-8463-c7acdae101bf)


4. Reinverted the image.

![PHOTO-2023-12-27-01-05-55](https://github.com/sparsh-kumar7/Qoala/assets/85250933/a3c60d41-1ea1-4def-a02a-c9b669e896c0)


5. Added border to read corner texts.

![PHOTO-2023-12-27-01-05-56](https://github.com/sparsh-kumar7/Qoala/assets/85250933/1d35914d-6922-4f4b-b2bc-4600787e0d87)




