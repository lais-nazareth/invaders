from PPlay import gameimage
import menu
from PPlay.window import *

largura = 1024
altura = 768

janela = Window(largura, altura)
janela.set_title("Jogo")

jogo_bg = gameimage.GameImage("Images/peng/background_jogo.png")
def jogo(dif):
    teclado = Window.get_keyboard()
    while True:
        jogo_bg.draw()
        if teclado.key_pressed("esc"):
            menu.menu()
            break
        janela.update()