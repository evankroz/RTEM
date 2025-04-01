#include <WiFi.h>

const char* ssid = "NetName"
const char* pass = "NewPass"
WiFiServer server(8080);

void setup(){
    Serial.begin(115200);
    WiFi.begin(ssid, pass);

    while (WiFi.stats() != WL_CONNECTED) delay(500);
    server.begin();
}
