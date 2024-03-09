import RPi.GPIO as GPIO
from time import sleep
from .predefined_positions import PIN

class ServoController:
    @staticmethod
    def __init__(self):
        """
        Initialize the ServoController with the specified GPIO pin.
        :param pin: GPIO pin number (BCM mode)
        """
        self.pin = PIN
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.pin, 50)  # 50 Hz frequency for servo control
        self.servo_pwm.start(0)  # Start PWM with duty cycle 0 (servo at center position)

    def set_angle(self, angle):
        """
        Set the servo angle.
        :param angle: Desired angle (0 to 180 degrees)
        """
        duty_cycle = (angle / 18) + 2  # Convert angle to duty cycle (2% to 12%)
        self.servo_pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.5)  # Allow time for servo to move

    def cleanup(self):
        """
        Clean up GPIO resources when done.
        """
        self.servo_pwm.stop()
        GPIO.cleanup()


# Example usage
if __name__ == "__main__":
    try:
        # Move servo to different angles
        ServoController.set_angle(90)  # Center position
        sleep(1)
        ServoController.set_angle(0)   # Leftmost position
        sleep(1)
        ServoController.set_angle(180)  # Rightmost position
        sleep(1)
    except KeyboardInterrupt:
        ServoController.cleanup()  # Release GPIO resources