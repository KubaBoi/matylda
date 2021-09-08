#include <Servo.h>
#include <Wire.h>
#include "AnimationManager.h"

# define I2C_SLAVE_ADDRESS 0x04
#define PAYLOAD_SIZE 2

volatile boolean receiveFlag = false;
char temp[32];
String command;

AnimationManager manager(1);

void setup()
{
  Wire.begin(I2C_SLAVE_ADDRESS);
  Serial.begin(9600); 
  delay(1000);               
  //Wire.onRequest(requestEvents);
  Wire.onReceive(receiveEvents);
  
  pinMode(13, OUTPUT);

  manager.setUp(3);
}

void loop()
{
  manager.runManager();
  //manager.getActualAngle(4);
  
  //delay(100);

  if (receiveFlag == true) {
    Serial.println("Recieved: " + String(temp));
    setMove();
    receiveFlag = false;
  }
}

void setMove() {
  String c = String(temp);
  int servo = getValue(c,',',0);
  int duration = getValue(c,',',1);
  int finalAngle = getValue(c,',',2);
  manager.setMove(servo, duration, finalAngle);
}

int getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return (found>index ? data.substring(strIndex[0], strIndex[1]) : "").toInt();
}

/*void requestEvents(int message) {
  Wire.write(message);
}*/

void receiveEvents(int howMany) {

  for (int i = 0; i < howMany; i++) {
    temp[i] = Wire.read();
    temp[i + 1] = '\0'; //add null after ea. char
  }

  //RPi first byte is cmd byte so shift everything to the left 1 pos so temp contains our string
  for (int i = 0; i < howMany; ++i)
    temp[i] = temp[i + 1];

  receiveFlag = true;
}
