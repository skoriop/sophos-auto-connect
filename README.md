# SophosAutoConnect
A small Python script using Selenium & Edge to auto-login to the LAN. It spawns a temporary Edge window and uses Selenium to auto-fill the login credentials.


# Requirements
  * Python 3
  * Selenium: `pip install selenium`
  * [Selenium Webdriver for Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 
    * After downloading, just add the executable to your PATH.

# Usage
Add your username and password to `connect.py` and run it: 
```
python3 connect.py
```

`connect.bat` lets you do this without opening Command Prompt and also starts up an Edge window to use. (To stop this, remove the last line.)

To use a different browser (like Chrome) for the temporary window, replace ```browser.Edge()``` with your browser and install its Selenium webdriver instead.
