import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from machine import Pin, ADC
from time import sleep_ms

x = ADC(Pin(32, Pin.IN))
y = ADC(Pin(33, Pin.IN))
joystick_button = Pin(25, Pin.IN, Pin.PULL_UP) 
x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #Inicialização do I2C

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

tea_options = [] # organizacao da tupla e nome, temperatura, tempo
select_button = True # Flag para controle do fluxo de seleção do chá desejados

green_tea = ('Cha verde', 65,180)
black_tea = ('Cha preto', 80,300) 

tea_options.append(green_tea)
tea_options.append(black_tea)

while True:
    lcd.putstr('    Bem vindo   ')
    lcd.putstr('  ao TeaWizard  ')
    sleep(1)
    lcd.clear()
    lcd.putstr('Selecione uma   ')
    lcd.putstr('opcao a seguir :')
    sleep(1)
    lcd.clear()

    counter = 0

    #Display the first tea available onscreen
    name, temp, infusion_time = tea_options[counter]
    lcd.clear() #limpa o display
    lcd.move_to(0,0) #vai para o começo da primeira linha
    lcd.putstr(name) #escreve o nome do chá
    lcd.move_to(0,1) #vai para o começo da segunda linha
    lcd.putstr(f'{temp} graus/{infusion_time}sec')

    while select_button: 
        x_val = x.read()
        y_val = y.read()

        sleep_ms(150)    

        if y_val > 3500:
            counter += 1
            
            if counter > (len(tea_options) - 1):        
                counter = 0
            
            name, temp, infusion_time = tea_options[counter]
            lcd.clear() #limpa o display
            lcd.move_to(0,0) #vai para o começo da primeira linha
            lcd.putstr(name) #escreve o nome do chá
            lcd.move_to(0,1) #vai para o começo da segunda linha
            lcd.putstr(f'{temp} graus/{infusion_time}sec')
        
        if y_val < 350:
            counter -= 1

            if counter < 0:
                counter = 0
            
            name, temp, infusion_time = tea_options[counter]
            lcd.clear() #limpa o display
            lcd.move_to(0,0) #vai para o começo da primeira linha
            lcd.putstr(name) #escreve o nome do chá
            lcd.move_to(0,1) #vai para o começo da segunda linha
            lcd.putstr(f'{temp} graus/{infusion_time}sec')

        button = joystick_button.value()
        if not button:
            selected_tea = tea_options[counter]

            name, temp, infusion_time = selected_tea
            lcd.clear()
            lcd.putstr('Cha selecionado:')
            lcd.putstr(name)
            sleep(10)
