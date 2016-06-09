import serial
import time
from conf import *
from threading import Thread

#Initializing
channel_buffer = range(0, 128)
for x in xrange(0, 128):
            channel_buffer[x] = 0

last_received = ''

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

def build_array(channels=512, value=0, kind='serial', single=False):
    "Produces an array for each DMX Channel"
    _array = range(0, channels)
    kette = ""
    if not single:
        for x in xrange(0, channels):
            _array[x] = value
    else:
        _array[channels] = value

    if kind == 'serial':
        first = True
        for x in xrange(0, channels):
            _array[x] = str(_array[x])
            if first:
                kette = str(_array[x])
                first = False
            else:
                kette = kette+'&'+str(_array[x])
    print(kette)
    return (kette+'\n').encode('ascii')


def rgbw_values_to_channel_buffer(data):
    "Setzt empfangene werte in den channel buffer"
    global channel_buffer
    channel_buffer[1] = data[0]['l']
    channel_buffer[2] = data[0]['r']
    channel_buffer[3] = data[0]['g']
    channel_buffer[4] = data[0]['b']
    channel_buffer[5] = data[0]['w']
    channel_buffer[6] = data[0]['str']

def send_serial_data(channels, value):
    "Sends a values to DMX channel_buffer via Serial"
    ser.write(chr(13).encode('ascii'))
    ser.write(build_array(channels, value, 'serial'))


def send_rgbw():
    global channel_buffer
    rgbw_channel_buffer = str(channel_buffer[1])
    rgbw_channel_buffer = rgbw_channel_buffer+'&'+str(channel_buffer[2])
    rgbw_channel_buffer = rgbw_channel_buffer+'&'+str(channel_buffer[3])
    rgbw_channel_buffer = rgbw_channel_buffer+'&'+str(channel_buffer[4])
    rgbw_channel_buffer = rgbw_channel_buffer+'&'+str(channel_buffer[5])
    rgbw_channel_buffer = rgbw_channel_buffer+'&'+str(channel_buffer[6])
    ser.write(chr(13).encode('ascii'))
    ser.write(rgbw_channel_buffer.encode('ascii')) 
    print("Send RGBW DATA")     


def read_serial_data():
    "Reads the incomming Serial DATA"
    values = last_received
    dmx = values.split(',')
    print(dmx)
    return dmx



def receiving(seri):
    global last_received

    buffer_string = ''
    while True:
        buffer_string = buffer_string + seri.read(seri.inWaiting())
        if '\n' in buffer_string:
            lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer_string = lines[-1]


Thread(target=receiving, args=(ser,)).start()
