#include <Servo.h>
Servo meuServo;
const int pinSensor = 7;
const int pinServo = 5;

void setup() {
  Serial.begin(9600);
  meuServo.attach(pinServo);
  meuServo.write(0);
}

void loop() {
  long duracao;
  int distancia;
  
  pinMode(pinSensor, OUTPUT);
  digitalWrite(pinSensor, LOW);
  delayMicroseconds(2);
  digitalWrite(pinSensor, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinSensor, LOW);
  pinMode(pinSensor, INPUT);
  duracao = pulseIn(pinSensor, HIGH);
  distancia = duracao * 0.034 / 2;
  
  Serial.print("Distância: ");
  Serial.print(distancia);
  Serial.println(" cm");
  
  if (distancia > 0 && distancia <= 30) {
    meuServo.write(90);
    Serial.println("Porta Aberta");
    while (true) {
      pinMode(pinSensor, OUTPUT);
      digitalWrite(pinSensor, LOW);
      delayMicroseconds(2);
      digitalWrite(pinSensor, HIGH);
      delayMicroseconds(10);
      digitalWrite(pinSensor, LOW);
      pinMode(pinSensor, INPUT);
      duracao = pulseIn(pinSensor, HIGH);
      distancia = duracao * 0.034 / 2;
      
      Serial.print("Distância: ");
      Serial.print(distancia);
      Serial.println(" cm");
      
      if (distancia > 30) break;
      delay(500);
    }
    delay(3000);
    pinMode(pinSensor, OUTPUT);
    digitalWrite(pinSensor, LOW);
    delayMicroseconds(2);
    digitalWrite(pinSensor, HIGH);
    delayMicroseconds(10);
    digitalWrite(pinSensor, LOW);
    pinMode(pinSensor, INPUT);
    duracao = pulseIn(pinSensor, HIGH);
    distancia = duracao * 0.034 / 2;
    
    if (distancia > 30) {
      meuServo.write(0);
      Serial.println("Porta Fechada");
    }
  }
  delay(500);
}
