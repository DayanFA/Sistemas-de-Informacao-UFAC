#include <Wire.h>
#include <Servo.h>
#define SERVO 10
Servo meuservo;
int Leitura = 0;
void setup()
{
Serial.begin(9600);
meuservo.attach(SERVO);
Wire.begin(15); //Barramento I2C do endereço 15
Wire.onReceive(receiveEvent); //Recepção de dados
}
void loop()
{
delay(100);
}
void receiveEvent(int howMany)
{
int x = Wire.read(); //recebe um byte do tipo inteiro
meuservo.write(x);
}