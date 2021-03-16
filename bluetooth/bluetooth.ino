//#include <math.h>
#include <Keypad.h>
#include "BluetoothSerial.h"

BluetoothSerial SerialBT;
char keys[4][4] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[4] = {14, 27, 26,  25};
byte colPins[4] = {13, 21, 22,  23};

Keypad kp = Keypad(makeKeymap(keys), rowPins, colPins, 4, 4);
char holdKey;
unsigned long t_hold;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32");
}

void loop(){
  char key = kp.getKey();
  
   if (key){
     holdKey = key;
     Serial.println(key);
     SerialBT.println(key);
   }
   else if (kp.getState() == HOLD) {
      if ((millis() - t_hold) > 1 ) {
          t_hold = millis();
          SerialBT.println(holdKey);
          Serial.println(holdKey);
      }
   }
   else {
      SerialBT.println(" ");
      Serial.println(" ");
   }
   delay(100);
}
