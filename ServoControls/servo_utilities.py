from . import predefined_positions
from .servo import ServoController

def servoHandler(prediction):
    ServoController.set_angle(predefined_positions.POSITIONS[prediction])