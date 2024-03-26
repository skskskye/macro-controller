const int key1 = 3;
const int key2 = 4;
const int key3 = 5;
const int key4 = 6;
const int key5 = 7;
const int key6 = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(key1, INPUT_PULLUP);
  pinMode(key2, INPUT_PULLUP);
  pinMode(key3, INPUT_PULLUP);
  pinMode(key4, INPUT_PULLUP);
  pinMode(key5, INPUT_PULLUP);
  pinMode(key6, INPUT_PULLUP);
}

void loop() {
  int key1State = digitalRead(key1);
  int key2State = digitalRead(key2);
  int key3State = digitalRead(key3);
  int key4State = digitalRead(key4);
  int key5State = digitalRead(key5);
  int key6State = digitalRead(key6);

  if(key1State == HIGH){
    Serial.println("0");
  }else{
    Serial.println("1");
  }

  if(key2State == HIGH){
    Serial.println("2");
  }else{
    Serial.println("3");
  }

  if(key3State == HIGH){
    Serial.println("4");
  }else{
    Serial.println("5");
  }

  if(key4State == HIGH){
    Serial.println("6");
  }else{
    Serial.println("7");
  }

  if(key5State == HIGH){
    Serial.println("8");
  }else{
    Serial.println("9");
  }

  if(key6State == HIGH){
    Serial.println("q");
  }else{
    Serial.println("w");
  }
}
