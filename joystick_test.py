from machine import Pin, ADC
from time import sleep_ms
from time import sleep

x = ADC(Pin(32, Pin.IN))
y = ADC(Pin(33, Pin.IN))
joystick_button = Pin(25, Pin.IN, Pin.PULL_UP)

x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)

tea_options = [] # organizacao das tuplas dentro da lista será nome, temperatura, tempo
select_button = True # Flag para controle do fluxo de seleção do chá desejados

green_tea = ('Cha verde', 65,180)
black_tea = ('Cha preto', 80,300) 

tea_options.append(green_tea)
tea_options.append(black_tea)

counter = 0
print(len(tea_options))
while True:
    x_val = x.read()
    y_val = y.read()

    sleep_ms(200)
    
    if y_val > 3500:
        counter += 1
        
        if counter > (len(tea_options) - 1):        
            counter = 0


    if y_val < 350:
        counter -= 1

        if counter < 0:
            counter = 0

    print(tea_options[counter])

    button = joystick_button.value()

    if not button:
        print('selected option:')
        print('teste')
        sleep(5)
