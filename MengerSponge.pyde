add_library('OBJExport')
from l_system import LSystem
from menger_l_system import MengerSpongeLSystem

record = False

def setup():
    global record
    global ds
    size(480, 480, P3D)
    ds = MengerSpongeLSystem()
    ds.simulate(2)
    
def draw():
    global record
    if record:
        beginRecord('nervoussystem.obj.OBJExport', 'filename.obj')
    background(255)
    translate(width/2, height/2, 0)
    if mousePressed:
        rotateY(mouseX/float(width))
        rotateX(mouseY/float(height))
    ds.render()
    if record:
        endRecord()
        print 'Saved!'
        record = False

def keyPressed():
    global record
    if key == 's':
        record = True
