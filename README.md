# siri-baymax-proxy
Python script for piping Siri speech input to Baymax server

## usage
Open up siri_baymax.py and fill in credentials:
```bash
SiriBaymax = SiriBaymax(icloud_username, apple_password, command_server)
```
(command_server defaults to Baymax at http://72.29.29.198:1337)

Run the script from the command line (requires Python3)...

## Linux
```bash
$ python3 siri_baymax.py
```
## Windows
```bash
> "C:/Python3x/python.exe" siri_baymax.py
```
## on your iDevice

- Ensure that Notes is enabled and connected with your iCloud account
- Talk to Siri like so...
- "Note Baymax, are your satisfied with your care? etc..."

Compatible with iOS 7 and up 
