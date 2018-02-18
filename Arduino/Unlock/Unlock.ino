#include <Servo.h>

// Serial reader variables
byte index = 0; // Index into array; where to store the character
const int maxChars = 4;
int input = 0;
char strValue[maxChars+1];

// Servo control variables
Servo myservo;
int servoPos = 0; 


void setup()
{
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(LED_BUILTIN, OUTPUT);
  myservo.attach(9);
}

void loop()
{
}


void serialEvent()
{
  readSerialPacket();
}

void unlock(){

  digitalWrite(LED_BUILTIN, HIGH);

  for (servoPos = 0; servoPos <= 180; servoPos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(servoPos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (servoPos = 180; servoPos >= 0; servoPos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(servoPos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }

  digitalWrite(LED_BUILTIN, LOW);
}

void readSerialPacket()
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
