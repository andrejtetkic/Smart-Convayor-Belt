import RPi.GPIO as GPIO
from time import sleep
from .predefined_positions import PIN

servo_pwm = None

def startServo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    servo_pwm = GPIO.PWM(PIN, 50)  # 50 Hz frequency for servo control
    servo_pwm.start(0)  # Start PWM with duty cycle 0 (servo at center position)
    return servo_pwm

def getServoPWM():
    global servo_pwm
    if servo_pwm is None:
        servo_pwm = startServo()
    return servo_pwm
    

def set_angle(angle):
    """
    Set the servo angle.
    :param angle: Desired angle (0 to 180 degrees)
    """
    servo_pwm = getServoPWM()
    duty_cycle = (angle / 18) + 2  # Convert angle to duty cycle (2% to 12%)
    servo_pwm.ChangeDutyCycle(duty_cycle)
    sleep(0.5)  # Allow time for servo to move
    GPIO.output(PIN, False)
    servo_pwm.ChangeDutyCycle(duty_cycle)


def cleanup():
    """
    Clean up GPIO resources when done.
    """
    servo_pwm = getServoPWM()
    servo_pwm.stop()
    GPIO.cleanup()


# Example usage
if __name__ == "__main__":
    try:
        # Move servo to different angles
        set_angle(90)  # Center position
        sleep(1)
        set_angle(0)   # Leftmost position
        sleep(1)
        set_angle(180)  # Rightmost position
        sleep(1)
    except KeyboardInterrupt:
        cleanup()  # Release GPIO resources