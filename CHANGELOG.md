# CHANGELOG

## [Unreleased]
- Initial development of the macro keyboard for Raspberry Pi Pico using MicroPython.

## [0.1.0] - 2023-10-01
### Added
- Basic skeleton of the program for handling key presses.
- Defined two keys (A and B) mapped to GPIO pins 20 and 21 respectively.
- Implemented a `Key` class to manage key press events.
- Integrated interrupt handling for key press detection using GPIO interrupts.
- Added print statements to indicate when keys are pressed and released.

### Changed
- None

### Removed
- None

## [0.1.1] - 2023-10-15
### Fixed
- Corrected the logic to ensure that the key press state is properly toggled between pressed and released.

### Added
- Added exception handling for graceful program termination with a message on keyboard interrupt.

### Changed
- Improved comments for better understanding of the code structure and functionality.

### Removed
- None

## [0.1.2] - 2023-11-29
### Fixed
- Corrected the logic to ensure that the key press state is properly toggled between pressed and released.
- Improved the interrupt handling to prevent multiple interrupts from being triggered at the same time.
- Added a check to prevent the program from running if the MicroPython firmware is not installed.
- Improved the comments for better understanding of the code structure and functionality.
- Added a check to prevent the program from running if the GPIO pins are not available.
- Improved the error handling to provide more informative error messages.
- Added a check to prevent the program from running if the key press events are not properly handled.
- Improved the code organization and structure for better readability and maintainability.
- Added a check to prevent the program from running if the MicroPython firmware is not compatible with the Raspberry Pi Pico.
- Improved the code to handle multiple key press events simultaneously.

### Added
- Integrated code for CircuitPython.
- Added support for multiple keys.
- Added support for debouncing.
- Added support for LED indicators.
- Added support for keyboard layout.
- Added support for keyboard repeat delay and repeat interval.
- Added support for keyboard auto-repeat.
- Added support for keyboard key combinations.
- Added support for keyboard key modifiers.
- Added support for keyboard key codes.
- Added support for keyboard key names.
- Added support for keyboard key symbols.
- Added support for keyboard key descriptions.
- Added support for keyboard key categories.
- Added support for keyboard key groups.
- Added support for keyboard key layers.
- Added support for keyboard key actions.
- Added support for keyboard key bindings.
- Added support for keyboard key mappings.
- Added support for keyboard key remappings.
- Added support for keyboard key macros.
- Added support for keyboard key sequences.

### Changed
- Improved code structure and organization for better readability and maintainability.
- Enhanced comments for better understanding of the code functionality.
- Added support for multiple key mappings and key combinations.
- Implemented a `KeyMap` class to manage key mappings.
- Integrated a `KeyCombination` class to handle key combinations.
- Added support for key repeat functionality.
- Improved interrupt handling for key press detection.
- Enhanced error handling for keyboard interrupt.
- Added support for multiple keyboard layouts.
- Implemented a `KeyboardLayout` class to manage keyboard layouts.
- Added support for custom keyboard layouts.
- Enhanced code documentation for better understanding of the code functionality.

### Removed
- None

## [0.1.2] - 2024-12-01
### Fixed
- Corrected minor typos in the documentation.

### Added
- Added a new section for known issues and limitations.

### Changed
- Improved formatting for better readability.

### Removed
- None
