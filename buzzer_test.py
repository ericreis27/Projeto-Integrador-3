import machine
from machine import Pin
import time

p13 = machine.Pin(13, machine.Pin.OUT)

print('Iniciando teste...')
time.sleep(2)

buzzer = machine.PWM(p13) 

buzzer.freq(1047)

while(1):
    print('looped')
    buzzer.freq(860)

    buzzer.duty(512) # Serve como controle de volume, max é 512

    time.sleep(2)

    buzzer.duty(0)

buzzer.deinit()