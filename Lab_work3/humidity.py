def setup():
    pinMode(A1, INPUT)
    Serial.begin(9600)

def loop():
    dvl = analogRead(A1)
    if dvl < 300:
        Serial.println("")
    if dvl > 700:
        Serial.println("")
    if dvl >= 300 and dvl <= 700:
        Serial.println("")
    delay(100)


