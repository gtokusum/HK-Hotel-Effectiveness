# Hotel Effectiveness Housekeeping GameDay Entry Reporter

Minimal script that automates the room count sorted by room type for Housekeeping Gameday in Hotel Effectiveness

## Background Info

WILL ONLY WORK WITH EXCEL FILES FROM INFOR HMS. Download the excel file directly from Housekeeping Assignment page. Will need to filter out unassigned rooms.\
Selecting an excel sheet not in the format of HMS tables will result in a file error

Future Implementation:\
Error Handeling - simple version added 3/14/2023\
Streamline building of script - Include initialization set up and automatically create .exe file\
Create more visual pleasing GUI\
Automatically input into Hotel Effectiveness - Will use broweser automater. Will most likely need to install web driver for this. Will need to figure out password storage solution. added 4/21/2023\
Fully automate script on server like Raspberry Pi - will need HE and HMS API and will run on a timer. Could put in updater that checks github regularly and installs updates. Will keep backup of 2 previous version.

## Dependecies

Packages:

[Pandas](https://pandas.pydata.org/)

Use package mangaer [pip](https://pip.pypa.io/en/stable/)

```bash
pip install Pandas
```

## Usage

This version is set to a specific hotel.

To change room type change global variables on HKRECON.py

```python
kings = ['Room types here']
queens = ['Room types here']
suitesK = ['Room types here']
SuitesS = ['Room types here']
suitesQ = ['Room types here']
```

To change points/credits\
Lines 70-114

```python
if points == credit_values_here
```

## Create Executable File

After changing the room types and points, use [pyinstaller](https://pypi.org/project/pyinstaller/) or [auto_py_to_exe](https://pypi.org/project/auto-py-to-exe/) to create executable

```bash
pip install pyinstaller
pip install auto_py_to_exe
```
Using pyinstaller use the following command
```bash
pyinstaller --noconfirm --onefile --windowed  "'PATH TO FOLDER'\gui.py"
```

Using auto_py_to_exe run the following command to start
```bash
auto_py_to_exe
```
This will bring up a GUI for pyinstaller.\
Select the script gui.py and select One File, Window Based

![Alt text](/img/auto_py_to_exe.PNG) 

Convert the script to executable and the exe file should move to "C:\User\YOUR LAPTOP USERNAME\output"