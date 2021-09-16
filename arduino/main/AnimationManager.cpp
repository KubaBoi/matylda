#include "AnimationManager.h"

/*
 * funkcni indexy
 * 1, 3, 4, 7, 8, 9
 */

AnimationManager::AnimationManager(int del) {}

//pripoji vsechna serva k pinum
void AnimationManager::setUp(int del) {
  _delay = del;
  _movesCount = 0;

  for (int i = 0; i < SERVOCOUNT; i++) {
    moves[i].attachServo(pins[i]);
    moves[i].setAngle(0);
  }
}

//loop
void AnimationManager::runManager() {
  for (int i = 0; i < SERVOCOUNT; i++) {
    moves[i].tick();
  }
}

int AnimationManager::getAngle(int servo) {
  return moves[servo].getAngle();
}

void AnimationManager::addAngle(int servo, int value) {
  moves[servo].addAngle(value);
}

void AnimationManager::setAngle(int servo, int value) {
  moves[servo].setAngle(value);
}

void AnimationManager::setMove(int servo, int duration, int finalAngle) {
  moves[servo].setUp(duration, finalAngle);
}

void AnimationManager::printServoInfo(int servo) {
  moves[servo].printServoInfo();
}
