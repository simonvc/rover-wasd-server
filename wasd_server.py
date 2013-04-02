#!/usr/bin/python

from pyfirmata import Arduino
from pyfirmata import SERVO
from time import sleep
from os import popen

from flask import Flask, Response
app = Flask(__name__)

#import SimpleCV

board = Arduino('/dev/ttyUSB0')


sleep(2)
Ptilt = 2
Ppan = 4

LeftForward = 3
LeftBack = 11
RightBack = 5
RightForward = 6

light = False

pan = 1228
tilt = 1278

board.digital[Ppan].mode = SERVO
board.digital[Ptilt].mode = SERVO

board.digital[Ptilt].write(tilt)
board.digital[Ppan].write(pan)

#webcam=SimpleCV.Camera()


@app.route("/hello")
def hello():
  return "Hello world"

#@app.route("/cam.jpg")
#def cam():
#  f=webcam.getImage().save('static/last.jpg')
#  return Response(open('static/last.jpg').read(), mimetype='image/jpeg')
########################## end setup ################



####################### pan tilt ####################


@app.route('/o')
def o():
  global pan
  global tilt
  tilt=tilt-50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))


@app.route('/l')
def l():
  global pan
  global tilt
  tilt=tilt+50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))

#  if c==';':
@app.route('/semicolon')
def semicolon():
  global pan
  global tilt
  pan=pan-50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


#  if c=='k':
@app.route('/k')
def k():
  global pan
  global tilt
  pan=pan+50
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


#  if c=='O':
@app.route('/O')
def O():
  global pan
  global tilt
  tilt=tilt-350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))



#  if c=='L':
@app.route('/L')
def L():
  global pan
  global tilt
  tilt=tilt+350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ptilt].write(tilt)
  return('%s, %s' % (pan, tilt))


#  if c==':':
@app.route('/colon')
def colon():
  global pan
  global tilt
  pan=pan-350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


#  if c=='K':
@app.route('/K')
def K():
  global pan
  global tilt
  pan=pan+350
  if tilt > 2400: tilt=2400 
  if tilt < 544: tilt=544
  if pan > 2400: pan=2400 
  if pan < 544: pan=544
  board.digital[Ppan].write(pan)
  return('%s, %s' % (pan, tilt))


############### motor controllers ###################
########################   w    ##########
@app.route("/w")
def w():
  print("w")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(1)
  board.digital[RightForward].write(1)
  return("w")

@app.route("/wup")
def wup():
  print("wup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("wup")
########################   a    ##########
@app.route("/a")
def a():
  print("a")
  board.digital[LeftBack].write(1)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(1)
  return("a")

@app.route("/aup")
def aup():
  print("aup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("aup")
########################   s    ##########
@app.route("/s")
def s():
  print("s")
  board.digital[LeftBack].write(1)
  board.digital[RightBack].write(1)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("s")

@app.route("/sup")
def sup():
  print("sup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("sup")
########################   d    ##########
@app.route("/d")
def d():
  print("d")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(1)
  board.digital[LeftForward].write(1)
  board.digital[RightForward].write(0)
  return("d")

@app.route("/dup")
def dup():
  print("dup")
  board.digital[LeftBack].write(0)
  board.digital[RightBack].write(0)
  board.digital[LeftForward].write(0)
  board.digital[RightForward].write(0)
  return("dup")

##################### w a ##################
@app.route("/wa")
def wa():
  print("wa")
  return("wwaaa")

@app.route("/waup")
def waup():
  print("waup")
  return("wwaaa")

##################### w d ##################
@app.route("/wd")
def wd():
  print("wd")
  return("wd")

@app.route("/wdup")
def wdup():
  print("wdup")
  return("wdup")

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
