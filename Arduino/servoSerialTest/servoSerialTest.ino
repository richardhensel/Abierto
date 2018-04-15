#include <Servo.h>

// Serial reader variables
byte index = 0; // Index into array; where to store the character
const int maxChars = 3;
int input = 0;
char strValue[maxChars+1];

// Servo control variables
Servo myservo;
int servoPos = 0; 


void setup()
{
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(LED_BUILTIN, OUTPUT);
  myservo.attach(3);
}

void loop()
{
}


void serialEvent()
{
  readSerialPacket();
}

void setServo(int posit){

  digitalWrite(LED_BUILTIN, HIGH);


  myservo.write(posit);              // tell servo to go to position in variable 'pos'


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

        int intValue = value.toInt();
        Serial.println(String(intValue));
        //if (intValue >= 0 && intValue <= 180) {
          //Serial.println("2001.");
          setServo(intValue);
        //} else {
         // Serial.println("2000.");
        //}
   
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
