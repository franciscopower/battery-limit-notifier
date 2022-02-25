import psutil
import schedule
import time
from win10toast import ToastNotifier
import yaml
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def check_battery(bat_min_limit, bat_max_limit):
    battery = psutil.sensors_battery()
    bat_status = battery.power_plugged
    bat_percent = battery.percent
    
    #send notification if necessary
    if bat_status and bat_percent > bat_max_limit:
        toaster.show_toast("Unplug your computer!",
                           f"Battery is more than {bat_max_limit}% full.\nUnplug it to keep your battery healthy.",
                           icon_path=resource_path("res\\Elegantthemes-Beautiful-Flat-Battery-full.ico")
                           )
                           
    elif not bat_status and bat_percent < bat_min_limit:
        toaster.show_toast("Low Battery",
                           f"Battery level is below {bat_min_limit}%.\nIt's a good idea to plug your computer in.",
                           icon_path=resource_path("res\\Elegantthemes-Beautiful-Flat-Battery-low.ico")
                           )


def main():
    # determine if the application is a frozen `.exe` (e.g. pyinstaller --onefile) 
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    # or a script file (e.g. `.py` / `.pyw`)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_name = 'config.yaml'
    config_path = os.path.join(application_path, config_name)

    #get settings
    with open(config_path) as config_file: 
    # with open('C:\\dev\\PYTHON\\battery-limit-notifier\\config.yaml') as config_file: #?For testing
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        
    # # Check every 5 minutes
    schedule.every(config['Notification_interval']).minutes.do(check_battery, config['Battery_min_limit'], config['Battery_max_limit'])
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    toaster = ToastNotifier()
    main()
