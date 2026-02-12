import json
import os
import consoleselect
import sys
import platform
from time import sleep


mode = ""

print("Welcome to Homebrew Installer v2!")
print("This build of the program is meant for windows.")
print("other builds for linux/macOS should be available,")
print("at the same website you got this windows build from.")

if platform.system() != "Windows":
   print("OS FOUND "+str(platform.system())+" PLEASE READ MESSAGE ABOVE THIS")
   print("EXITING PROGRAM IN 10 SECONDS....")
   sleep(10)
   sys.exit("OS NOT ALLOWED")

#this should be the only hardcoded path but i am not sure.
appjson_path = "project/meta/app.json"

with open(appjson_path, "r") as f:
    appjson = json.load(f)

if appjson["devmode"]["m"] == True and os.path.exists(path=appjson["settings_path"]):
   os.remove(appjson["settings_path"])
                     
if not os.path.exists(path=appjson["settings_path"]):
    os.makedirs(os.path.dirname(appjson["settings_path"]), exist_ok=True)
    with open(appjson["settings_path"], "w") as f:
        json.dump(appjson["prodmake"], f)


with open("project/meta/settings.json", "r") as f:
    data = json.load(f)
    print(data)

if data["mode"] != "console" and data["mode"] != "gui":
 print("y=Console/n=GUI")
 option = input("Start program in console or (unstable) GUI mode (y/n)? ")

 if option.lower() == 'y':
     print("Starting in console mode...")
     mode = "console"
 elif option.lower() == 'n':
     print("Starting in GUI mode...")
     mode = "gui"
 else:
     print("Invalid option. Starting in console mode by default.")
     mode = "console"

if data["mode"] == "":
 with open(appjson["settings_path"], "w") as f:
     json_write_data = {
    "mode": mode
}
     json.dump(json_write_data, f)
     print("Settings.json updated.")
     data["mode"] = mode

consoleselect.init()