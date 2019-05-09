# SumoBot
![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/Img_1.jpg)
## Requirements
1.	LEGO MINDSTORMS EV3 Intelligent Brick
2.	A microSD or microSDHC card (2GB or larger). microSDXC is not supported on the EV3. All cards larger than 32GB will not work with the EV3!
3.	A computer with an adapter for the SD card. You will need administrator user permissions on this computer.
4.	A way to communicate with the device. For the EV3, this can be one of the following:
•	USB cable (the one that comes with the EV3)
•	USB Wi-Fi dongle
•	USB Ethernet (wired) dongle
•	Bluetooth
## Libraries (Computer and EV3 Brick)
1. For the Computer
•	Python
•	Libraries
•	pandas
•	sklearn
•	rpyc
•	VS Code
    A. Extensions
    B. Phyton
    C. Ev3Dev

2. For the Ev3 Brick
•	Python
•	Libraries
•	pandas
•	rpyc
•	threading


## Step 1: Download the latest ev3dev STRETCH image file
•	http://oss.jfrog.org/list/oss-snapshot-local/org/ev3dev/brickstrap/ 
    Steap to download the correct version

![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/1.png)
![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/2.png)
 
•	UnZip the file “snapshot-ev3dev-stretch-ev3-generic-2019-04-07” the name maybe varies a little.
## Step 2: Flash the SD card
•	https://www.balena.io/etcher/
1.	Click the “Select image” button and browse to the folder where you downloaded an ev3dev release. Select the file that you downloaded. The release can be a .img.zip or .img.xz; whichever you have will work with Etcher.
 
![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/3.png)

2.	Plug the SD card into your PC (if your PC doesn’t have a micro SD slot, you can use an adapter or external reader). Etcher should detect the new device and display its information under the “Select drive” step. Confirm that the selected drive is correct.
 
![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/4.png)

3.	When you are confident that you have selected the correct drive, click “Flash!” and wait for the operation to complete.
 
![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/5.png)

4.	If you arrive at this screen, you have successfully flashed your SD card and are ready to move on to the next step.
 
![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/6.png)

## Step 3: Boot ev3dev
1.	Put the SD Card in your EV3 and power it on. At first, you will see the MINDSTORMS boot splash and the red LEDs will be on. This is immediately followed by the ev3dev boot splash and the LEDs changing to orange. The LEDs indicate disk (SD card) activity.

2.	After about one minute, the screen will go blank. This happens on the first boot only. The first boot takes longer than subsequent boots because the EV3 has to create a unique SSH host ids and take care of a few other housekeeping items. After another minute or two, you will see the Brickman loading… screen. If nothing has happened after five minutes, something is not right - check the troubleshooting tips below.

3.	You will notice the number in the battery in the upper right corner. This displays the remaining voltage of the power supply. It is not possible to calculate an accurate percent value of the remaining energy, so this value is chosen. If the voltage drops below 5V the brick will turn off. All unsaved data will be lost. Keep in mind, that it may take a much longer time from 8V to 6.5V than from 6.5V down to 5V!

4.	When the boot is complete, the LEDs will turn green and you will see something like this on the screen

![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/7.png)
 
Troubleshooting tips if your EV3 won't boot:
1.	Make sure nothing is plugged into the EV3 (USB/sensors/motors/etc.)
2.	Try writing the image to the SD card again.
3.	You may have a bad/incompatible SD card - try a different SD card.
4.	Check the condition of the EV3 batteries.
## Step 4: Download and install VS Code
1.	https://code.visualstudio.com/download
Step 5: In VS Code, Open the Hello World started project folder and install two extensions
1.	Download this example of VS Code Hello World for Ev3Dev 
a.	https://github.com/ev3dev/vscode-hello-python
b.	Follow the steps inside of the Readme.md

## Install RPyC
https://sites.google.com/site/ev3python/learn_ev3_python/rpyc

Configure server.sh file to start the server on the EV3

Connect it via bluetooth to the computer where the processing will take place

Set the IP address in the file that will be run on the computer so that it sends the indications to the EV3

Start the server on the EV3 and run the program on the computer

## Description of the programs:
### Test.py
1. Code for the creation of a classifier model of actions, carried out according to the data set provided by using MLPClassifier
2. Make use of the model to make a prediction
3. Give a report evaluating the accuracy of the model

### Sumobot.py
1. The actions of the sumobot are defined by means of functions (Found, Dodging, Searching, Attacking)
2. Function is defined to run the multiple actions depending on the inputs (Without AI)
3. The function is declared to collect the data of the inputs of the sensors and the actions carried out according to the inputs
4. Through threads the function Main () is declared to run the two previously mentioned functions

### RunMLP.py
1. The actions of the sumobot are defined by means of functions (Found, Dodging, Searching, Attacking)
2. The function is declared to run the multiple actions depending on the inputs referring to the MLPClassifier model

##A reference to disaing a sumobot

Open Building Instructions.html locate on the main folder 

![alt text](https://github.com/DanielAbner71/Sumo/blob/master/Img/8.png)

## Referencias 
https://www.youtube.com/watch?v=TNXqizQTZhs
https://sites.google.com/site/ev3devpython/
https://sites.google.com/site/ev3devpython/the-vs-code-workflow
