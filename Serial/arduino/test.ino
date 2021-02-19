void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  String msg = "";
  
  if(Serial.available() > 0) // returns how many packets are available to be read
  {
    
    msg = Serial.readString();
    Serial.print("Incoming message: ");
    Serial.print(msg);
  }
}
