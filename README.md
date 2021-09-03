# Battery limit notifier

Displays a notification when battery level is above 90% while the computer is charging or below 20% while the commputer is discharging, in order to alert the user to unplug or plug the computer extending the computer's battery life.

## Settings

Maximum and minimum battery limits can be adjusted, by adjusting the values of the following variables:
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
- List dependencies;
- Explain windows and linux instalation;
