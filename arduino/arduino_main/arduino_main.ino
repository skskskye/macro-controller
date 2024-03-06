const int buttonPin = 3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if(buttonState == HIGH){
    Serial.println("0");
  }else{
    Serial.println("1");
  }
}
