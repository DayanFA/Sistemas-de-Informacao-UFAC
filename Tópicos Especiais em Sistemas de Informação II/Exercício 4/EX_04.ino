const int buttonPin = 3;
const int ledPin = 2;
const int buzzerPin = 4;
const int ldrPin = A0;
bool alarmActive = false;
bool lastButtonState = HIGH;
void setup() {
pinMode(buttonPin, INPUT_PULLUP);
pinMode(ledPin, OUTPUT);
pinMode(buzzerPin, OUTPUT);
Serial.begin(9600);
}
void loop() {
bool buttonState = digitalRead(buttonPin);
if (buttonState == LOW && lastButtonState == HIGH) {
alarmActive = !alarmActive;
delay(300);
}
lastButtonState = buttonState;

digitalWrite(ledPin, alarmActive ? HIGH : LOW);

int ldrValue = analogRead(ldrPin);
Serial.println(ldrValue);
int lightThreshold = 500;
if (alarmActive) {
if (ldrValue > lightThreshold) {
digitalWrite(buzzerPin, HIGH);
} else {
digitalWrite(buzzerPin, LOW);
}
} else {
digitalWrite(buzzerPin, LOW);
}
}