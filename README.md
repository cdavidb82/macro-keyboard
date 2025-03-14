# Macro Keyboard

This project provides a customizable macro keyboard solution using Circuit Python, allowing users to create custom keyboard layouts and macros efficiently.

## Table of Contents

- [Authors](#authors)
- [License](#license)
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [Future Development](#future-development)

## Authors

- [@cdavidb82](https://www.github.com/cdavidb82)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Introduction

This project aims to create a customizable macro keyboard using Circuit Python. It provides a simple and efficient way to create custom keyboard layouts and macros.

## Requirements

- Circuit Python compatible board
- Keyboard switches and keycaps
- USB cable
- Computer with internet connection

## References
[CircuitPy Library](https://circuitpython.org/libraries)

[CircuitPy](https://circuitpython.org)

## Installation

1. Install Circuit Python on your board.
2. Clone this repository and upload the code to your board.
3. Add libraries from CircuitPy
    - adafruit_debouncer
    - adafruit_ticks
4. Connect your keyboard switches and keycaps to the board.
5. Verify that your board is recognized by your computer.
6. Run the code and test your keyboard.

## Usage

1. Define your custom keyboard layout and macros in the code.
2. Upload the code to your board.
3. Use your macro keyboard to improve your productivity.

### Key Press and Release Functions

The code includes functions to handle key press and release events. You can customize these functions to perform specific actions when a key is pressed or released.

```python
def on_key_a_pressed():
    print("Function for Key A pressed")

def on_key_b_pressed():
    print("Function for Key B pressed")

def on_key_a_released():
    print("Function for Key A released")

def on_key_b_released():
    print("Function for Key B released")
```

## Troubleshooting

- If your board is not recognized by your computer, try restarting your computer and board.
- If your keyboard layout is not working as expected, check your code for errors.

## Contributing

Contributions are welcome. To contribute, fork this repository and submit a pull request with your changes.

## Changelog

- v1.0: Initial release
- v1.1: Added support for multiple keyboard layouts
- v1.2: Improved macro functionality
- v1.3: Added key press and release functions

## Future Development

- Add support for wireless connectivity
- Improve user interface for easier macro creation
- Add support for multiple boards
