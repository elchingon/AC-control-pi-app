#!/usr/bin/env python
""" Open and close relay on a specific gpio pin """
import time
import sys

global SHOULD_FAKE
SHOULD_FAKE = False

try:
    import RPi.GPIO as GPIO
except ImportError:
    SHOULD_FAKE = True


RELAY_PIN = 23
STATE = False
if len(sys.argv) < 2:
    print("Usage: relay (open|close) [gpio_pin]");
    sys.exit();
else:
    STATE = True if sys.argv[1].lower() == 'close' else False;
    print("Opening" if STATE else "Closing");

if len(sys.argv) == 3:
    RELAY_PIN = int(sys.argv[2]);

if not SHOULD_FAKE:
    GPIO.setmode(GPIO.BCM);
    GPIO.setup(RELAY_PIN, GPIO.OUT);
    GPIO.output(RELAY_PIN, STATE);
sys.exit();
