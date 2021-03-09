//declairing variables needed for the analog potientometers and digtal inputs
int an0;
int an1;
int an2;
int an3;
int dval0;
int dval1;
int dval2;
int dval3;

//sets up digtal input and output pins, as well as sets the serial rate
void setup() {
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  Serial.begin(9600);
  

}


void loop() {
  if(Serial.available() ==0)//checks if serial is ready
  {
    String pystring=Serial.readStringUntil('\n'); //reads string from pi until newline
    if(pystring=="Pin8") // checks to see if string matches 
    {
      digitalWrite(8,HIGH); //sets output pin high
      delay(2500); // delay for 2.5 seconds
      digitalWrite(8,LOW);// sets the output low again
    }
    else if(pystring=="Pin9")
    {
      digitalWrite(9,HIGH);
      delay(2500);
      digitalWrite(9,LOW);
    }
    else if(pystring=="Pin10")
    {
      digitalWrite(10,HIGH);
      delay(2500);
      digitalWrite(10,LOW);
    }
    else if(pystring=="Pin11")
    {
      digitalWrite(11,HIGH);
      delay(2500);
      digitalWrite(11,LOW);
    }
    else{ // if portion of string does not equal any of the above execute
      dval0=digitalRead(2);// reads value of the digital input pin and stores it in variable
      dval1=digitalRead(3);
      dval2=digitalRead(4);
      dval3=digitalRead(5);
      an0=analogRead(A0); //reads and stores the vlaue on the anlog input pin
      an1=analogRead(A1);
      an2=analogRead(A2);
      an3=analogRead(A3);

      Serial.print(an0); //sends the analog inputs value to the pi
      Serial.print(","); // used to parse out the data into seperate pieces with the same line
      Serial.print(an1);
      Serial.print(",");
      Serial.print(an2);
      Serial.print(",");
      Serial.print(an3);
      Serial.print(",");
      Serial.print(dval0); //sends the digtal input reading to the pi
      Serial.print(",");
      Serial.print(dval1);
      Serial.print(",");
      Serial.print(dval2);
      Serial.print(",");
      Serial.print(dval3);
      Serial.print(",");
      Serial.print("\n"); //sends newline at the end of the serial being sent to the pi
      Serial.flush(); //clears serial
    }
  }

}
