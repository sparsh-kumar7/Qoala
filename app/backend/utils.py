from .models import OCRResult
import io
from PIL import Image
import cv2
import pytesseract
import re
from datetime import datetime
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def noise_removal(image):
    import numpy as np
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=3)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)

def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)
#https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df
import numpy as np

def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    blur = cv2.GaussianBlur(newImage, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle
# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage
def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)

def remove_borders(image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    return (crop)
def convert_date(input_date):
    print(input_date)
    if "." in input_date:
        input_date = input_date.replace(".", "")
    # Parse the input date string
    parsed_date = datetime.strptime(input_date, '%d %b %Y')
    # Format the date in the desired way
    formatted_date = parsed_date.strftime('%d/%m/%Y')
    return formatted_date

def extract_dates_and_english_text(image_path):
    # Use Tesseract OCR to extract text from the image
    img = cv2.imread(image_path)

    inverted_image = cv2.bitwise_not(img)
    cv2.imwrite("temp\inverted.jpg", inverted_image)

    gray_image = grayscale(inverted_image)
    cv2.imwrite("temp\gray_inv.jpg", gray_image)

    thresh, im_bw = cv2.threshold(gray_image, 140, 180, cv2.THRESH_BINARY)
    cv2.imwrite("temp\\bw_image.jpg", im_bw)

    inverted_image2 = cv2.bitwise_not(im_bw)
    cv2.imwrite("temp\inverted2.jpg", inverted_image2)

    #fixed = deskew(inverted_image2) 
    #cv2.imwrite("temp\\rotated_fixed.jpg", fixed)

    #no_noise = noise_removal(fixed)
    #cv2.imwrite("temp\\no_noise.jpg", no_noise)

    no_borders = remove_borders(inverted_image2)
    cv2.imwrite("temp\\no_borders.jpg", no_borders)

    color = [255, 255, 255]
    top, bottom, left, right = [150]*4
    image_with_border = cv2.copyMakeBorder(no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    cv2.imwrite("temp\image_with_border.jpg", image_with_border)

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image_with_border, lang='eng',config=custom_config)
    print(text)
    array = text.split("\n")
    id_exp = r'[0-9]{1}\s[0-9]{4}\s[0-9]{5}\s[0-9]{2}\s[0-9]{1}'
    date_exp = r'[0-2]?[0-9]{1}\s[a-zA-z]{3}[\.]?\s[1-2]{1}[0-9]{3}'
    extracted_dates = []
    name=""
    last_name=""
    id_number=""
    for line in array:
        if(re.search(id_exp, line)):
            t = re.findall(id_exp, line)
            id_number = t[0]
        if(re.search(date_exp, line)):
            t = re.findall(date_exp, line)
            extracted_dates.extend(t)
        if "Name" in line:
            arr = line.split(" ")
            i = arr.index("Name")
            name = arr[i+1]+" "+arr[i+2]
        if "Last" in line:
            if "Lastname" in line:
                arr = line.split(" ")
                i = arr.index("Lastname")
                last_name=arr[i+1]
            else:
                arr = line.split(" ")
                i = arr.index("Last")
                last_name=arr[i+2]
    dob = ""
    doi = ""
    doe = ""
    if(len(extracted_dates)==1):
        dob = convert_date(extracted_dates[0])
    elif(len(extracted_dates)==2):
        dob = convert_date(extracted_dates[0])
        doi = convert_date(extracted_dates[1])
    elif(len(extracted_dates)==3):
        dob = convert_date(extracted_dates[0])
        doi = convert_date(extracted_dates[1])
        doe = convert_date(extracted_dates[2])
    # Create the required JSON object
    print(dob)
    json_object = {
        "identification_number": id_number,
        "name": name,
        "last_name": last_name,
        "date_of_birth": dob,
        "date_of_issue": doi,
        "date_of_expiry": doe,
    }

    return json_object

