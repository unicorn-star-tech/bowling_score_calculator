# Bowling Score Calculator

**Version:** 0.1.0 (Alpha)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Known Issues](#known-issues)
4. [Future Optimizations](#future-optimizations)
5. [Testing](#testing)

## Introduction

The Bowling Score Calculator is a Python application designed to help you keep track of your scores while playing a game of 10-pin bowling. It provides a user-friendly interface for recording each throw, calculating scores, and displaying the progress of the game. This alpha version of the program is a basic implementation that allows you to enter the number of pins knocked down in each throw and provides real-time scoring. The overall goal of this project was to build a professional app following OOP principles for a robust and extensible design.

## Installation

To run the Bowling Score Calculator, follow these steps:

1. **Prerequisites:**
   - PyQt6 library installed: https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html 
   - Python 3.12. This application was developed with Python 3.12 and PyQt6, and earlier versions were not tested. 

2. **Download the Application:**
   - Download the source code.

3. **Run the Application:**
   - Navigate to the `application` directory.
   - Run the `bowling_app.py` script using Python.

4. **Navigation:**
   - Use keyboard keys 0-9, x, X, and / to enter scores.
   - Use mouse to click the RESET button.

## Known Issues

1. In the current version, the application may not handle certain edge cases correctly, leading to inaccurate scoring under certain circumstances. Some of these include:
   - More thorough handling of reaching the 10th Frame.
   - Scoring of all Strikes displays the score incorrectly on Throw #20, and there are some other small discrepancies like this where the score displays earlier/later than intended.
   - Throw #20 should not allow a Spare if Throw #19 was a Strike.
   - Throw #21 should not be allowed if Frame 10 is an Open Frame after Throw #20.

2. The user interface is basic, and there is limited error handling for invalid inputs.
   - The GUI had to be re designed to a simpler less elegant version, since there were issues accessing labels when attempting to nest widgets.
   - Some of the error messages are not specific.
   - Not all edge cases have error messages.

3. Some keyboard shortcuts or special characters might not be handled properly, potentially leading to unexpected behavior.
   - Basic keys will be recognized but a variety of keyboards was not tested.

## Testing

To run the test suite for the Bowling Score Calculator, you can use the included `bowling_test.py` script found in the `tests` directory. This script contains unit tests to verify the correctness of the scoring logic.

## Future Optimizations

1. Address and fix the known issues to ensure accurate scoring, additional error messaging, and improved user experience.

2. Address more edge cases.

3. Refactor the code for a more elegant and accurate design, reevaluating the architecture.
   - Re work the logic and design to be more elegant and accurate.
   - Was attempting to be clever with the way Frames were rendered and the score was counted/calculated, which caused some issues with iterating through frames and throws.
   - MVC may not be the most appropriate architecture, especially since PyQt has a Model-View architecture.
   - The styling could be further broken out from the view.
   - Additional sub directories can further organize the project.

4. Enhance the user interface to make it more visually appealing and user-friendly.
   - PyQt6 was chosen since it had the most ability to be expanded for professional use. However, Qt Designer could not be used with PyQt6 and Python 3.12, which limited design options.

5. This application was only tested on Windows 10 Home. Extend platform compatibility by testing on various operating systems.

6. Build executable(s) to make the app easy to run for end users.

7. Improve test coverage and implement additional unit tests to ensure code quality and reliability.

8. In the long term, consider implementing new features, such as support for multiple games, multiple users, and visualizations of pin placements.
