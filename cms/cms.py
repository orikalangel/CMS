#
# sudo apt install -y python3-pip tesseract-ocr
# sudo pip3 install --upgrade pip - Upgrade pip to the latest version:
# sudo pip3 install pytesseract
from picamera import PiCamera
from time import sleep


def extract_numbers_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale for better OCR accuracy
    image = image.convert("L")

    # Apply OCR to extract text from the image
    numbers = pytesseract.image_to_string(image, config="--psm 6")

    # Filter out non-digit characters
    numbers = ''.join(filter(str.isdigit, numbers))

    return numbers

camera = PiCamera()
camera.rotation=90

camera.start_preview()
sleep(2)
camera.capture('/home/st-001/Documents/1.jpg')#if "1%s.jpg %i" replace "1.jpg" that chance tha name of the file - in loop
camera.stop_preview()
camera.close()
image_path = "/home/st-001/Documents/1.jpg"
numbers = extract_numbers_from_image(image_path)
print("Numbers in the image:", numbers)
