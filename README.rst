FlashForge Finder API
=======================

This is an unofficial interpretation of the FlashForge Finder API.
It's served with Flask to make it as easy as possible to create your own UI.

Warning
=======================
Use at your own risk. It only does reading operations but it is unofficial and may of course have bugs etc.
This API is done solely by reverse engineering.

How does it work?
=======================
You specify the printer IP address + port in api/app.py, then simply start the Flask app.
This will spawn a lightweight HTTP server which exposes the API functions.

Example output:

/info:

  {
    "Firmware": " V1.5 20170419",
    "Name": "A Finder",
    "SN": " 52985A58",
    "Tool Count": " 1",
    "Type": " Flashforge Finder",
    "X": " 140  Y: 140  Z: 140"
  }

Start it on your machine
=======================
1. Make sure you have Flask installed:

  pip install flask
  
and 
  
  pip install flask-cors

2. Add this environment variable:
  
  **CMD**: set FLASK_APP=app.py 
  
  **Unix Bash**: export FLASKAPP=app.py
  
  **PowerShell**: $env:FLASK_APP=app.py

3. Run it:

  flask run --host=0.0.0.0 --port=5000 --without-threads

4. By default, you should now have access to the API at localhost:5000. Try http://localhost:5000/*{printer IP address}*/info to see if you get any info from the printer.

Start it using Docker
=====================
1. Run this (you might need sudo):

  docker build --tag flashforge-api . && docker run --publish 5000:5000 flashforge-api

What information does the API give me?
=======================

It supports:

/info: General printer info


/head-location: Printer head location (as X, Y Z)


/temp: Current/target temperature


/progress: Print progress


/status: Status (i.e. if it's printing or not)


Does it support other FlashForge models?
=======================
It's only been tested on the Finder model. Please let me know if it works on other models too.
