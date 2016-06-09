from conf import *
from DMX_data_handler import *
from socketIO_client import SocketIO
import pygame

socketIO = SocketIO(SERVER, PORT)
global paused
paused = False;


def on_checkbox_response(*args):
        data = args[0]
        print data["value"]


def send_dmx_channels(*arguments):
    "Sends DMX Channel range to 0"
    send_serial_data(256, 0)
    print "something should happen"

def send_dmx_rgbw(*data):
    "Sendet DMX RGBW werte"
    rgbw_values_to_channel_buffer(data)
    send_rgbw()
    print('Sende rgbw')

def send_dmx_channels_with_values(*data):
    "Sends DMX Channel range"
    send_serial_data(10, data[0]["value"])
    print "something should happen"


def send_websocket(which, *data):
    "Sends data trough Websocket on 'which' call"
    socketIO.emit(which, {'data': data})


def get_channel_values():
    "Sends receiving_channel values via broadcast"
    socketIO.emit('channels', {'all': read_serial_data()})


def play_anything(file="/home/pi/ITS_2016/music/test/test.mp3"):
    global paused
    if not paused:
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        paused = False
       # while pygame.mixer.music.get_busy() == True:
        #continue
    else:
        pygame.mixer.music.unpause()
        paused = False
    


def pause_anything():
    "Pausiert die Music"
    global paused
    pygame.mixer.music.pause()
    paused = True


def music_volume(data):
    volume =int(data['v'])/100.00
    pygame.mixer.music.set_volume(volume)


def set_lumination(data):
    global channel_buffer
    channel_buffer[1] = data['l'];
    send_rgbw()


def set_strobe(data):
    global channel_buffer
    channel_buffer[6] = data['str'];
    send_rgbw()


def receive_websockets():
    "Collects Websocket data and calls the right function"
#    socketIO.on('slider1', slider1_call)
    socketIO.on('checkbox', send_dmx_channels)
    socketIO.on('lampe', send_dmx_channels_with_values)
    socketIO.on('get_channel_values', get_channel_values)
    socketIO.on('rgbw_dmx',send_dmx_rgbw)
    socketIO.on('play_anything',play_anything)
    socketIO.on('pause_anything',pause_anything)
    socketIO.on('volume',music_volume)
    socketIO.on('lumi', set_lumination)
    socketIO.on('strobe', set_strobe)
    socketIO.wait()
