# YACHACK_OPENCV

## Getting started

Code in Python, for the operation of a 4WD or 2WD robot, using OPENCV, in [Control P(kp)](https://github.com/BrianBot24/YACHACK_OPENCV/blob/main/Kp_line.py) and [Control PID.](https://github.com/BrianBot24/YACHACK_OPENCV/blob/main/Line_Follower.py)

### INSTALL WEBCAM
Visit Link: [Using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/)

### INSTALL WEBCAM UVC
Execute in Terminal:

_sudo rmmod uvcvideo_

_sudo modprobe uvcvideo quirks=2_

<img src="https://raw.githubusercontent.com/BrianBot24/YACHACK_OPENCV/main/doc/terminal.png" width="100%"/>

### YOU WILL NEED
+ Raspbery Pi 3B+ or Superior
+ WebCAM
+ CHASIS 4WD or 2WD
+ TB6612fng or other Bridge H
+ Motors 4 or 2
+ REG 1117 +3.3V
+ Battery

### HOW THE CONTROL PID WORKS

The algorithm was conducted similar to that of a follower line with sensors IR.

<img src="https://raw.githubusercontent.com/BrianBot24/YACHACK_OPENCV/main/doc/PID_1.png" width="100%"/>

+ cx is point Green = 466 (code line 24 - Line_Follower.py)
+ middleX is point Red = 620 (code line 29 - Line_Follower.py)

error=cx-middleX (code line 35 - [Line_Follower.py](https://github.com/BrianBot24/YACHACK_OPENCV/blob/main/Line_Follower.py))

error = 466-620

error = -154

Execute PID TEST, replacing the values of cx and middleX [PID TEST](https://github.com/BrianBot24/YACHACK_OPENCV/blob/main/PID_TEST.py)

LEFT MOTOR SPEED  = 82.08

RIGTH MOTOR SPEED = 57.91 
