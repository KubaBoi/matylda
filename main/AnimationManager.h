#include <Arduino.h>
#include <Servo.h>
#include "Move.h"

#ifndef _ANIMATIONMANAGER_H_
#define _ANIMATIONMANAGER_H_

class AnimationManager {
  public:
    int SERVOCOUNT = 16;
    int MAXMOVES = 20;

    int _delay;
    int _movesCount;
    
    Move moves[16];
    
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
