import _thread
import RPi.GPIO as GPIO
import time

LED_OUT_1 = 26
LED_OUT_2 = 19
LED_OUT_3 = 13

LED_OUT_RED = 11
LED_OUT_GREEN = 9

BUTTON_IN = 6

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_OUT_1, GPIO.OUT)
GPIO.setup(LED_OUT_2, GPIO.OUT)
GPIO.setup(LED_OUT_3, GPIO.OUT)
GPIO.setup(LED_OUT_RED, GPIO.OUT)
GPIO.setup(LED_OUT_GREEN, GPIO.OUT)
GPIO.setup(BUTTON_IN, GPIO.IN)

GPIO.output(LED_OUT_1, True)
GPIO.output(LED_OUT_2, True)
GPIO.output(LED_OUT_3, True)
GPIO.output(LED_OUT_RED, True)
GPIO.output(LED_OUT_GREEN, True)

freq = 100
percent = 0
pwm = GPIO.PWM(LED_OUT_GREEN, freq)
pwm.start(percent)

def button_irq(BUTTON_IN):
    count = 0
    while True:
        i = GPIO.input(BUTTON_IN)
        #print(i)
        if (i==1):
            count += 1
            if(count == 1):
                GPIO.output(LED_OUT_1, False)
                GPIO.output(LED_OUT_2, True)
                GPIO.output(LED_OUT_3, True)
                print(count)
                time.sleep(0.5);
            elif(count == 2):
                GPIO.output(LED_OUT_1, True)
                GPIO.output(LED_OUT_2, False)
                GPIO.output(LED_OUT_3, True)
                print(count)
                time.sleep(0.5);
            elif(count == 3):
                GPIO.output(LED_OUT_1, True)
                GPIO.output(LED_OUT_2, True)
                GPIO.output(LED_OUT_3, False)
                print(count)
                time.sleep(0.5);
            elif(count == 4):
                GPIO.output(LED_OUT_1, False)
                GPIO.output(LED_OUT_2, False)
                GPIO.output(LED_OUT_3, True)
                print(count)
                time.sleep(0.5);
            elif(count == 5):
                GPIO.output(LED_OUT_1, True)
                GPIO.output(LED_OUT_2, False)
                GPIO.output(LED_OUT_3, False)
                print(count)
                time.sleep(0.5);
            elif(count == 6):
                GPIO.output(LED_OUT_1, False)
                GPIO.output(LED_OUT_2, True)
                GPIO.output(LED_OUT_3, False)
                print(count)
                time.sleep(0.5);
            elif(count == 7):
                GPIO.output(LED_OUT_1, False)
                GPIO.output(LED_OUT_2, False)
                GPIO.output(LED_OUT_3, False)
                print(count)
                time.sleep(0.5);
            elif(count == 8):
                GPIO.output(LED_OUT_1, True)
                GPIO.output(LED_OUT_2, True)
                GPIO.output(LED_OUT_3, True)
                print(count)
                time.sleep(0.5);
                count = 0

GPIO.add_event_detect(BUTTON_IN, GPIO.RISING, callback=button_irq, bouncetime=200)


def thread1_def():

    while True:
        # pwm.ChangeDutycycle(percent)
        # pwm.stop()
        for percent in range(0,101,1):
            pwm.ChangeDutyCycle(percent) # provide duty cycle in the range 0-100
            time.sleep(0.01)
        # time.sleep(0.5)
    
        for percent in range(100,-1,-1):
            pwm.ChangeDutyCycle(percent)
            time.sleep(0.01)
        # time.sleep(0.5)
        
_thread.start_new_thread(thread1_def,())
    
while True:
    GPIO.output(LED_OUT_RED, True)
    # GPIO.output(LED_OUT_GREEN, False)
    time.sleep(1);
    GPIO.output(LED_OUT_RED, False)
    # GPIO.output(LED_OUT_GREEN, True)
    time.sleep(1);