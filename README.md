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
The main features that this project highlights are separated into 4 sections:

### - Hardware
 * Raspberry pi model 3B+ , L298N DC motor Driver, 2 DC Motors, 2 Tires and a Ball caster,  Wireless Speaker and microphone, HC-05 Ultrasonic distance sensor, 2s2p(2 series 2 parallel) lithium-ion batteries, 2 LED indicators (optional), 5V USB output SMPS PCB, MPU6050 Gyroscope Sensor
### - Operating System and packages 
Raspberry Pi OS 64-bit

### - Applications 
- Autonomous Vehicle Navigation: The vehicle will be able to detect any obstacles along its path in forward motion.
- Precise Rotation : The vehicle has an integrated gyroscope sensor module to accurately turn 90 degrees when prompted to turn right or left and 180 degrees when prompted to turn back. This integration allows the car to rotate accurately, regardless of the environments parasitic properties.
- Speech Recognition: The device will check for the users authentication from its enrolled profiles of the project participants' voices. If it cannot correlate between the users voice and the profiles', the application will not proceed.
- Speech-to-Text: Initially, the users prompt will be converted to text via an STT provider for the LLM to process its content into concrete text commands. 

- Natural Language Processing: The LLM(Large Language Model) service
- Text-to-Speech: 
- Object Detection:
- User-Friendly GUI: The collected

## Installation
In any linux-based SBC(Single Board Computer) like a raspberry pi model 3B+

```bash
# Example commands
git clone https://github.com/username/project-name.git
cd project-name
```

## Usage
Once the main.py python script is run from the user interface or manually through the original operating system, the vehicle will begin to wait for the user to either start recording from the UI using the 'record' button or through the push button on the vehicle to start giving vocal instructions through the microphone.

When the user has given enough input, they can either press the record button on the UI again or release the button on the vehicle to stop recording. When the recording stops, the SBC will start determine if the users voice is authenticated or not. If they are authenticated, the recorded voice will be sent to the STT service to extract raw text from it 

## Screenshots
Include screenshots of the project in action to give a visual representation of its functionality. You can also add videos of running project to YouTube and give a reference to it here. 

## Acknowledgements
Give credit to those who have contributed to the project or provided inspiration. Include links to any resources or tools used in the project.

[Participant 1](https://github.com/emiirkaya)
[Participant 2](https://github.com/mfurkanozdem)
[Participant 3](https://github.com/user1)
[Participant 1](https://github.com/user1)

[Resource](https://www.raspberrypi.org/)
[Speaker Recognition Tool Api](https://picovoice.ai/docs/eagle)
[Text-to-Speech Tool](https://cloud.google.com/text-to-speech/docs)
[Speech-to-Text Tool](https://cloud.google.com/speech-to-text/docs/)
[LLM Tool](https://platform.openai.com/docs/api-reference/introduction)
