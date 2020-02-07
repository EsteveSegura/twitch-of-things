void setup(){
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
    while (!Serial);
    Serial.println("BOARD_ON");
}

void loop(){
    if(Serial.available()){ 
        char state = Serial.read();

        if(state == 'E'){
            encenderLed();
        }

        if(state == 'A'){
            apagarLed();
        }
    }
}

void encenderLed(){
    digitalWrite(LED_BUILTIN,HIGH);
}

void apagarLed(){
    digitalWrite(LED_BUILTIN,LOW);
}
