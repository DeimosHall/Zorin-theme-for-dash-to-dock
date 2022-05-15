from datetime import datetime
import os
import time

name = "extensions/dash-to-dock@micxgx.gmail.com/"
path = f"/home/deimos/.local/share/gnome-shell/{name}"

def change_to_white():
    print("Disabling Dash to dock...")
    os.system("gnome-extensions disable dash-to-dock@micxgx.gmail.com")
    print("Copying files...")
    os.system("cp White\ theme/stylesheet.css /home/deimos/.local/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/")
    print("Enabling Dash to dock...")
    os.system("gnome-extensions enable dash-to-dock@micxgx.gmail.com")

def change_to_dark():
    print("Disabling Dash to dock...")
    os.system("gnome-extensions disable dash-to-dock@micxgx.gmail.com")
    print("Copying files...")
    os.system("cp Dark\ theme/stylesheet.css /home/deimos/.local/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/")
    print("Enabling Dash to dock...")
    os.system("gnome-extensions enable dash-to-dock@micxgx.gmail.com")

# time.sleep(10)

os.system("gnome-extensions disable dash-to-dock@micxgx.gmail.com")
os.system("gnome-extensions enable dash-to-dock@micxgx.gmail.com")

now = datetime.now()
hour = int(now.strftime("%H"))

if (hour >= 8 and hour < 20):
    change_to_white()
else:
    change_to_dark()

while(True):
    now = datetime.now()
    hour = now.strftime("%H:%M:%S")

    if (hour == "08:00:25"):
        change_to_white()
        time.sleep(1)

    if (hour == "20:00:00"):
        change_to_dark()
        time.sleep(1)