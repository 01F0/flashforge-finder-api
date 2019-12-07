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
You specify the printer IP address + port in api/webapi.py, then simply start the Flask app.
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

How to get it running?
=======================
1. Make sure you have Flask installed:

  pip install flask
  
and 
  
  pip install flask-cors

2. Run it like this (make sure you're in the /api folder)

  env FLASK_APP=webapi.py flask run --without-threads
  
Alternatively, use this to make it visible outside localhost. More info here: https://github.com/01F0/flashforge-finder-api/issues/1
  
  env FLASK_APP=webapi.py flask run --host=0.0.0.0 --port=5000 --without-threads

The environment assignment may differ depending on which shell you're running.

3. By default, you should now have access to the API at localhost:5000. Try http://localhost:5000/*{printer IP address}*/info to see if you get any info from the printer.

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
