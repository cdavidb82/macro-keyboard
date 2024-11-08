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