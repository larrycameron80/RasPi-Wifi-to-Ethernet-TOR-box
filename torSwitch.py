#! /usr/bin/env python

import subprocess

def main():
   print("Do you wish to redirect TCP traffic through TOR on (Y/N)")
   input = raw_input("> ")
   if input == "Y":
    tor_on()
   elif input == "N":
    tor_off()
   else:
    print('Invalid argument please enter Y or N ')
    main()

def tor_on():
 subprocess.call(['./runtor'])
