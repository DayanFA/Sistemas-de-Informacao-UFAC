#define LED1 2
#define LED2 3
#define LED3 4
#define BOT 5
int LEITURA = LOW;
int ESTADO = 0;
void setup()
{
pinMode(LED1, OUTPUT);
pinMode(LED2, OUTPUT);
pinMode(LED3, OUTPUT);
pinMode(BOT, INPUT);
}
void loop()
{
LEITURA = digitalRead(BOT);
if (LEITURA == HIGH)
ESTADO = ESTADO + 1;
delay(100);
if (ESTADO == 1)
digitalWrite(LED1, HIGH);
if (ESTADO == 2)
digitalWrite(LED2, HIGH);
if (ESTADO == 3)
digitalWrite(LED3, HIGH);
if (ESTADO == 4) {
ESTADO = 0;
digitalWrite(LED1, LOW);
digitalWrite(LED2, LOW);
digitalWrite(LED3, LOW);
}
}