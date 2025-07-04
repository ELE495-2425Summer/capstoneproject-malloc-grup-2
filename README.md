# TOBB ETÜ ELE495 - Capstone Project

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Acknowledgements](#acknowledgements)

## Introduction
This capstone project aims to develop an autonomous vehicle that takes vocal instructions of movement in natural turkish language to process it into concrete commands for the vehicle to execute(e.g. to move backwards for 2 seconds, turning left, right etc.), provides vocal feedback on what is currently happening in its system through an external speaker and sends the information it receives and what it processes from the vocal input synchronously onto a user interface.


## Features
The main features that this project highlights are separated into 3 sections:

### - Hardware
 * Raspberry pi model 3B+ , L298N DC motor Driver, 2 DC Motors, 2 Tires and a Ball caster,  Wireless Speaker and microphone, HC-05 Ultrasonic distance sensor, 2s2p(2 series 2 parallel) lithium-ion batteries, 2 LED indicators (optional), 5V USB output SMPS PCB, MPU6050 Gyroscope Sensor
### - Operating System and packages 
Raspberry Pi OS 64-bit
#### API Services : 
- Google Cloud Text-to-Speech,Speech-to-Text
- OpenAI ChatGPT GPT 4.0 API
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
In any linux-based SBC(Single Board Computer) PCB like a raspberry pi model 3B+, clone this repository to get the source code of this project by typing the script below on the console:
```
git clone https://github.com/ELE495-2425Summer/capstoneproject-malloc-grup-2.git
cd capstoneproject-malloc-grup-2
```
Install Python 3.10+ and pip if it hasn't already been installed.[Link](https://www.python.org/downloads/)
Create a virtual environment for Python on a desired path.(Your IDE may also automatically create it.)
```
python -m venv /path/to/new/virtual/environment-name
source environment-name/bin/activate
```
Install the required libraries below using a comfortable IDE for Python(make sure your environment is activated):
```
pip install pyaudio os numpy io pydub google.cloud google.oauth2.service_account threading openai time json
```        
Note: Make sure you create a seperate virtual environment for Python before installing any libraries to prevent compatibility issues as you navigate throughout the project.

It is time to create accounts for the API calls, you need to sign up for Google Cloud and Picovoice to retrieve your API keys for free. You also need to sign up and pay $5 to create an API account for OpenAI's GPT APIs.

Once you are registered, you need to find your API keys for every service and replace the old keys in the code you downloaded with your own ones. Additionally, you must download these files from the links below and put them into your project folder where your python scripts are.
[libpv_eagle.so](https://github.com/Picovoice/eagle/blob/main/lib/raspberry-pi/cortex-a53/libpv_eagle.so)
[eagle_params.pv](https://github.com/Picovoice/eagle/blob/main/lib/common/eagle_params.pv)

Now you are ready to execute the main script to run the project. If you wish, you may also execute the script using the UI.

Start assembling the hardware to the skeleton of the vehicle as you see fit or according to our project image with reference to the schematic and circuit image below using jumper wires or thick cables for high power rails(power supply lines) if necessary.

### Vehicle circuit connection image
![circuit_image(3)](https://github.com/user-attachments/assets/4b4c551f-59c6-4e67-812f-e6afe0ad7d74)


Note: Since this project is made for a Raspberry pi Model 3B+, the pins may differ from other brands or models. So the PWM and I2C pins should be connected with respect to the module at hand and not just any other GPIO.


### Vehicle front image
![12](https://github.com/user-attachments/assets/c63f1b86-19df-489d-88c7-1f3509bc16dc)

### Vehicle Up image

### Vehicle Right side image

### Vehicle Left side image


Start connecting the bluetooth speaker and microphone to the SBC using either the ssh sever from the UI, or the Raspberry pi OS.


## Usage
After installing the required hardware and software prerequisites the user is able to start giving commands either from the UI or through the push button on the breadboard of the vehicle. Before the user can speak, they must register their voices through the speaker recognition function enroll_speaker that is present in the stt_modulu.py script. The speaker will give audio samples until the Progress is 100% done like the image below.
![image](https://github.com/user-attachments/assets/59d34c87-1efb-482d-90a1-c2d8eeea8281)


Once the main.py python script is run from the user interface or manually through the original operating system, the vehicle will begin to wait for the user to either start recording from the UI using the 'record' button or through the push button on the vehicle to start giving vocal instructions through the microphone indicated by the BLUE LED.

## Screenshots


## Acknowledgements

[Participant 1](https://github.com/emiirkaya)
[Participant 2](https://github.com/mfurkanozdem)
[Participant 3](https://github.com/SEFIK5545)
[Participant 1](https://github.com/user1)

[Resource](https://www.raspberrypi.org/)
[Speaker Recognition Tool Api](https://picovoice.ai/docs/eagle)
[Text-to-Speech Tool](https://cloud.google.com/text-to-speech/docs)
[Speech-to-Text Tool](https://cloud.google.com/speech-to-text/docs/)
[LLM Tool](https://platform.openai.com/docs/api-reference/introduction)
