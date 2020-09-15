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
from PIL import Image


def decode_image(path_to_png):
    '''
    Args:
        path_to_png: relative or absolute path to png
    
    Returns: 
        decoded image from encoded png

    Raises:
        typeError: Not a png file      
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

def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass
