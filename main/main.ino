#include <Servo.h>
#include <Wire.h>
#include "AnimationManager.h"

# define I2C_SLAVE_ADDRESS 11
#define PAYLOAD_SIZE 2

AnimationManager manager(1);

void setup()
{
  Wire.begin(I2C_SLAVE_ADDRESS);
  Serial.begin(9600); 
  delay(1000);               
  Wire.onRequest(requestEvents);
  Wire.onReceive(receiveEvents);
  
  pinMode(13, OUTPUT);

  manager.setUp(3); 
  manager.setMove(1, 90, 90);
}

void loop()
{
  //manager.runManager();
  //manager.getActualAngle(4);
  
  //delay(100);
}

int n = 0;

void requestEvents()
{
  Serial.println(F("---> recieved request"));
  Serial.print(F("sending value : "));
  Serial.println(n);
  Wire.write(n);
}

void receiveEvents(int numBytes)
{  
  Serial.println(F("---> recieved events"));
  n = Wire.read();
  Serial.print(numBytes);
  Serial.println(F("bytes recieved"));
  Serial.print(F("recieved value : "));
  Serial.println(n);
}
