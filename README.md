# siri-baymax-proxy
Python script for piping Siri speech input to Baymax server

## usage
Open up the siri_baymax.py file and fill in your iCloud credentials:
```bash
SiriBaymax = SiriBaymax(icloud_username, icloud_password, command_server)
```
(command_server defaults to Baymax at "http://72.29.29.198:1337/")


Now simply run the script from Terminal or Command Prompt (requires Python 3*):

## Linux\Mac OS X
```bash
$ python3 siri_baymax.py
```
## Windows
```bash
> "C:/Python3x/python.exe" siri_baymax.py
```
where 3.X is your version of Python.

(*) If you don't have Python 3, download it [here](https://www.python.org/downloads/release/python-343/#more-resources).


## on your iDevice
- Under Settings > iCloud, ensure that the Notes App is enabled and connected with your iCloud account
- Talk to Siri like so...
- "Note Baymax, are you satisfied with your care? etc..."
- It may help to add "Baymax" to your Contacts list for speech recognition of proper names.

Compatible with iOS 7 and up. 
