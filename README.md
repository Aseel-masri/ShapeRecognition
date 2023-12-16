# Shape Recognition with OpenCV

## Overview

Welcome to the Shape Recognition project built in Python using the OpenCV library! This project focuses on detecting and recognizing various shapes, including faces, lines, rectangles, triangles, and curves, in an input image. The application goes beyond basic shape recognition by annotating each identified shape with descriptive text. Additionally, if a face is detected, the system determines the positions of the eyes, nose, and mouth within the facial region.

## Features

- **Shape Recognition:** The system identifies and outlines different shapes within the input image, enhancing the understanding of its contents.

- **Text Annotation:** Each recognized shape is annotated with descriptive text, providing valuable information about the identified elements.

- **Face Detection:** The project includes a face detection module, allowing the identification of faces within the image.

- **Facial Features Detection:** For recognized faces, the system determines the positions of eyes, nose, and mouth, adding a layer of detailed analysis.

## Technologies Used

- **Python:** The primary programming language for implementing the shape recognition algorithm.

- **OpenCV:** A powerful computer vision library used for image processing, shape detection, and face recognition.

## Transformation Showcase

![Original Image](images/inputImage.png) | ![Processed Image](images/outputImage.png)
--- | ---
*Original Image* | *Image with Shape Recognition*

## How to Run

1. Ensure you have Python installed on your system.

2. Install the required dependencies using:

   ```bash
   pip install opencv-python
   ```

3. Clone or download the repository.

4. Run the main script:

   ```bash
   python shape_recognition.py
   ```

5. Provide an input image, and the program will perform shape recognition and annotation.

