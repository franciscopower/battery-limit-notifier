# Battery limit notifier

Displays a notification when battery level is above 90% while the computer is charging or below 20% while the commputer is discharging, in order to alert the user to unplug or plug the computer extending the computer's battery life.

## Windows Installation

Just download the `BatteryLimitNotifierSetup.exe` file and run it on your computer. This will automatically perform all the steps discribed in the "Windows manual installation" section.

## Windows manual installation

1. Download the `Battery Limit Notifier.exe` and `config.yaml` files;
2. Create a folder in the `C:\Program Files` directory named `BatteryLimitNotifier`;
3. Move the `Battery Limit Notifier.exe` and `config.yaml` files to the created folder;
4. Right-click the `Battery Limit Notifier.exe` file and select "Create shortcut";
5. Press the `Windows + r` keys to open up a "Run" prompt. In the text field type "shell:common startup" and click "OK". This will open the startup applications folder.
6. Move the shortcut created in step 5 to the folder opend in step 6.

Once the computer restarts, the program will automatically start. 
To manually start the program, simply double click the program icon.

## Settings

Time between notifications, maximum and minimum battery limits can be adjusted, by adjusting the values in the `config.yaml` file:
```yaml
Battery_min_limit: 20 # percent
Battery_max_limit: 90 # percent
Notification_interval: 5 # minutes
```

## Build from source

This project can be compiled to an executable using a tool such as `pyinstaller` or can be run as a script. 

### Dependencies
(see requirements.txt)
```
psutil==5.8.0
pypiwin32==223
pywin32==303
PyYAML==6.0
schedule==1.1.0
win10toast==0.9
```

### Option 1: Compile into an executable

TO DO

### Option 2: Run program as a script

0. Install Python and all the dependencies listed above on your computer.
1. Download the archive with all the files from this repository onto your computer and unzip it *or* clone this repository onto your computer.
2. Place the `batery_monitor` folder in a folder named `Startup_scripts` in your `C:` drive. The scipts and images should end up int `C:\Startup_scripts\battery_monitor`.
3. Right click on the python file and select *Open with > Choose another app*. When a pop-up windows appears, select "Python" and check the box "Always use this app to open .py files", before clicking OK.
4. Right click on the `battery_limiter_launcher.vbs` file and create a shortcut.
5. Press the `Windows` + `r` keys on your keyboard and a windows should appear. Write `shell:startup` in the text field and click `OK`. This will open up a folder in your windows explorer.
6. Move the shortcut created in step 4 to the folder opened in step 5.
7. Restart your computer and the program should start automatically.


## TODO:
- Explain build from source
- Make relative path for icons work;
- Change duration of notifications;
