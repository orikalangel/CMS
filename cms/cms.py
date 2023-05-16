#
# sudo apt install -y python3-pip tesseract-ocr
# sudo pip3 install --upgrade pip - Upgrade pip to the latest version:
# sudo pip3 install pytesseract
from picamera import PiCamera
from time import sleep
from PIL import Image
import pytesseract


def extract_numbers_from_image(image_path, min_size=30):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale for better OCR accuracy
    image = image.convert("L")

    # Apply OCR to extract text from the image
    numbers = pytesseract.image_to_string(image, config="--psm 6")

    # Filter out non-digit characters
    numbers = ''.join(filter(str.isdigit, numbers))

    # Get the size of the image
    image_width, image_height = image.size

    # Filter numbers based on size
    filtered_numbers = ""
    for number in numbers:
        # Get the bounding box of the number
        bbox = pytesseract.image_to_boxes(image, config="--psm 6")

        # Calculate the size of the bounding box
        bbox_size = int(bbox.split()[3]) - int(bbox.split()[1])

        # Check if the size is larger than the specified minimum size
        if bbox_size > min_size:
            filtered_numbers += number

    return filtered_numbers

camera = PiCamera()
camera.rotation=90

camera.start_preview()
sleep(2)
camera.capture('/home/st-001/Documents/1.jpg')#if "1%s.jpg %i" replace "1.jpg" that chance tha name of the file - in loop
camera.stop_preview()
camera.close()

image_path = '/home/st-001/Documents/1.jpg'
numbers = extract_numbers_from_image(image_path)
print("Numbers in the image:", numbers)
