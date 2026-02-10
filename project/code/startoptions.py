import json
import os
import consoleselect

mode = ""

print("Welcome to Homebrew Installer v2!")
print("This program is meant for windows.")

appjson_path = "project/meta/app.json"
settingspath = "project/meta/settings.json"

with open(appjson_path, "r") as f:
    appjson = json.load(f)

if appjson["devmode"] == True:
   os.remove(settingspath)

if not os.path.exists(path=settingspath):
    os.makedirs(os.path.dirname(settingspath), exist_ok=True)
    with open(settingspath, "w") as f:
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
 with open("project/meta/settings.json", "w") as f:
     json_write_data = {
    "mode": mode
}
     json.dump(json_write_data, f)
     print("Settings.json updated.")
     data["mode"] = mode

consoleselect.init()