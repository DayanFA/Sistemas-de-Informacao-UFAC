#include <SPI.h> // Biblioteca utilizada para comunicação com o Arduino

#include <Ethernet.h>

// A linha abaixo permite definir o endereço físico (MAC ADDRESS) da placa de rede.

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte ip[] = { 192, 168, 99, 2 }; // Define o endereço IP.
// Porta onde estará aberta para comunicação Internet e Arduino.

EthernetServer server(80);
String readString;
int led1 = 3;
int led2 = 4;

int led3 = 5; // Pino digital onde será ligado e desligado o LED.

void setup(){

pinMode(led1, OUTPUT); // Define o Pino 9 como saída.
pinMode(led2, OUTPUT); // Define o Pino 9 como saída.
pinMode(led3, OUTPUT); // Define o Pino 9 como saída.
Ethernet.begin(mac, ip); // Chama o MAC e o endereço IP da placa Ethernet.
// Inicia o servidor que esta inserido junto a placa Ethernet.

server.begin();
}
void loop() {

EthernetClient client = server.available();

if (client) {
while (client.connected()) {
if (client.available()) {
char c = client.read();
if (readString.length() < 100) {
readString += c;
}
if (c == '\n') {

client.println("HTTP/1.1 200 OK");
client.println("Content-Type: text/html");

client.println();

client.println("Acende LED <br />");

client.println("Projeto basico para demonstracao com Shield Ethernet <br />");

client.println("<hr>");

client.println("<a href=""Led1On"">Acender led 1</a><br />");
client.println("<a href=""Led1Off"">Apagar led 1</a><br />");

client.println("<hr>");

client.println("<a href=""Led2On"">Acender led 2</a><br />");
client.println("<a href=""Led2Off"">Apagar led 2</a><br />");

client.println("<hr>");

client.println("<a href=""Led3On"">Acender led 3</a><br />");
client.println("<a href=""Led3Off"">Apagar led 3</a><br />");

client.println("<hr>");

client.println("<a href=""AllOn"">Ligar todos</a><br />");
client.println("<a href=""AllOff"">Apagar todos</a><br />");

client.println("<hr>");
delay(1);
client.stop();

if(readString.indexOf("Led1On") > 0) {
digitalWrite(led1, HIGH); // Liga LED.

}

if(readString.indexOf("Led1Off") > 0) {
digitalWrite(led1, LOW); // Desliga LED.

}

if(readString.indexOf("Led2On") > 0) {
digitalWrite(led2, HIGH); // Liga LED.

}

if(readString.indexOf("Led2Off") > 0) {
digitalWrite(led2, LOW); // Desliga LED.

}

if(readString.indexOf("Led3On") > 0) {
digitalWrite(led3, HIGH); // Liga LED.

}

if(readString.indexOf("Led3Off") > 0) {
digitalWrite(led3, LOW); // Desliga LED.

}

if(readString.indexOf("AllOn") > 0) {
digitalWrite(led1, HIGH); // Desliga LED.
digitalWrite(led2, HIGH); // Desliga LED.
digitalWrite(led3, HIGH); // Desliga LED.

}

if(readString.indexOf("AllOff") > 0) {
digitalWrite(led1, LOW); // Desliga LED.
digitalWrite(led2, LOW); // Desliga LED.
digitalWrite(led3, LOW); // Desliga LED.

}
readString="";
}
}
}
}
}