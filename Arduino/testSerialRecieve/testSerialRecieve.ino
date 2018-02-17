String a;

// Parameters for the serial listener.
byte index = 0; // Index into array; where to store the character
const int maxChars = 4;
int input = 0;
char strValue[maxChars+1];


void unlock(){
  digitalWrite(14, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);                       // wait for a second
  digitalWrite(14, LOW);    // turn the LED off by making the voltage LOW
  digitalWrite(LED_BUILTIN, LOW);
}

void flushRead(){
  while (Serial.available()){
    Serial.read();
  }
}

void setup() {

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(14, OUTPUT);
}

void loop() {

  //Serial.print("current internal Value: ");
  //Serial.println(strValue);
  //Serial.print("current index: ");
  //Serial.println(index);
  //delay(2000);

//  //while(Serial.available()) {
//  //if (Serial.available()){
//    delay(10); 
//  }
//  
//  a= Serial.readString();// read the incoming data as string
//  flushRead();
//  Serial.print(a.length());
//  //Serial.print("\n"); 
//  if (a=="unlock"){
//    Serial.println("unlock"); 
//    //Serial.print("\n");
//    unlock(); 
//
//     
//  }
//  else {
//    Serial.println("do nothing");
//    //Serial.print("\n");
//  }
//  
//  //}
  

}


void serialEvent()
{
  while (Serial.available())
  {
    char ch = Serial.read();
    //Serial.println(ch);

    if (isDigit(ch)) {
      if (index < maxChars) {
        strValue[index++] = ch;

      } else {
        //Serial.println("Too many digits before separator");
        Serial.println("1002.");
        clearInput();
      }
    } else {
      if (index == maxChars) {
        
        String value;
        value = String(value + strValue);
        if (value == "9000") {
          Serial.println("2001.");
          unlock();
        } else {
          Serial.println("2000.");
        }
        //input = atoi(strValue);
        //Serial.print("input is: ");
        //Serial.println(strValue);

        

        //setPpm();        
        clearInput();
      } else {
        //Serial.println("Too few digits before separator");
        Serial.println("1002.");
        clearInput();
      }
    }
  }
}

void clearInput()
{
  input = 0;
  index = 0;
}
