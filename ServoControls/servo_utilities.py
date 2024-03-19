from . import predefined_positions
from . import servo

def servoHandler(prediction):
    servo.set_angle(predefined_positions.POSITIONS[prediction])