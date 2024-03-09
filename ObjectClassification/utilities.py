from Logger.logger import PredictionLogger

import sys
import os

# Get the absolute path to the parent directory of your project
project_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_parent_dir)

from ServoControls.servo_utilities import servoHandler

def printState(count):
    print(f"Option 1: {count[0]} passed; Option 2: {count[1]} passed; Option 3: {count[2]} passed")


def predictionHandler(choice):
    servoHandler(choice)
    PredictionLogger.log_prediction(choice)
    PredictionLogger.update_count(choice)