# BoxCar2D Decoder Documentation

This utility is designed to decode and analyze the genetic data strings (genomes) used in the BoxCar2D simulation. It converts encoded car configurations into structured, human-readable reports and machine-interoperable data formats.

## Overview
In the BoxCar2D environment, vehicle configurations are stored as encoded character strings. These strings encapsulate all physical and aesthetic parameters of a vehicle, including:

- **Chassis Geometry**: The precise spatial coordinates (vertices) of the vehicle body.
- **Wheel Specifications**: Attachment points, radii, and density parameters for each wheel slot.
- **Aesthetic Parameters**: Hexadecimal color values used for vehicle rendering.

This script automates the extraction and formatting of these parameters for analysis.

---

## Execution Instructions

### 1. Prerequisites
- **Python Runtime**: Ensure that Python 3.x is installed on your system.
- **File Integrity**: Verify that `decoder.py` is present in the working directory.

### 2. Configuring Input Data
- Open `decoder.py` using a text editor or Integrated Development Environment (IDE).
- Locate the `data` variable assignment at the beginning of the script.
- Replace the existing string with the encoded genome you wish to analyze.
- Save the changes to the file.

### 3. Running the Script
- Open a terminal or command prompt.
- Navigate to the directory containing the script.
- Execute the following command:
  ```bash
  python decoder.py
  ```

---

## Output and Data Management
Upon successful execution, the script generates a dedicated directory for each vehicle, named using a unique identifier derived from the input data (e.g., `car_[ID]/`).

Each directory contains the following outputs:

1.  **`report.txt` (Analysis Report)**
    - A formatted summary intended for human review. It details chassis coordinates, wheel attachment statuses, and calculated physical properties.

2.  **`genome.json` (Structured Data)**
    - A JSON-formatted file containing the raw decoded data. This is suitable for integration with other software tools or for further computational analysis.

**Note:** The use of unique identifiers ensures that multiple car configurations can be analyzed sequentially without data loss or file overwriting.

---

## Troubleshooting
- **Command Not Found**: Ensure Python is correctly added to your system's PATH environment variable.
- **Syntax Errors**: Verify that the encoded string is properly enclosed in quotation marks and that no structural code has been inadvertently modified.
