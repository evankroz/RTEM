#include "HX711.h"

HX711 scale;

uint8_t dataPin = 3;
uint8_t clockPin = 2;
int relay = 7;
//bool firesent = false;

void setup() {
  pinMode(relay, OUTPUT);
  digitalWrite(relay, LOW);


  Serial.begin(115200);

  scale.begin(dataPin, clockPin);
  scale.set_scale(100.319198);  // Calibrate this value for your setup
  scale.tare();


  digitalWrite(relay, HIGH);
  delay(600);  // Keep firing relay on for 500 ms
  digitalWrite(relay, LOW);
}

void loop() {

  float weight = scale.get_units();
  if (abs(weight) > 0.8) {               // Adjust this threshold as needed
    weight = (weight / 1000) * 9.80665;  // Converting grams to Newtons
    Serial.println(weight, 5);
  } else {
    Serial.println(0.00000, 5);
  }

  // No delay here to allow for rapid measurements
}
