import psutil
import schedule
import time
from win10toast import ToastNotifier


BATTERY_MAX_LIMIT=90
BATTERY_MIN_LIMIT=90


def check_battery():
    battery = psutil.sensors_battery()
    bat_status = battery.power_plugged
    bat_percent = battery.percent
    
    #send notification if necessary
    if bat_status and bat_percent > BATTERY_MAX_LIMIT:
        toaster.show_toast("Unplug your computer!",
                           f"Battery is more than {BATTERY_MAX_LIMIT}% full.\nUnplug it to keep your battery healthy.",
                           icon_path="res\\Elegantthemes-Beautiful-Flat-Battery-full.ico"
                           )
                           
    elif not bat_status and bat_percent < BATTERY_MIN_LIMIT:
        toaster.show_toast("Low Battery",
                           f"Battery level is below {BATTERY_MIN_LIMIT}%.\nIt's a good idea to plug your computer in.",
                           icon_path="res\\Elegantthemes-Beautiful-Flat-Battery-low.ico"
                           )


toaster = ToastNotifier()

# Check every 5 minutes
# schedule.every(5).minutes.do(check_battery)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

check_battery() #Testing