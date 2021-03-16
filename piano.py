import time
import playsound
import serial
import sys

sounds = ["sounds/tock.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3"]

ser = False
while not ser:
    try: 
        ser = serial.Serial("/dev/cu.ESP32-ESP32SPP",115200)
    except:
        print("Could not connect to ESP32, trying again")

for i in range(19):
    ser.readline()

i = 0
waitfor = 0.5
lastadded = ""
while True:   
    ser.flushInput()
    ser.flushOutput()
    line = str(ser.readline())[2:-5]
    # line=str(ser.readline())
    print(line)
    if line == "*" and len(sounds) > 1:
        waitfor =  max((0, waitfor - 0.25))
    elif line == "#":
        waitfor +=  0.25
    if line.isdigit() and line != lastadded:
        lastadded = line
        sounds[i] = f"sounds/{line}.mp3"
    if line == "A":
        waitfor = 0.5
        sounds = ["sounds/tock.mp3","sounds/tick.mp3"]
    elif line == "B":
        waitfor = 0.5
        sounds = ["sounds/tock.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3"]
    elif line == "C":
        waitfor = 0.5
        sounds = ["sounds/tock.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3"]
    elif line == "D":
        waitfor = 0.5
        sounds = ["sounds/tock.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3","sounds/tick.mp3"]
    try: 
        playsound.playsound(sounds[i])
    except:
        3
    time.sleep(waitfor)
    i = (i+ 1)%len(sounds)

  

