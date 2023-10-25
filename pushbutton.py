import RPi.GPIO as GPIO
import os

# GPIO pin
BUTTON_PIN = 18

def button_callback(channel):
	print("Nice Push!!")
	os.system('raspistill -o /home/nakanishi/photo/jpg')
	print("photo complete!")

# BCM mode
GPIO.setmode(GPIO.BCM)

# pull up
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set event
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
	input("Press Button!")
finally:
	GPIO.cleanup()
	print("Bye!")
