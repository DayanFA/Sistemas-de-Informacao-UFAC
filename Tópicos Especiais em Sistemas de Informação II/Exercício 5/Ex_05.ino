int potPin = A0;
int ledPins[5] = {2, 3, 4, 5, 6};
void setup() {
for (int i = 0; i < 5; i++) {
pinMode(ledPins[i], OUTPUT);
}
Serial.begin(9600);
}
void loop() {
int potValue = analogRead(potPin);
Serial.println(potValue);
int numLeds = 0;
if (potValue >= 100) {
numLeds = map(potValue, 0, 1023, 1, 5);
numLeds = constrain(numLeds, 1, 5);
}
for (int i = 0; i < 5; i++) {
if (i < numLeds) {
digitalWrite(ledPins[i], HIGH);
} else {
digitalWrite(ledPins[i], LOW);
}
}
delay(100);
}