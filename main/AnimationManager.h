#include <Arduino.h>
#include <Servo.h>
#include "Move.h"

#ifndef _ANIMATIONMANAGER_H_
#define _ANIMATIONMANAGER_H_

class AnimationManager {
  public:
    int SERVOCOUNT = 6;
    int MAXMOVES = 20;

    int _delay;
    int _movesCount;
    
    int pins[6] = {3, 5, 6, 9, 10, 11};
    Move moves[6];
    
    AnimationManager(int i);
    
    void setUp(int del);
    void printServoInfo(int servo);
    
    void runManager();
    int getAngle(int servo);
    void addAngle(int servo, int value);
    void setAngle(int servo, int value);
    void setMove(int servo, int duration, int finalAngle); 
};

#endif
