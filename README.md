# BackDoor
This program which is written using python will enable the attacker to gain a shell of the victim's machine. It uses python libraries like socket to enable connection between victim's machine and the attacker's machine, time library for time related operations, json library for serialization and deserialization in JSON (JavaScript Object Notation) format, subprocess library to run external commands and processes and os library to interact with the operating system in a portable way.

# Prerequisites
1. Install python3 if not installed.
```bash
winget install python3
```

2. Install pip.
- Download the script, from https://bootstrap.pypa.io/get-pip.py.
- Open a terminal or cmd, change the directory using cd to the folder containing the get-pip.py file and run.

3. Install PyInstaller using pip.
```bash
pip insatll PyInstaller
```

# Usage
- Before run the program open Server.py and Backdoor.py, in there, you will see something like <Attacker_IP_Address>, clear that and instert your attacker's IP address.
- Run the following command in your attacker's machine.
```bash
python3 Server.py
```

- Run the following command in the victim's machine (Powershell/cmd).
```bash
python3 -m PyInstaller Backdoor.py --onefile --noconsole
```

- You will see a folder named dist.
- Open the folder and you will see executable.
- Double click the executable and wait until you gain a shell in your attacker's machine.
