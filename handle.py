from importlib.metadata import files
from time import sleep
from pynput import keyboard
import re

numero = -1
velocidade = 0.3
controller = keyboard.Controller()


def typePhrase(phrase):
    # split phrase by letter
    phrase = list(phrase)

    # for each letter in phrase
    for letter in phrase:
        controller.press(letter)
        sleep(velocidade)

    # press end
    # if prhase has one letter
    if len(phrase) > 1:
        controller.press(keyboard.Key.end)
        # controller.press(keyboard.Key.enter)


def capturar_teclas(tecla):
    global numero
    global velocidade

    # if tecla  == f9
    if tecla == keyboard.Key.f9:
        tecla = str(tecla)

        # remover as aspas simples
        tecla = re.sub(r'\'', '', tecla)

        # adicionar 1 ao numero
        numero += 1
        execRead(numero)

    # if tecla == esc
    elif tecla == keyboard.Key.esc:
        return False
    elif tecla == keyboard.Key.ctrl_l:
        velocidade += 0.01
    elif tecla == keyboard.Key.ctrl_r:
        velocidade -= 0.01


def execRead(numero):
    # open file to read
    indices = sum(1 for line in open('script/text.txt', 'r')) - 1

    if(numero <= indices):
        # read line by index
        fileText = open('script/text.txt', 'r')
        line = fileText.readlines()[numero]

        # trim spaces of line
        line = line.strip()

        # write text
        typePhrase(line)

        # close file
        fileText.close()
    else:
        print("Fim do script")
        keyboard.Listener.stop()
        return False


with keyboard.Listener(on_press=capturar_teclas) as l:
    l.join()
