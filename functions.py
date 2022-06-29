from importlib.metadata import files
from time import sleep
from pynput import keyboard
import re
import pyautogui as pag

controller = keyboard.Controller()

numero = -1
velocidade = 0.003


def typePhrase(text):
    # split phrase by letter
    phraseList = text.split('%')

    # for each letter in phrase
    for phrase in phraseList:
        if(phrase == 'e'):
            controller.press(keyboard.Key.end)
            sleep(0.8)
        elif(phrase == 'eb'):
            controller.press(keyboard.Key.end)
            sleep(0.6)
            controller.press(keyboard.Key.enter)
            return
        elif(phrase == 'enter'):
            sleep(0.3)
            controller.press(keyboard.Key.enter)
            return
        elif(phrase == 'enter2'):
            sleep(0.3)
            controller.press(keyboard.Key.enter)
            sleep(0.3)
            controller.press(keyboard.Key.enter)
            return
        elif(phrase == 'enter3'):
            sleep(0.3)
            controller.press(keyboard.Key.enter)
            sleep(0.3)
            controller.press(keyboard.Key.enter)
            sleep(0.3)
            controller.press(keyboard.Key.enter)
            return
        elif (phrase == 'b'):
            return
        else:
            for letter in phrase:
                if(letter == '0' or letter == '1' or letter == '2'):
                    pag.write(str(letter))
                else:
                    pag.write(letter)
                sleep(velocidade)


def capturar_teclas(tecla):
    global numero
    global velocidade

    # if tecla  == shift_r
    if tecla == keyboard.Key.shift_r:
        tecla = str(tecla)

        # remover as aspas simples
        tecla = re.sub(r'\'', '', tecla)

        # adicionar 1 ao numero
        numero += 1
        execRead(numero)

    if tecla == keyboard.Key.alt_gr:
        velocidade += 0.03
    elif tecla == keyboard.Key.ctrl_r:
        velocidade -= 0.03


def execRead(numero):
    path = 'C:/Users/wroge/Desktop/ListenerPy/texto.txt'

    # open file to read
    indices = sum(1 for line in open(path, 'r')) - 1

    if(numero <= indices):
        # read line by index
        fileText = open(path, 'r')
        line = fileText.readlines()[numero]

        # trim spaces of line
        line = line.strip()

        # write text
        isHashTag = line.startswith('#')
        if(isHashTag == False):
            typePhrase(line)

        # close file
        fileText.close()
    else:
        print("Fim do script")
        keyboard.Listener.stop()
        return False
