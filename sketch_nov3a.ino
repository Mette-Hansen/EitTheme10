#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
//Globals
String dataLabel = "X,Y,Z"; 
bool label = true;

void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10);

  // Try to initialize!
  if (!mpu.begin()) {
    while (1) {
      delay(10);
    }
  }
}

void loop() {
  //Print out colum header
  while (label) {
    Serial.println(dataLabel);
    label = false;
  }

  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  Serial.print(a.acceleration.x);
  Serial.print(",");
  Serial.print(a.acceleration.y);
  Serial.print(",");
  Serial.println(a.acceleration.z - 9.82);
  delay(500);
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
//Globals
String dataLabel = "X,Y,Z"; 
bool label = true;

void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10);

  // Try to initialize!
  if (!mpu.begin()) {
    while (1) {
      delay(10);
    }
  }
}

void loop() {
  //Print out colum header
  while (label) {
    Serial.println(dataLabel);
    label = false;
  }

  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  Serial.print(a.acceleration.x);
  Serial.print(",");
  Serial.print(a.acceleration.y);
  Serial.print(",");
  Serial.println(a.acceleration.z - 9.82);
  delay(500);
}