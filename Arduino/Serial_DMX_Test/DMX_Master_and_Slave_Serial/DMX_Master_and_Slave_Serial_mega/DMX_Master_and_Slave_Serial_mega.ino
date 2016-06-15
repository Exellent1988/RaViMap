

#include <Conceptinetics.h>
#include <DmxSimple.h>

int channels_with_vals[128] = {0};

int number_of_channels = 10;

#define DMX_SLAVE_CHANNELS   number_of_channels


#define INPUT_SIZE ((number_of_channels*3)+number_of_channels)
DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void initalisierung() {
  DmxSimple.maxChannel(number_of_channels);
  dmx_slave.enable();
  dmx_slave.setStartAddress (1);
}

void receiving() {
  digitalWrite(2, LOW);

    for (int i = 1; i <= number_of_channels; i++) {
          Serial1.print(dmx_slave.getChannelValue(i));
          
          Serial1.print(",");
    }
    Serial1.println(" ");
  }

void sending() {
  digitalWrite(2, HIGH);
  for (int i = 0; i <= sizeof(channels_with_vals); i++) {
    DmxSimple.write( i+1, channels_with_vals[i] );
  }

}


void read_values() {
  char input[INPUT_SIZE + 1];
  byte size = Serial1.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;
  int channelid = 0;
  char* command = strtok(input, "&");
  while (command != 0)
  {
    int value = atoi(command);
    channels_with_vals[channelid] = value;
    // Find the next command in input string
    command = strtok(0, "&");
    channelid++;
  }
    sending();
    delay(1500);
}

void setup() {
  pinMode(2, OUTPUT);
  DmxSimple.usePin(3);

  //set SoftwareSerial
  Serial1.begin(115200);
  Serial1.setTimeout(250);
  initalisierung();
  Serial1.println("HY PI I'm Version 3");

}
void loop() {

  if (Serial1.available() > 0) {
    read_values();
  }
  else {
    receiving();
  }

}
