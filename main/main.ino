#include <Servo.h>     //zahrnutí knihovny pro ovládání servo motoru
#include "AnimationManager.h"
int pos = 0;           
int input = 7;

AnimationManager manager(1);

void setup()
{
  pinMode(input, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);

  manager.setUp(3); 
  manager.setMove(1, 90, 90);
}

bool t = true;
int s = 0;
void loop()
{
  manager.runManager();
  //manager.getActualAngle(4);
  
  //delay(100);
}
