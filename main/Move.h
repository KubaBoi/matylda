#include <Arduino.h>
#include <Servo.h>

#ifndef _MOVE_H_
#define _MOVE_H_

class Move {
  private:
    int _duration;
    int _finalAngle;
    int _step;
    bool _active;
  
  public:
    Servo servo;
  
    Move();

    void setUp(int duration, int finalAngle);
    void printServoInfo();

    void tick();

    int getAngle();
    void addAngle(int value);
    void setAngle(int value);
    bool isActive();

    void attachServo(int pin);
};

#endif
