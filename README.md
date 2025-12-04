Keylogger Detection Simulator
=============================

Overview
--------
This project is a **Keylogger Detection Simulator** written in Python.  
It does NOT perform any real keylogging. Instead, it demonstrates how defenders
might try to detect suspicious background programs that could behave like keyloggers.

The tool scans running processes on a Windows machine and applies simple
name-based rules to flag processes that *might* be suspicious. This is for
educational and portfolio purposes only.

Features
--------
- Lists all running processes (PID + name)
- Flags processes whose names/paths/command-lines contain suspicious keywords
  (e.g., "keylog", "logger", "spy", "monitor", "capture", "hook")
- Generates a simple text report in the console
- Teaches how attackers might hide in background processes and how defenders
  might start looking for them

Technology Stack
----------------
- Python 3
- `psutil` library for process inspection
- Designed and tested on Windows using Visual Studio Code

How It Works
------------
1. Uses the `psutil` library to iterate over all running processes.
2. For each process, it collects:
   - PID (Process ID)
   - Name
   - Executable path (if accessible)
   - Command line arguments (if accessible)
3. Combines this information into a single lower-case string.
4. Checks this string for a list of suspicious keywords such as:
   "keylog", "logger", "spy", "stealth", "monitor", "sniff", "capture", "hook".
5. If any keyword is found, the process is marked as "suspicious".
6. Finally, it prints a human-readable report:
   - Summary: total processes and suspicious count
   - List of suspicious processes (if any)
   - List of all processes with a flag (S = suspicious, . = normal)

Installation
------------
1. Install Python 3 from the official website and make sure it is added to PATH.
2. Install Visual Studio Code (optional but recommended).
3. Clone or download this project folder.

   Example using Git:
   - git clone https://github.com/your-username/keylogger-detection-simulator.git

4. Open a terminal in the project folder and create a virtual environment:

   - python -m venv .venv

5. Activate the virtual environment (Windows):

   - .venv\Scripts\activate

6. Install required Python package:

   - pip install psutil

Usage
-----
1. Make sure the virtual environment is activated.
2. Run the script:

   - python detector.py

3. Read the report printed in the console. Suspicious processes (based purely on
   simple name rules) will be highlighted.

Sample Resume Line
------------------
"Developed a Python-based Keylogger Detection Simulator that scans running
processes and flags potential threats using heuristic rules, demonstrating
understanding of defensive security and Windows process inspection."

Disclaimer
----------
- This tool **does NOT perform any keylogging**.
- It is **NOT a real antivirus** or security product.
- It is intended purely for learning, demonstration, and portfolio purposes.
- Real-world malware can use much more advanced techniques to hide from
  detection.
