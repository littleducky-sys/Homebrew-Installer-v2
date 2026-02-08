import json
import os

mode = ""

print("Welcome to Homebrew Installer v2!")
print("This program is meant for windows.")

with open("project/meta/settings.json", "r") as f:
    data = json.load(f)

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

json_write_data = {
    "mode": mode
}

if data["mode"] == "":
 with open("project/meta/settings.json", "w") as f:
     json.dump(json_write_data, f)
     print(f"Mode set to: {mode}")
     print("Settings.json updated.")

if data["mode"] == "console":
    print("console")
elif data["mode"] == "gui":
    print("gui")