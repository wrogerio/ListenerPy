from functions import capturar_teclas, keyboard

with keyboard.Listener(on_release=capturar_teclas) as l:
    l.join()
