import os
import json
import time
import clearcmd

appjson_path = "project/meta/app.json"

def init():
 
 with open(appjson_path, "r") as f:
    appjson = json.load(f)

 with open(appjson["settings_path"], "r") as f:
    clearcmd.clear()
    data = json.load(f)

 if data["mode"] == "console":
     option = input("What console are you installing homebrew on?")
     if option.lower() not in appjson["Consoles"]:
         clearcmd.clear()
         print("Console isn't supported by this guide yet, or console name is spelled wrong.")
     else:
         if option.lower() != "Nintendo Switch".lower():
             print("--WARNING: EVERYTHING ON YOUR SD CARD WILL. BE. DELETED!!--")
             print("To start please format your SD Card to FAT32.")
             print("if the SD Card is under 32 GB then simply use Quick Format in windows.")
             print("if the SD Card is above 32 GB use GUIFormat [http://ridgecrop.co.uk/index.htm?guiformat.htm].")
             print("if the program is flagged by windows defender or your web browser allow it the application is safe.")
             print("Also dont name the SD Card just ["+option+"] due to homebrew issues,")
             print("name it ["+option+"EX0008] or anything else that isn't just the name of the console.")
             option2 = input("Press N when your ready.")
             if option2 == "N":
                 print("Connecting to Host...")
                 time.sleep(3)
                 print("Host Connected!")
                 time.sleep(1)
         elif option.lower() == "Nintendo Switch".lower():
             print("--WARNING: EVERYTHING ON YOUR SD CARD WILL. BE. DELETED!!--")
             print("To start please format your SD Card to FAT32.")
             print("if the SD Card is under 32 GB then simply use Quick Format in windows.")
             print("if the SD Card is above 32 GB use GUIFormat [http://ridgecrop.co.uk/index.htm?guiformat.htm].")
             print("if the program is flagged by windows defender or your web browser allow it the application is safe.")
             print("EXFAT is supported on the nintendo switch but,")
             print("it is more recommended to use FAT32 for better support.")
             print("Also dont name the SD Card just ["+option+"] due to homebrew issues,")
             print("name it ["+option+"EX0008] or anything else that isn't just the name of the console.")
             
        
 elif data["mode"] == "gui":
     print("gui")

