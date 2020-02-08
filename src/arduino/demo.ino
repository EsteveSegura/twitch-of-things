void setup(){
    pinMode(LED_BUILTIN, OUTPUT); // Our led
    Serial.begin(9600); // Starting serial with 9600baud
    while (!Serial);
}


void loop(){
     // If comunication is active ...
    if(Serial.available()){ 
        char state = Serial.read(); // get the values

        // If state is E... turn on the Led
        if(state == 'E'){
            encenderLed();
        }

        // If state is A... turn off the Led
        if(state == 'A'){
            apagarLed();
        }
    }
}

// The logic and functions of our program and hardware
void encenderLed(){
    digitalWrite(LED_BUILTIN,HIGH);
}

void apagarLed(){
    digitalWrite(LED_BUILTIN,LOW);
}