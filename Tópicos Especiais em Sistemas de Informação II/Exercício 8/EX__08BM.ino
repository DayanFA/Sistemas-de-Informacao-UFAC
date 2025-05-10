#include <Wire.h>
void setup()
{
Wire.begin(); // Configura o barramento I2C
Serial.begin(9600); // Pino do Botão
}
void loop()
{
int leitura = analogRead(A0);
leitura = map(leitura, 0, 1023, 0, 179);
Wire.beginTransmission(15);
Wire.write(leitura); // Envia 1 byte
Wire.endTransmission();
delay(100);
}