

#include <Conceptinetics.h>
#include <SoftwareSerial.h>
#include <DmxSimple.h>
SoftwareSerial mySerial(10, 11); // RX, TX
int number_of_channels = 256;
int channels_with_vals[512] = {0};
#define DMX_SLAVE_CHANNELS   number_of_channels 
#define INPUT_SIZE 1024

DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void setup() {             
 pinMode(2, OUTPUT);
 DmxSimple.usePin(3);
 
  //set SoftwareSerial
   mySerial.begin(115200);
   mySerial.setTimeout(1000);
  
 mySerial.println("HY PI How are you???!!!!");
   delay(2000);
   dmx_slave.enable();
   dmx_slave.setStartAddress (1);
   
   
 
}

void loop(){
  if (mySerial.available() > 0){
    read_values();
  }
  else{ 
 receiving();
}
}

void receiving(){
  
  digitalWrite(2, LOW);   
  for(int i=1;i<=DMX_SLAVE_CHANNELS;i++){
  mySerial.print(dmx_slave.getChannelValue(i) );
  mySerial.print(",");
  }
  mySerial.println(" ");
}
void sending(){
  digitalWrite(2, HIGH);
  for(int i=0;i<=number_of_channels;i++){
    DmxSimple.write( i+1, channels_with_vals[i] );
  }
    
}


void read_values(){ 
int set_1 = 0
int set_2 = 0
int set_3 = 0

 while (char x = mySerial.read() != null){
    switch x{
      case ':':
      set_1 = 0
      case isDigit(x):
        if (set_1 !=0)
          value = x;
        else if (set_2 !=0){
          value= x*10;
          set_2 =1
        }else
          value= x*100; 
    }
     mySerial.println(" SEND DATA");
     mySerial.println(inputs);
  sending();  
}

