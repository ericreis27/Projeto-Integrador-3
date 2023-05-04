import machine, onewire, ds18x20, time
from machine import Pin

ds_pin = machine.Pin(33)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
green_led = Pin(25, Pin.OUT)
yellow_led = Pin(26, Pin.OUT)
red_led = Pin(27, Pin.OUT)

roms = ds_sensor.scan()
print('Found DS devices: ', roms)
green_led = Pin(25, Pin.OUT)
yellow_led = Pin(26, Pin.OUT)
red_led = Pin(27, Pin.OUT)
print('iniciando loop principal')
red_led.on()
time.sleep(5)
red_led.off()
yellow_led.on()
while(1):    
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print('Temperatura atual: ', temp)
        print(type(temp))
    time.sleep(1)
    if(temp > 35): # 35 graus foi uma temperatura de teste escolhida randomicamente
        print('Temperatura acima de 35 graus')
        yellow_led.off()
        green_led.on()

    