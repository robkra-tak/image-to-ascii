# ASCII Art Generator

This Python application converts an image into ASCII art. It uses the OpenCV library to process images and generates ASCII art with customizable width and height.

## Requirements

- Python 3
- OpenCV Python package

## Installation

1. Clone this repository.
2. Install the required Python packages using pip.

## Usage

You can run the ASCII Art Generator from the command line with the following syntax:

```
python app.py <image_path> <output_width> <output_height>
```

Where:

- `<image_path>` is the path to the image file you want to convert to ASCII art.
- `<output_width>` is the desired width of the ASCII art.
- `<output_height>` is the desired height of the ASCII art.

For example:

```
python app.py image.jpg 100 30
```

This will convert the image at `image.jpg` into ASCII art with a width of 100 characters and a height of 30 characters.

The ASCII art will be printed to the console and also saved to a text file in the output directory.

## Functionality

The application works by first loading the specified image using OpenCV. It then converts the image to grayscale and resizes it to the specified dimensions. The grayscale pixel values are then mapped to ASCII characters, with different characters representing different intensities of gray. The resulting ASCII characters are assembled into a string, which forms the ASCII art.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.