#include "Move.h"

Move::Move() {}

void Move::setUp(int duration, int finalAngle) {
  //Servo servo;
  _duration = duration;
  _finalAngle = finalAngle;
  _step = (finalAngle - servo.read()) / duration;
  _active = true;
}

void Move::tick() {
  if (isActive()) {
    if (servo.read() == _finalAngle) {
      _active = false;
    }
    else {
      addAngle(_step);
    } 
  }
}

void Move::attachServo(int pin) {
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
  Serial.println("Adding: " + String(value));
  int stat = servo.read() + value;
  servo.write(stat);

  digitalWrite(13, LOW);
  digitalWrite(13, HIGH);
}
void Move::setAngle(int value) {
  printServoInfo();
  Serial.println("Setting: " + String(value));
  servo.write(value);

  digitalWrite(13, LOW);
  digitalWrite(13, HIGH);
}

void Move::printServoInfo() {
  Serial.println("Servo angle: " + String(servo.read()));
}
