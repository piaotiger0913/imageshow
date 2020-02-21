# imageshow
1 first install kivy
   URL:https://kivy.org/doc/stable/installation/installation-rpi.html

   sudo apt update
   sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
      pkg-config libgl1-mesa-dev libgles2-mesa-dev \
      python-setuptools libgstreamer1.0-dev git-core \
      gstreamer1.0-plugins-{bad,base,good,ugly} \
      gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
      xclip xsel libjpeg-dev
   sudo python3 -m pip install --upgrade --user pip setuptools
   sudo python3 -m pip install --upgrade --user Cython==0.29.10 pillow

   sudo pip3 install kivy

2 then install onedriver

-curl -L https://raw.github.com/pageauc/rclone4pi/master/rclone-install.sh | bash

-rclone config

-Enter n

-Enter a name.onedrive

-Enter onedrive

-Press Enter for client ID

-Press Enter for Client Secret

-Press n and enter for edit advanced config

-Enter y for auto config (if you are on the Pi Directly) or n if you are logged in remotely through SSH and then press enter

-A browser window will now open, log in with your Microsoft Account and select yes to allow OneDrive access.

-You will then see “success” and you can close the web browser

-Now choose 1 for OneDrive Personal or Business

-Now select the OneDrive you would like to use, you will probably only have one OneDrive linked to your account. This will be 0

-Now select y for yes

-Now select y for yes again to save the connection

-Close the terminal window

-In your OneDrive create a folder to sync Show Display Image

-First open a terminal and test your sync command. rclone sync -v onedrive:Show\ Display\ Image /home/pi/Driver. This command will sync   the “onedrive” connection “Documents” folder to your raspberry pi. The contents will be downloaded to you documents folder on the pi.     If successful you will see the terminal start downloading each file to the folder.

-For this method you need to login to the pi directly. Now lets make it automatic. If your comfortable with a text editor you can enter   this string into leafpad on the raspberry pi and save it as drive.sh rclone sync -v onedrive:Show\ Display\ Image /home/pi/Driver

-This file will call the connection and download any new files from OneDrive.
   Only follow if your Pi doesn’t have a Desktop installed (Headless) or you have installed Raspian Buster– Run crontab -e  in the terminal
   Select 2 for nano
   Enter the following string  * * * * * /home/pi/Drive.sh 
   Save the file ( usually Ctrl + O to save and Ctrl + X to exit) ,then skip to step 32

   please see it as reference
   URL:https://jarrodstech.net/how-to-raspberry-pi-onedrive-sync/


3 run kivy file  
 
   In terminal,sudo python3 ~/MyImage1.py
   For startup, you should write following command in terminal
   sudo nano /etc/profile
   In bottom line
   cd /home/pi && sudo python3 MyImage1.py




