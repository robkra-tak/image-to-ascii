import cv2
import sys
import os

def image_to_ascii(image_path, output_width=100, output_height=30):
    # Load the image
    image = cv2.imread(image_path)
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Resize the image to the specified output width and height
    resized_gray_image = cv2.resize(gray_image, (output_width, output_height), interpolation=cv2.INTER_LANCZOS4)

    # Define the ASCII characters that will represent the image
    # The characters are ordered by increasing intensity (i.e., darkness)
    ascii_chars = "@%#*+=-:."

    # Create an ASCII art string
    ascii_art = ""
    for pixel_value in resized_gray_image:
        for value in pixel_value:
            # Map the pixel value to an ASCII character
            ascii_art += ascii_chars[value // 32] if value != 0 else ' '
        ascii_art += "\n"
    
    return ascii_art

def main():
    # Check if the image file path and size parameters are provided as command line arguments
    if len(sys.argv) < 4:
        print("Usage: python ascii_art.py <image_path> <output_width> <output_height>")
        return
    
    # Get the image file path and size parameters from the command line arguments
    image_file_path = sys.argv[1]
    output_width = int(sys.argv[2])
    output_height = int(sys.argv[3])
    
    # Convert the image to ASCII art
    ascii_image = image_to_ascii(image_file_path, output_width, output_height)
    
    # Print the ASCII art
    print(ascii_image)
    
    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Save the ASCII art to a text file in the output directory
    with open(os.path.join('output', 'ascii_art.txt'), 'w') as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()
