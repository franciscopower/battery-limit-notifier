# Battery limit notifier

Displays a notification when battery level is above 90% while the computer is charging or below 20% while the commputer is discharging, in order to alert the user to unplug or plug the computer extending the computer's battery life.

## Windows installation

### Project description

This repository contains several files. The required files are:
- Two .png images;
- battery_limiter_win.py;
- battery_limiter_launcher.vbs.

### Dependencies
- Python 3.9
- Python packages:
  - psutil
  - schedule
  - win10toast

### Installation

0 - Install Python and all the dependencies listed above on your computer.
1 - Download the archive with all the files from this repository onto your computer and unzip it *or* clone this repository onto your computer.
2 - Place the `batery_monitor` folder in a folder named `Startup_scripts` in your `C:` drive. The scipts and images should end up int `C:\Startup_scripts\battery_monitor`.
3 - Right click on the python file and select *Open with > Choose another app*. When a pop-up windows appears, select "Python" and check the box "Always use this app to open .py files", before clicking OK.
4 - Right click on the `battery_limiter_launcher.vbs` file and create a shortcut.
5 - Press the `Windows` + `r` keys on your keyboard and a windows should appear. Write `shell:startup` in the text field and click `OK`. This will open up a folder in your windows explorer.
6 - Move the shortcut created in step 4 to the folder opened in step 5.
7 - Restart your computer and the program should start automatically.

## Settings

Maximum and minimum battery limits can be adjusted, by adjusting the values of the following variables in the python script script:
```python
BATTERY_MAX_LIMIT=90
BATTERY_MIN_LIMIT=20
```

## Possible errors

**Some trouble with the icon** - replace the relative icon path with the full path.
**Cannot open "charge_now", "charge_full" or "status" files** (Linux) - check `battery_path` variable, check names of files on the linux machine.

## TODO:
- Make relative path for icons work;
- Change duration of notifications;
- Use `psutil` library on Linux version;
- Explain Linux installation
