# FlashForge Finder API

This is an unofficial interpretation of the FlashForge API.
It is served with Flask to make it as easy as possible to create your own UI.

Works with:
* FlashForge Finder 1
* FlashForge Adventurer 3 (Thanks @jptrsn)
* FlashForge Adventurer 4 (Thanks @vazman13)

# Warning
Use at your own risk. It only does reading operations but it is unofficial and may of course have bugs etc.
This API is done solely by reverse engineering.

# How does it work?
You start the Flask app which serves a lightweight HTTP server that exposes the API functions.

Example output:

`http://localhost:5000/YOUR_PRINTER_IP_ADDRESS/info`:
```
  {
    "Firmware": " V1.5 20170419",
    "Name": "A Finder",
    "SN": " 52985A58",
    "Tool Count": " 1",
    "Type": " Flashforge Finder",
    "X": " 140  Y: 140  Z: 140"
  }
```
If your printer runs on a different port (default `8899`), you can change the setting in `api/app.py`.
# Run it as a Docker container
Run this:

    `docker build --tag flashforge-api . && docker run --publish 5000:5000 flashforge-api`

# Start it on your machine
1. Make sure you have Flask installed:

    `pip3 install -r requirements.txt`

2. Add this environment variable:
  
    **CMD**: `set FLASK_APP=app.py`
    
    **Unix Bash**: `export FLASKAPP=app.py`
    
    **PowerShell**: `$env:FLASK_APP=app.py`

3. Run it:

    `flask run --host=0.0.0.0 --port=5000 --without-threads`

4. By default, you should now have access to the API at `localhost:5000`.
   
    Try `http://localhost:5000/YOUR_PRINTER_IP_ADDRESS/info` to see if you get any info from the printer.

# Run it in VS Code
1. Make sure you have Flask installed:

    `pip3 install -r requirements.txt`

2. Run `Run: Start Debugging` in VS Code, it will launch the app through `/.vscode/launch.json`
# What information does the API give me?

It supports:

`/info`: General printer info:
```
{
  "Firmware": "V1.5 20170419",
  "Name": "My Finder",
  "SN": "6A8D887A",
  "Tool Count": "1",
  "Type": "Flashforge Finder",
  "X": "140  Y: 140  Z: 140"
}
```


`/head-location`: Printer head location (as X, Y Z):
```
{
  "X": "86.9984",
  "Y": "70.5016",
  "Z": "140"
}
```


`/temp`: Current/target temperature
```
{
  "TargetTemperature": "35",
  "Temperature": "31"
}
```

`/progress`: Print progress
```
{
  "BytesPrinted": 4276,
  "BytesTotal": 4275,
  "PercentageCompleted": 100
}
```

`/status`: Status (i.e. if it's printing or not)
```
{
  "Endstop": "X-max: 1 Y-max: 0 Z-max: 1",
  "MachineStatus": "READY",
  "MoveMode": "READY",
  "Status": "S:0 L:0 J:0 F:1"
}
```
# Contributing
* Suggestions and ideas are welcomed!
* Does the API work and your printer model isn't listed? Let me know!
* Want to add a new feature? Run `tcpdump tcp src port 8899 -A` to find commands from your printer, then share them or implement them and create a PR.
