# TOBB ETÜ ELE495 - Capstone Project

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Acknowledgements](#acknowledgements)

## Introduction
This capstone project aims to develop an autonomous vehicle that takes vocal instructions of movement in natural turkish language, provides vocal feedback on what is currently happening in its system through an external speaker and sends the information it receives and what it processes from the vocal input synchronously onto a user interface.


## Features
The main features that this project highlights are separated into 4 sections:

# - Hardware
 * Raspberry pi model 3B+ , L298N DC motor Driver, Wireless Speaker and microphone, HC-05 Ultrasonic distance sensor, 2s2p(2 series 2 parallel) lithium-ion batteries, 2 LED indicators (optional), 5V usb output SMPS 
- Operating System and packages : 
- Applications 
- Google Cloud TTS/STT through API, Picovoice Eagle Speaker Recognition through API, OpenAI Chatgpt through API, 

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

[Participant 1]([https://github.com/user1](https://github.com/emiirkaya))
[Participant 2]([https://github.com/user1](https://github.com/mfurkanozdem))
[Participant 3](https://github.com/user1)
[Participant 1](https://github.com/user1)
[Speaker Recognition Tool Api](https://picovoice.ai/docs/eagle)
