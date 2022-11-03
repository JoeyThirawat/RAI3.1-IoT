import spidev
import time

spi = spidev.Spidev()
spi.open(0,0)
spi.max_speed_hz = 1000000

ch = 0
while True:
    raw = spi.xfer2([1, (ch<<4) | 0x80, 0])
    data = ((raw[1]&3)<<8 | raw[2])
    print ("ADC Output : "+str(data))
    time.sleep(1);
