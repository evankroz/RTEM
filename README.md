# Rocket Thrust Evaluation Module (RTEM)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![GitHub Stars](https://img.shields.io/github/stars/evankroz/RTEM?style=social)](https://github.com/evankroz/RTEM)
[![GitHub Forks](https://img.shields.io/github/forks/evankroz/RTEM?style=social)](https://github.com/evankroz/RTEM)

## Disclaimer!

By accessing and using this rocketry repository, you acknowledge that you are aware of the risks associated with rocketry activities. You understand that any information or guidance provided is for educational purposes only, and you assume full responsibility for any actions taken. The repository owner(me) and contributors are not liable for any harm or damage resulting from the use of this information. All rocketry activities should be conducted at your own risk and in compliance with local laws and safety regulations. Please treat any and all rocket motors as explosives until fired and take necessary precautions and storage procedures to minimize risk. Although most safety information will be covered in this guide, common sense is necessary.

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

## Structure

``` zsh
.
├── 3DFiles
│   ├── 0.25Mandrel Hold for Casting v9.stl
│   ├── 0.3853Mandrel Hold for Casting.stl
│   ├── 0.5Mandrel Hold for Casting v9.stl
│   ├── 0.636Mandrel Hold for Casting.stl
│   ├── 0.75Mandrel Hold for Casting v9.stl
│   ├── 1.335MotorHolder v2.stl
│   ├── 1inPVCFunnel.stl
│   ├── ClosureDisks/
│   ├── Fusion360Files
│   │   ├── XLRTEMAssmeblyv1.f3z
│   │   └── a.txt
│   ├── PVCCapDrill032.stl
│   ├── XLComponentCover.stl
│   ├── XLEngineBoxCoverv1.stl
│   ├── XLEngineBoxV15.stl
│   ├── a.txt
│   ├── nozzlecaststand v3.stl
│   └── nozzleconcretecaste.stl
├── LICENSE
├── README.md
├── mentions.md
├── requirements.txt
├── schematics
│   ├── RTEMElectronics.kicad_sch
│   └── a.txt
├── src
│   ├── LoadCellCalibration.ino
│   ├── LoadCellPlotter.ino
│   ├── SerialCSVLogger.py
│   ├── SerialDisplayNONCSV.py
│   ├── a.txt
│   └── wireless.ino
└── ui
    ├── __pycache__
    │   └── app.cpython-313.pyc
    ├── app.py
    ├── demo_plot.py
    ├── graph.py
    ├── main.py
    └── results.py

```

## Overview

The Rocket Thrust Evaluation Module (RTEM) is an open-source project dedicated to providing tools and resources for evaluating rocket thrust performance. This repository contains code, schematics, and documentation to assist in the design, analysis, and testing of rocket engines and propulsion systems.

## Features

*   **Code:** Implementations of thrust calculation algorithms and data processing tools.
*   **Schematics:** Electronic designs for data acquisition and control systems.
*   **Documentation:** Guides on using the module, understanding rocket thrust principles, and interpreting results. (Coming Soon!)

## Getting Started

### Prerequisites

* [Python](https://www.python.org/downloads/) (3.7 or higher)
* [Arduino IDE](https://www.arduino.cc/en/software) (if using the data acquisition components)
* [HX711 Arduino Library](https://github.com/bogde/HX711) (Install via the Arduino Library Manager)

### Recommended "Requirements"

The following items have been verified to work, and reliably so.

* [Sovol SV06 3D Printer](https://www.sovol3d.com/products/sovol-sv06-best-budget-3d-printer-for-beginner?srsltid=AfmBOor-8pa9bs1p1uqZoSzxjIPdzcbphXCHgTdLtcDfJDk9fETHXUum) (Cheap and Reliable, Recommended Filament: PETG)
* [Elegoo Arduino Uno R3](https://www.amazon.com/dp/B01EWOE0UU?ref=ppx_yo2ov_dt_b_fed_asin_title)(Cheap and reliable, expanding to esp32 modules soon!)
* [HX711 Module](https://www.amazon.com/dp/B079LVMC6X?ref=ppx_yo2ov_dt_b_fed_asin_title)(Others exist (for cheaper...), but out of the many tested, this is the most reliable in terms of SPS and noise)
* [Loooong Printer Cable](https://www.amazon.com/gp/product/B0DHJK5648/ref=ox_sc_saved_title_3?smid=A6T4JXBFY4LP2&psc=1)(Allows to keep expensive electornics ($1000+ laptops) further away from the potential bomb, esp32 wireless comms coming soon!)
* [Aluminum Round Bars](https://www.onlinemetals.com/en/buy/aluminum-round-bar?_gl=1*9q53ki*_up*MQ..*_gs*MQ..&gclid=CjwKCAiA-ty8BhA_EiwAkyoa37jQ9IgVjLr5L9LlD2e6fZ1aLD96FopDmEb4iOxVr1FgKVagvYEVMhoC7oEQAvD_BwE)(Quite reliable raw material supplier for casting motors)
* [Load Cell](https://www.amazon.com/dp/B096FKK8KS?ref=ppx_yo2ov_dt_b_fed_asin_title)(3D Files dimensioned under this load cell, recommended for use (20kg))
* [5V Relay Module](https://www.amazon.com/Tolako-Arduino-Indicator-Channel-Official/dp/B00VRUAHLE/ref=sr_1_8?crid=1ZQF4U026ZM0L&dib=eyJ2IjoiMSJ9.h0EVR8TCbppzx_vKt7A72at8MIXTfm3V6LeEWWapL6oajmAMqI6frB3kFQ1_0h3gyzNVlf-r5nav-8fnOF96wuleZ1DIJsZLTE1V_K5xThTxPldw-DpU1rNY_5zdYexwmC2pFPIO7nFN3jhYitxQ-ZoVsgXS2pcjYRvZbdI2HLumMmhqH_MvDm4KcOHnGUpqdDVrMFzwL9TYrv1CuWxm-tIhQljGd6rbnm9naaaPA1w.C-xjg1RlJiGe1Jlr0uIx-WcDbQ93ys_un8CBElsBUCU&dib_tag=se&keywords=5v+relay&qid=1741825163&sprefix=5v+rela%2Caps%2C94&sr=8-8)(5V Relay - quite reliable)
* [1" Internal PVC Piping](homedepot.com)(PVC is very danegrous to make rocket motors out of but with necessary precautions becomes cheap and reliable)
* [Rockite Concrete](amazon.com)(Rockite concrete made for casting both the forward closure and the nozzle for better performance)
* [1.315" ID PVC Endcap](homedepot.com)(This is used as the primary component of the nozzle)
  
This is quite an extensive BOM, but most of them are quite cheap and easy to acquire.


<---/In Progress/--->
## How to Build A Rocket Motor

### SAFETY
> As mentioned previously almost all general safety guidelines and background information on rocket safety can be found [here](https://www.nakka-rocketry.net/safety.html#:~:text=Wear%20appropriate%20safety%20apparel%2C%20including,in%20particular%2C%20sensitivities%20and%20incompatibilities.). More project-specific safety information and guidelines will be discussed in the section that follows.


## How To Build The RTEM

#### 3D Printed Parts

>If you do not have access to a 3D Printer there are no workarounds as of right now. :(

#### Electrical Components


<-------//------->



## Installation 

### Installing the HX711 Arduino Library

1. Open the Arduino IDE.
2. Go to `Sketch` > `Include Library` > `Manage Libraries...`.
3. In the Library Manager, search for `HX711`.
4. Click `Install` on the `HX711` library by Rob Tillaart.

1.  Clone the repository:
    > Clone Repo.
    ```
    git clone https://github.com/evankroz/RTEM.git
    ```
    > Navigate to RTEM directory
    ```
    cd RTEM
    ```
2.  Install the required Python libraries:
    > Recursively install python packages from requirements.txt
    ```
    pip install -r requirements.txt
    ```

### Usage

>Note: Main RTEM should be connected to laptop through cable or connection (soon) WITHOUT ignitors/leads in the motor. Relay triggers upon connection and WILL PREMATURELY IGNITE MOTOR. 

1.  Navigate to the `code` directory:

    ```
    cd code
    ```
2.  Run the main script:

    >For NON-Logging Purposes/Testing Ignitors etc:
    ```
    python3 SerialDisplayNONCSV.py 
    ```
    >For CSV-Logging Purposes/Writing to Excel File:
    ```
    python3 SerialCSVLogger.py 
    ```