# TOBB ETÜ ELE495 - Capstone Project

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Working Visuals](#Visuals)
- [Acknowledgements](#acknowledgements)

## Introduction
This capstone project aims to develop an autonomous vehicle that takes vocal instructions of movement in natural turkish language to process it into concrete commands for the vehicle to execute(e.g. to move backwards for 2 seconds, turning left, right etc.), provides vocal feedback on what is currently happening in its system through an external speaker and sends the information it receives and what it processes from the vocal input synchronously onto a user interface.


## Features
The main features that this project highlights are separated into 3 sections:

### - Hardware
 * 1x Raspberry pi model 3B+ , 2x L298N DC motor Driver PCB, 4x DC Motors, 4 Tires,  1x Wireless Speaker and microphone, 1x HC-05 Ultrasonic distance sensor, 2s2p(2 series 2 parallel) lithium-ion batteries, 2x LED indicators (optional),1x 5V USB output SMPS PCB(LM2596), 1x MPU6050 Gyroscope Sensor, 1x 470, 1x 330, 4x 1k, 1x 2k Ohm Resistors, 1x pushbutton
### - Operating System and packages 
Raspberry Pi OS 64-bit
#### API Services : 
- Google Cloud Text-to-Speech,Speech-to-Text
- LLM with OpenAI ChatGPT GPT 4.0 API
- Picovoice Eagle Speaker Recognition

### - Applications 
- Speech Recognition: The device will check for the users authentication from its enrolled profiles of the project participants' voices. If it cannot correlate between the users voice and the profiles', the application will not proceed.
- Speech-to-Text: Initially, the users prompt will be converted to text via an STT provider for the LLM to process its content into concrete text commands. 
- Natural Language Processing: The LLM(Large Language Model) service will receive the text from the STT module to filter its contents into sequential commands of movement for the vehicle to perform and discard any prompt that it can't execute.
- Text-to-Speech: This service will provide vocal feedback on its movement while the vehicle propagates along its commanded path.
- Object Detection: The vehicle will stop any time it detects an obstacle along its path using the ultrasonic distance sensor.
- Autonomous Vehicle Navigation: The vehicle will be able to detect any obstacles along its path in forward motion.
- Precise Rotation : The vehicle has an integrated gyroscope sensor module to accurately turn 90 degrees when prompted to turn right or left and 180 degrees when prompted to turn back. This integration allows the car to rotate accurately, regardless of the environments parasitic properties.
- User-Friendly GUI: The User Interface is able to start the main script of the source code to initiate the car to wait for instructions and start giving commands to it through a BLE and SSH server powered PyQT GUI script.

## Installation
In any linux-based SBC(Single Board Computer) PCB like a raspberry pi model 3B+, go to a desired path where you want the project files to be and clone this repository to get the source code of this project by typing the script below on the console:
```
cd desired-path
git clone https://github.com/ELE495-2425Summer/capstoneproject-malloc-grup-2.git
cd capstoneproject-malloc-grup-2
```
Install [Python](https://www.python.org/downloads/) 3.10+ and pip if it hasn't already been installed.
Create a virtual environment for Python on a desired path.(Your IDE may also automatically create it.)
```
python -m venv /path/to/new/virtual/environment-name
source environment-name/bin/activate
```
Install the required libraries below using a comfortable IDE for Python(make sure your environment is activated):
```
pip install pyaudio numpy pydub google.cloud google openai pveagle
```        
Note: Make sure you create a seperate virtual environment for Python before installing any libraries to prevent compatibility issues as you navigate throughout the project.

It is time to create accounts for the API calls, you need to sign up for Google Cloud and Picovoice to retrieve your API keys for free. You also need to sign up and pay $5 to create an API account for OpenAI's GPT APIs.

Once you are registered, you need to find your API keys for every service and replace the old keys in the code you downloaded with your own ones. Additionally, you must download these files from the links below and put them into your project folder where your python scripts are.
[libpv_eagle.so](https://github.com/Picovoice/eagle/blob/main/lib/raspberry-pi/cortex-a53/libpv_eagle.so)
[eagle_params.pv](https://github.com/Picovoice/eagle/blob/main/lib/common/eagle_params.pv)

Now you are ready to execute the main script to run the project. If you wish, you may also execute the script using the UI.

Start assembling the hardware to the skeleton of the vehicle as you see fit or according to our project image with reference to the schematic and circuit image below using jumper wires or thick cables for high power rails(power supply lines) if necessary.

### Vehicle circuit connection image
<img width="3000" height="1723" alt="circuit_image(4)" src="https://github.com/user-attachments/assets/af7cf2fb-02f8-498f-be5a-5357663b2c9e" />



Note: Since this project is made for a Raspberry pi Model 3B+, the pins may differ from other brands or models. So the PWM and I2C pins should be connected with respect to the module at hand and not just any other GPIO.


### Vehicle front image

![ön](https://github.com/user-attachments/assets/11e865c4-f14c-4121-a793-413b5464159e)



### Vehicle Up image
![üst](https://github.com/user-attachments/assets/ff7a7eaa-4af7-42d0-868e-24046de0845c)

### Vehicle Right side image
![sağ](https://github.com/user-attachments/assets/5d1a60e9-374e-4a83-bf5e-65dd5f47a8fe)


### Vehicle Left side image
![osl](https://github.com/user-attachments/assets/0f5a0fe9-b09d-4955-b177-eeaf4cb60ad9)

### Vehicle Rear side image

![arka](https://github.com/user-attachments/assets/d75fac7e-867c-4013-8ecf-f4df1a8811c8)


Start connecting the bluetooth speaker and microphone to the SBC using either the ssh server from the UI, or the Raspberry pi OS using a VNC connection. How to use a [VNC](https://www.youtube.com/watch?v=EXYiHmbyZ9c&pp=ygUhdm5jIGNvbm5lY3QgcmFzcGJlcnJ5IHBpIGV0aGVybmV0) connection on the same network(ethernet).


## Usage
After installing the required hardware and software prerequisites the user is able to start giving commands either from the UI or through the push button on the breadboard of the vehicle. Before the user can speak, they must register their voices through the speaker recognition function enroll_speaker that is present in the stt_modulu.py script. The speaker will give audio samples until the Progress is 100% done like the image below. Make sure to give different sentences or words otherwise the bar will not go all the way up.

![image](https://github.com/user-attachments/assets/59d34c87-1efb-482d-90a1-c2d8eeea8281)


Once the main.py python script is run from the user interface or manually through the original operating system through an ethernet VNC connection, the vehicle will begin to wait for the user to either start recording from the UI using the 'record' button or through the push button on the vehicle to start giving vocal instructions through the microphone indicated by the BLUE LED.

## Visuals


Working video [link](https://youtu.be/z8yhrKLpuHg) on YT 

## Acknowledgements

Participant 1 -> [Emir Kaya](https://github.com/emiirkaya)
Participant 2 -> [Furkan Özdem](https://github.com/mfurkanozdem)
Participant 3 -> [Emir Şefik Öztürk](https://github.com/SEFIK5545)
Participant 4 -> [Bilge Cimbar](https://github.com/Bilge-Cimbar)

[Raspberry Pi](https://www.raspberrypi.org/)
[Speaker Recognition Tool API](https://picovoice.ai/docs/eagle)
[Text-to-Speech Tool API](https://cloud.google.com/text-to-speech/docs)
[Speech-to-Text Tool API](https://cloud.google.com/speech-to-text/docs/)
[LLM Tool API](https://platform.openai.com/docs/api-reference/introduction)
