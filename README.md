FingerTip Canvas (FT CANVAS)
Overview
FingerTip Canvas (FT CANVAS) is an interactive drawing application that uses hand gestures to draw on a virtual canvas. The application leverages the Mediapipe library for hand detection and OpenCV for drawing and displaying the canvas and camera feed.

Features
Draw on a virtual canvas using hand gestures.
Select colors and clear the canvas using on-screen buttons.
Save the drawings as images.
Use different colors including Blue, Green, Red, Yellow, Orange, Brown, Pink, Cyan, Black, Maroon, Grey, and Purple.
Prerequisites
Ensure you have Python 3.6 or later installed on your system. You also need to install the required Python packages listed in requirements.txt.

Installation
1. Clone the Repository
Clone this repository to your local machine:

git clone <repository-url>
cd <repository-directory>
2. Create and Activate a Virtual Environment
Create a virtual environment using venv:

python -m venv venv
Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
3. Install Required Packages
Install the required packages using requirements.txt:

pip install -r requirements.txt
4. Running the Application
To run the application, use the following command:

cam.py.py
This will start the application, and you should see a window displaying your camera feed and the drawing canvas.

Usage
Drawing: Use your hand to draw on the canvas. The drawing color can be changed by selecting different color buttons on the camera feed.

Clear Canvas: To clear the canvas, use the "CLEAR" button on the camera feed.

Save Drawing: To save your drawing, use the "SAVE" button. The drawing will be saved in the Paintings directory with a unique filename.

Color Selection: Select different colors by moving your hand to the corresponding color button.

Exit: Press ESC to exit the application.

Notes
The application will create a Paintings directory if it does not already exist.
Ensure your webcam is properly connected and accessible for the application to work.
