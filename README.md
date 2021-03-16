# COMS 3930: Creative Embedded Systems
## Module 3 – Installation Art <br> Spencer Bruce 

![Picture of Takeout Sound container](images/full.png)

### Included Files

I have uploaded, along with this README, the following files:
- a bluetooth.ino program to be run on an ESP32 microcontroller. This file is what  sends the matrix keypad inputs over Blutooth to my laptop.
- a piano.py to be run on a laptop or other output device. If using a Raspberry Pi, it must be able to play sounds through a connected speaker or external monitor in response to Blutooth serial input from the ESP32.

I decided to use Bluetooth instead of WiFi as my communication protocol between the ESP32 and my laptop. I had the unfortunate circumstance of emergency travel over spring break, so I had to adjust my code to work with Bluetooth instead of WiFi once I left campus. It ended up being not too bad, thanks to the starter code Achmmed posted in the Discord!

One issue I ran into was the inability to re-connect to the Bluetooth serial input without resetting ESP32 in between runs. This likely has to do with me Control-C-ing my Python code without correctly disconnecting from Bluetooth, but it was not too cumbersome to work around. 

A video of me using the PixelMask can be seen [here](https://youtu.be/jyS8_fwuTdA). 

### Creative Vision
I wanted Takeout Sounds to be a fun little toy like one I used to use growing up in the doctor's office waiting room. This toy was a small soundboard with different farm animals on it, and you could push on the farm animals to play their accompanying sound. I wanted Takeout sounds to be more applicable to the Youth™ of today, so I used some meme sounds I found on the internet. 

You can use any of the number keys to play a sound effect at that current timestep in the sound loop. By pressing the * or the # at the bottom of the keypad, you can change the tempo of the sound loop. By pressing A, B, C, or D on the right of the keypad, you can create an empty loop with 2, 4, 6, or 8 sound slots, respectively. 

In future iterations I would like to add the ability to adjust pitch for each sound, to make a sort  of mini MIDI controller. 

### Dependencies
I used the following items to create this project: 
- 1 x ESP32 microcontroller 
- 1 x matrix keypad
- 1 x plastic takeout container
- 1 x 3.7V 650 mAh LiPo battery
- 1 x micro-USB cable for flashing the ESP32
- Some wires
- Blue tape
- A craft knife 

In terms of Python packages, make sure you have the following installed: 
- playsound
- time
- serial 
- sys 
