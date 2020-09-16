"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://make-school-courses.github.io/BEW-2.3-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image, ImageDraw, ImageChops


def decode_image(path_to_png):
    '''
    Args:
        path_to_png (str): relative or absolute path to png
    
    Returns: 
        decoded image from encoded png

    Raises:
        FileNotFoundError: File not found
    '''
    encoded_image = Image.open(path_to_png)
    decoded_img = encoded_image.copy()

    pixels = decoded_img.load()
    x_size, y_size = decoded_img.size

    for i in range(0,x_size):
        for j in range(0,y_size):
            if pixels[i,j][0] % 2 == 0:
                pixels[i,j] = (0,0,0)
            else:
                pixels[i,j] = (255,255,255)

    decoded_img.save("decoded_image.png")

def encode_image(path_to_png, text_to_write):
    """
    Args:
        path_to_png (str): relative or absolute path to png
        text_to_write (str): text to encode with, takes multiline sentences
    
    Returns: 
        encodes image on given file

    Raises:
        FileNotFoundError: File not found
    
    """
    raw_image = Image.open(path_to_png).convert("RGB")
    round_red_channel(raw_image)
    msg_image = Image.new("RGB",raw_image.size,(0,0,0))

    msg = ImageDraw.Draw(msg_image)
    msg.multiline_text((10,10), text_to_write, fill=(1,0,0))
    msg_image.save('Savedtext.png')

    encoded_image = ImageChops.add(raw_image,msg_image)
    encoded_image.save('encoded_image.png')

def round_red_channel(image):
    '''
    Args:
        image (PIl image file): realtive or absolute path to png
    
    Returns:
        image with all it's channel rounded down
    
    Raises:
        TypeError: arg image is not a PIL image file
    '''
    pixels = image.load()
    x_size, y_size = image.size
    for i in range(0,x_size):
        for j in range(0, y_size):
            pixel = pixels[i,j]
            pixels[i,j] = (pixel[0] - pixel[0]%2,pixel[1],pixel[2])
    
    

