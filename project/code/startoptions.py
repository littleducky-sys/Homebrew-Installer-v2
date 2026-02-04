import json
import os

mode = ""

SETTINGS_PATH = "project/meta/settings.json"

if os.path.exists(SETTINGS_PATH):
    with open(SETTINGS_PATH, "r") as file:
        settings = json.load(file)
else:
    settings = {}

if not settings.get("cgui"):
    print("Welcome to Homebrew Installer v2!")

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

    settings["cgui"] = mode

    print(f"Mode set to: {mode}")
    print("Settings.json updated.")

    with open(SETTINGS_PATH, "w") as file:
        json.dump(settings, file, indent=4)

print("test")