#include "Move.h"

Move::Move() {}

void Move::setUp(int duration, int finalAngle) {
  _duration = duration;
  _finalAngle = finalAngle;
  _step = (finalAngle - servo.read()) / duration;
  _active = true;
}

//lerp - linearni interpolace
// p = p1 + (p2 - p1)xU
void Move::tick() {
  if (isActive()) {
    if (servo.read() == _finalAngle) {
      printServoInfo();
      Serial.println(" STOP");
      _active = false;
      digitalWrite(13, LOW);
    }
    else {
      addAngle(_step);
      digitalWrite(13, HIGH);
    } 
  }
}

void Move::attachServo(int pin) {
  _pin = pin;
  servo.attach(pin);
}

int Move::getAngle() {
  printServoInfo();
  return servo.read();
}

bool Move::isActive() {
  return _active;
}

void Move::addAngle(int value) {
  printServoInfo();
  Serial.println(" Adding: " + String(value));
  int stat = servo.read() + value;
  servo.write(stat);
}
void Move::setAngle(int value) {
  printServoInfo();
  Serial.println(" Setting: " + String(value));
  servo.write(value);
}

void Move::printServoInfo() {
  Serial.print("Servo: " + String(_pin) + " angle: " + String(servo.read()));
}
