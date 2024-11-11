from PPlay.window import *
from PPlay.gameimage import *
import menu

bgmenu = GameImage("Images\\peng\\background copy.png")
largura = 1024
altura = 768
janela = Window(largura, altura)

def ranking():
    teclado = Window.get_keyboard()
    while True:
        bgmenu.draw()
        if teclado.key_pressed("esc"):
            menu.menu()
            break
        janela.update()
