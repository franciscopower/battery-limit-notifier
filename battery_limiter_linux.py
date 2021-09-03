#!/usr/bin/env python3

import notify2
import schedule
import time

BATTERY_MAX_LIMIT=90
BATTERY_MIN_LIMIT=20

battery_path = "/sys/class/power_supply/BAT0/" 

bat_full = None

def check_battery():
    global n_max
    #calculate battery percentage
    with open(battery_path + 'charge_now' , 'r') as bat_now_file:
        bat_now = float(bat_now_file.read())
    bat_percent = round(bat_now/bat_full, 3)*100

    #check if is charging
    with open(battery_path + 'status' , 'r') as bat_status_file:
        bat_status = bat_status_file.read()
        
    #send notification if necessary
    if 'Charging\n' == bat_status and bat_percent>BATTERY_MAX_LIMIT:
        n_max.show()
    elif 'Discharging\n' == bat_status and bat_percent<BATTERY_MIN_LIMIT:
        n_min.show()


n_max = notify2.Notification("Unplug your computer!",
                         f"Battery is more than {BATTERY_MAX_LIMIT}% full.\nUnplug it to keep your battery healthy.",
                         "./res/Elegantthemes-Beautiful-Flat-Battery-full.ico"   # Icon name
                        )
                        
n_min = notify2.Notification("Low Battery",
                         f"Battery level is below {BATTERY_MIN_LIMIT}%.\nIt's a good idea to plug your computer in.",
                         "./res/Elegantthemes-Beautiful-Flat-Battery-low.ico"   # Icon name
                        )

notify2.init('battery_monitor')

with open(battery_path + 'charge_full', 'r') as bat_full_file:
    bat_full = float(bat_full_file.read())

schedule.every(5).minutes.do(check_battery)

while True:
    schedule.run_pending()
    time.sleep(1)