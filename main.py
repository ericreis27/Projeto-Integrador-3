import machine
import onewire
import ds18x20 
import time
import sys
from machine import Pin

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

# SETTINGS
ds_pin = machine.Pin(33)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
green_led = Pin(25, Pin.OUT)
yellow_led = Pin(26, Pin.OUT)
red_led = Pin(27, Pin.OUT)

# TEA OPTIONS AVAILABLE CURRENTLY
tea_options = [] # organizacao da tupla e nome, temperatura, tempo

green_tea = ('Chá verde', 65,180)
black_tea = ('Chá preto', 80,300) 

tea_options.append(green_tea)
tea_options.append(black_tea)


# MAIN LOOP
red_led.on()
print('Bem vindo ao TeaWizard!')
time.sleep(1)
print('Selecione uma das opções de chá abaixo:')
time.sleep(0.4)

for index, tea in enumerate(tea_options):
    name, temperature, infusion_time = tea
    print(f'{index} -> {name} - {temperature}° - {infusion_time} segundos')
try:
    choice = int(input("Chá desejado: "))
except ValueError as exc:
    print('Valor inserido não é válido, tente novamente.')
    sys.exit()

if choice > len(tea_options):
    print('Valor inserido não é válido, tente novamente.')
    sys.exit()

chosen_tea_name, chosen_tea_temperature, chosen_tea_time = tea_options[choice]
print(chosen_tea_name, chosen_tea_temperature, chosen_tea_time)

roms = ds_sensor.scan()

print(f'iniciando preparo do {chosen_tea_name}')

time.sleep(3)

red_led.off()
yellow_led.on()

temp = 0

while(temp < chosen_tea_temperature):    
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print('Temperatura atual: ', temp)
        time.sleep(1)

    if(temp > 40):
        print('Temperatura acima de 35 graus')
        yellow_led.off()
        green_led.on()

print('Fim do teste')
sys.exit()
    