from PPlay import gameimage
from PPlay.window import *
from PPlay.mouse import *
from jogo import jogo
from modo import dificuldade

largura = 1024
altura = 768

rato = Mouse()

janela = Window(largura, altura)
janela.set_title("Invaders")

menu_bg = gameimage.GameImage("Images/peng/background.png")


jogar = gameimage.GameImage("Images/peng/botao_jogar.png")
jogar_select = gameimage.GameImage("Images\peng\\botao_jogar_selected.png")
jogar_select.set_position(largura/2 - jogar_select.width/2, 195)
jogar.set_position(largura/2 - jogar.width/2, 200)

modo_botao = gameimage.GameImage("Images\peng\\botao_modo.png")
modo_botao.set_position(largura/2 - modo_botao.width/2, 600)
modo_botao_select = gameimage.GameImage("Images\peng\\botao_modo_select.png")
modo_botao_select.set_position(largura/2 - modo_botao_select.width/2, 595)

def menu():
    menu_bg.draw()

    if Mouse.is_over_area(rato, (largura/2-jogar.width/2, 200),(largura/2+jogar.width/2, jogar.height+200)):
        jogar_select.draw()
        modo_botao.draw()
        if Mouse.is_button_pressed(rato, 1):
            jogo(1)
    elif Mouse.is_over_area(rato, (largura/2-modo_botao.width/2, 600),(largura/2 + modo_botao.width/2, modo_botao.height+600)):
        modo_botao_select.draw()
        jogar.draw()                               
        if Mouse.is_button_pressed(rato, 1):
            dificuldade()
    else:
        jogar.draw()
        modo_botao.draw()
