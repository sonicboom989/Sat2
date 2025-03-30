import cv2
import numpy as np
import os

def filter_color(image_path, lower_bound, upper_bound, output_path=None):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not read image from {image_path}")

    # Convert image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(image, image, mask=mask)

    if output_path is None:
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_filtered{ext}"

    # Save the result image
    cv2.imwrite(output_path, result)
    print(f"Filtered image saved to {output_path}")

# Example: Filter green color in HSV range

def main():
    filename = 'KUbesat color filter\kubesattestpic.png'
    lower_green = np.array([35, 40, 40])   # Lower bound of green in HSV
    upper_green = np.array([85, 255, 255]) # Upper bound of green in HSV

    filter_color(filename, lower_green, upper_green)

if __name__ == '__main__':
    main()
