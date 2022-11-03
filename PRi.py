import _thread
import RPi.GPIO as GPIO
import time

LED_OUT_1 = 26
LED_OUT_2 = 19
LED_OUT_3 = 13

BUTTON_IN = 6

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_OUT_1, GPIO.OUT)
GPIO.setup(LED_OUT_2, GPIO.OUT)
GPIO.setup(LED_OUT_3, GPIO.OUT)
GPIO.setup(BUTTON_IN, GPIO.IN)

GPIO.output(LED_OUT_1, True)
GPIO.output(LED_OUT_2, True)
GPIO.output(LED_OUT_3, True)

count = 0

'''
while True:
    i = GPIO.input(BUTTON_IN)
    print(i)

'''

def thread1_def(arg0, arg1):
    

_thread.start_new_thread(thread1_def, (arg0, arg1))

def button_irq(ch):
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


while True:
    i = GPIO.input(BUTTON_IN)
    #print(i)
    if (i==1):while True:
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
        count += 1
        if(count == 1):
            GPIO.output(LED_OUT_1, False)
            GPIO.output(LED_OUT_2, True)
            GPIO.output(LED_OUT_3, Truwhile True:
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
            count = 0e)
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
    
    
    
    '''
    time.sleep(0.5);
    
    GPIO.output(LED_OUT_1, True)
    GPIO.output(LED_OUT_2, False)
    GPIO.output(LED_OUT_3, True)
    time.sleep(0.5);
    
    GPIO.output(LED_OUT_1, True)
    GPIO.output(LED_OUT_2, True)
    GPIO.output(LED_OUT_3, False)
    time.sleep(0.5);
    
    
    
    GPIO.output(LED_OUT_1, False)
    GPIO.output(LED_OUT_2, False)
    GPIO.output(LED_OUT_3, True)
    time.sleep(0.5);
    
    GPIO.output(LED_OUT_1, True)
    GPIO.output(LED_OUT_2, False)
    GPIO.output(LED_OUT_3, False)
    time.sleep(0.5);
    
    GPIO.output(LED_OUT_1, False)
    GPIO.output(LED_OUT_2, True)
    GPIO.output(LED_OUT_3, False)
    time.sleep(0.5);
    
    
    GPIO.output(LED_OUT_1, False)
    GPIO.output(LED_OUT_2, False)
    GPIO.output(LED_OUT_3, False)
    time.sleep(3);
    '''

