# SUSTech EE201-17L DIY Project - Laser Keyboard


## Project Members
- Wang Haiyu
  - Determined the methodology of the project
  - Designed the whole program
- Zhang Qinbo
  - Designed the outlook of the keyboard
  - 3D printed the keyboard
- Sun Yijing
  - Designed the circuit
  - Camera distortion correction

## Introduction
The laser-projected virtual keyboard designed in this project is based on the combination of OpenCV with an image camera, a 980nm line laser diode, a 980nm infrared filter, and a keyboard projection laser. This device detects points of diffuse reflection caused by finger obstruction of the 980nm line laser diode using a camera equipped with a 980nm infrared filter. By detecting and locating the center of these points, the device identifies and tracks the position of the fingers and maps them to the corresponding keys on the projected keyboard, enabling the appropriate keyboard events on the computer.

![](D:/Files/Document/MyDocument/Workspace/Courses/laser-keyboard/assets/image-20231109112829298.png)


## Design Tasks and Requirements
The design aims to create a virtual keyboard projected by a laser. The appearance should meet the usual habits of most users. It's designed to be clear and distinct on various surfaces and in different environments. The performance requirements involve covering the whole keyboard range with an infrared line laser and providing real-time image capture and data transmission to the computer.

## Solutions and Selection
After considering several project ideas, including a pulse meter, alcohol detection, and electric curtains, the virtual laser keyboard was selected using the TOPSIS entropy weight method for decision-making.

## Theoretical Analysis and Computation
The hardware analysis includes the choice of a 980nm line infrared laser and the keyboard projection laser. A wide-angle camera and circuit design are considered, with a focus on ensuring sufficient light for signal detection and transformation. The software analysis includes image distortion correction with MATLAB, image processing with OpenCV, and the calculation necessary for designing the external frame.

![image-20231109113419931](D:/Files/Document/MyDocument/Workspace/Courses/laser-keyboard/assets/image-20231109113419931.png)

## Circuit Design
The design includes using Altium Designer for circuit schematics and PCB design, and OpenCV for image processing program design. The program flow includes reading the camera input, correcting distorted images, cropping the keyboard area, image erosion and binarization, and locating 'counters' (fingers) to determine the pressed keys.

![image-20231109113124504](D:/Files/Document/MyDocument/Workspace/Courses/laser-keyboard/assets/image-20231109113124504.png)

## Testing and Results
The hardware was tested for device functionality and electrical integrity, while the software was tested for image processing and distortion correction. The overall system was tested in a simulated real-world scenario to ensure accurate keypress detection. And the performance please refer to the video.

<video src="D:/Files/Document/MyDocument/Workspace/Courses/laser-keyboard/video-compressed.mp4"></video>

## Conclusion
This project successfully combines hardware and software to create a functional virtual laser-projected keyboard. It showcases the potential of virtual keyboards in technology and offers improvements over traditional keyboards, such as noise reduction and visibility in dark environments.
