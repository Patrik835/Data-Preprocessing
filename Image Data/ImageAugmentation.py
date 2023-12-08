import cv2
import numpy as np

MIN_ROTATION_ANGLE = -10
MAX_ROTATION_ANGLE = 10
MIN_BRIGHTNESS = -50
MAX_BRIGHTNESS = 50
MIN_CONTRAST = 0.5
MAX_CONTRAST = 1.5
NOISE_THRESHOLD = 0.4

def load_image(path):
    return cv2.imread(path)

def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def flip_horizontally(img):
    return cv2.flip(img, 1)

def randomly_rotate_image(img):
    angle = np.random.randint(MIN_ROTATION_ANGLE, MAX_ROTATION_ANGLE)
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated = cv2.warpAffine(img, M, (cols, rows))
    return rotated

def radomly_adjust_brightness_and_contrast(img):
    brightness = np.random.randint(MIN_BRIGHTNESS, MAX_BRIGHTNESS)
    contrast = np.random.uniform(MIN_CONTRAST, MAX_CONTRAST)
    b_c = cv2.addWeighted(img, contrast, img, 0, brightness)
    return b_c
 
def add_salt_and_pepper_noise(img):
    noise = np.zeros(img.shape, np.uint8)
    # Set a noise threshold of 0.4 => 40% of the pixels will be changed to black or white
    threshold = NOISE_THRESHOLD
    # Loop through each pixel in the image
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            r = np.random.rand()
            if r < threshold/2:
                # Set pixel to black
                noise[row, col] = 0
            elif r < threshold:
                # Set pixel to white
                noise[row, col] = 255
            else:
                noise[row, col] = img[row, col]
    noised = cv2.add(img, noise)
    return noised

img = load_image('dog.jpg')
gray = convert_to_grayscale(img)
flipped = flip_horizontally(img)
rotated = randomly_rotate_image(img)
b_c = randomly_rotate_image(img)
noised = add_salt_and_pepper_noise(img)
# Show output
cv2.imshow('Input Image', img)
cv2.imshow('Input Image', img)
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Flipped Image', flipped)
cv2.imshow('Rotated Image', rotated)
cv2.imshow('Brightness and Contrast Image', b_c)
cv2.imshow('Noise Image', noised)
cv2.waitKey(0)
cv2.destroyAllWindows()