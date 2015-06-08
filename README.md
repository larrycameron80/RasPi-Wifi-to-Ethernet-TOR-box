# RasPi-Wifi-to-Ethernet-TOR-box
Code to set up an TOR ethernet to wifi bridge with a Python command line switch

Please note the following.

I am a novice network/computing enthusiast and have limited understanding of the concepts used here.

The files contained here are purely for educational use and I have submitted them solely to demonstrate the things I have learnt, I accept no responsibility if things going wrong etc.

Requirements for the raspi are as follows:

- Ethernet cable
- Wifi USB 'card'
- tor (sudo apt-get install tor)
- chmod 775 all shell and python scripts

That said this small project is a concatenation of the ethernet to wifi bridge guide found here:

https://rbnrpi.wordpress.com/project-list/wifi-to-ethernet-adapter-for-an-ethernet-ready-tv/

and the TOR access point found here:

https://learn.adafruit.com/onion-pi/install-tor

Whilst I respect that the end 'product' might be easily implemented by just running tor on your computer, this just makes things a little more interesting. 

To start you will want the interfaces file, followed by the restiptables, setupiptables and setuproutes scripts. 

Modify your raspberry pi interfaces file to match the one here adding in your SSID and PSK where stated, then run restiptables, setupiptables and setuproutes (I have these stored in my /~ directory of my raspberry pi, you will need to make these executable i.e chmod 775 [script_name])

After this sudo reboot the pi and you should have an ethernet to wifi bridge working. (To test this connect your computer via ethernet and try to ping out)

The next step is to then run the runtor script (remember it needs to be executable)
This script will redirect your internet traffic through the TOR port 9040.

To enable switching this feature of the ethernet to wifi bridge on and off run the python script (ensure the .py file is saved in the same location as the runtor script).

Note, I ssh into my raspi from my linux desktop (ssh pi@....) then run the python script from there.

As stated in the Ada fruit tutorial you can check that this feature works by refreshing the IP chicken link.

Happy Days!





