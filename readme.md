# Project One - Puzzlbox

# Table of contents

- About Puzzlbox
- Sensor & actuators
- Technologies
- The circuits
- Instructables

# About Puzzlbox

I am an MCT student from Howest in Kortrijk, Belgium.

My project is a smart Puzzlbox using Raspberry Pi 4.
The Pi is used as the brains for the puzzles.

The Puzzlbox is made for children 10 years old and up. It has 4 different games that the user must solve in order to activate the end button.

# Sensor & actuators

Raspberry Pi 4B with 16GB SD Card

### LCD Display 16x2 with PCF8574N expander

The LCD display shows the ip address and messages with instructions.

### WS2812B - 12 RGB Neopixel ring

The neopixel ring shows the process of the player when playing

### 2 Servo motors

The 2 servo motors are used to trigger magnet contacts by magnets attached to sticks.

### RFID Reader

The RFID reader is used to start the game. The user can choose from 4 different colors RFID card.

### Magnet sensors

The magnetic sensors are mainly used in the quiz game to check whether the correct answer has been given.

### BCD with PCF8574N

I read the BCD via the PCF8574N to know which number the user has dialed in the number game.

### MPU6050

The MPU6050 is used to control the servos. When you turn the MPU, the servos turn with it.

#Features on site

- Random questions for the question game
- History of players
- Sensor history
- button to shutdown Pi
- button to test servo's range

## Technologies

These are all used programming languages and libraries.

- [Python](https://www.python.org/)
- [HTML](https://html.com/)
- [Javascript](https://www.javascript.com/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Socketio](https://python-socketio.readthedocs.io/en/latest/)

##Getting things started

To configure the Pi please check out the detailed guide on my [instructables](https://www.instructables.com/PuzzlBox/) page.

## The circuits

The circuit with schematics can be found on the [instructables](https://www.instructables.com/PuzzlBox/) page.

## Instructables

If you would like to remake the project for yourself you can find a detailed guide on [instructables](https://www.instructables.com/PuzzlBox/)

## Contact

Lagae Jens - [jens.lagae@student.howest.be](mailto:jens.lagae@student.howest.be)
Source code: https://github.com/howest-mct/2021-2022-projectone-LagaeJens
