mode = ""
path = ""

option = input("Where this program's folder being stored (ex C:/Users/joe/Downloads/HBIV2)?")

path = option

print(f"Program folder set to: {path}")
print("if this is the wrong install folder, please restart the program right now.")

print("(WINDOWS ONLY PROGRAM)")
print("Welcome to Homebrew Installer v2!")
print()

print("y=Console/n=GUI")
option = input("Start program in console or (unstable) GUI mode (y/n)?")
if option.lower() == 'y':
    print("Starting in console mode...")
    mode = "console"
elif option.lower() == 'n':
    print("Starting in GUI mode...")
    mode = "gui"
else:
    print("Invalid option. Starting in console mode by default.")
    mode = "console"

print(f"Mode set to: {mode}")
print("Settings.json updated.")