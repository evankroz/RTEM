# Rocket Thrust Evaluation Module (RTEM)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![GitHub Stars](https://img.shields.io/github/stars/evankroz/RTEM?style=social)](https://github.com/evankroz/RTEM)
[![GitHub Forks](https://img.shields.io/github/forks/evankroz/RTEM?style=social)](https://github.com/evankroz/RTEM)



## Structure
``` zsh
RTEM/
├── code/ # Source code for thrust calculation and data processing
│ ├── SerialCSVLogger.py # Logging script
│ ├── SerialDisplayNONCSV.py # Non logging script
│ └── ...
├── schematics/ # Electronic schematics for data acquisition
│ ├── thrust_sensor.pdf # Schematic for the thrust sensor interface
│ └── ...
├── docs/ # Documentation and guides
│ ├── #soon to come.
│ └── ...
├── LICENSE # License information (GNU GPL v3)
└── README.md # This file
```

## Overview

The Rocket Thrust Evaluation Module (RTEM) is an open-source project dedicated to providing tools and resources for evaluating rocket thrust performance. This repository contains code, schematics, and documentation to assist in the design, analysis, and testing of rocket engines and propulsion systems.

## Features

*   **Code:** Implementations of thrust calculation algorithms and data processing tools.
*   **Schematics:** Electronic designs for data acquisition and control systems.
*   **Documentation:** Guides on using the module, understanding rocket thrust principles, and interpreting results. (Coming Soon!)

## Getting Started

### Prerequisites

*   [Python](https://www.python.org/downloads/) (3.7 or higher)
*   [Arduino IDE](https://www.arduino.cc/en/software) (if using the data acquisition components)


## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for details.

## Contact

Evan Kroz - evan.kroz@gmail.com

## Support

For questions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/evankroz/RTEM/issues).





##  <---------> Work in Progress <--------->

### Installation 

1.  Clone the repository:

    ```
    git clone https://github.com/evankroz/RTEM.git
    cd RTEM
    ```
2.  Install the required Python libraries:

    ```
    pip install -r requirements.txt #need to create requirements.txt file in future
    ```

### Usage

1.  Navigate to the `code` directory:

    ```
    cd code
    ```
2.  Run the main script:

    ```
    python SerialDisplayNONCSV.py #for non logging purposes
    python SerialCSVLogger.py #for logging rocket motor thrust
    ```
