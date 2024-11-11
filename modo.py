from PPlay import gameimage
import menu
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from jogo import jogo

bgmenu = gameimage.GameImage("Images\\peng\\background copy.png")
largura = 1024
altura = 768
janela = Window(largura, altura)

facil = gameimage.GameImage("Images\\peng\\facil_botao.png")
medio = gameimage.GameImage("Images\\peng\\medio_botao.png")
dificil = gameimage.GameImage("Images\\peng\\dificil_botao.png")

facil_select = gameimage.GameImage("Images\\peng\\facil_botao_select.png")
medio_select = gameimage.GameImage("Images\\peng\\medio_botao_select.png")
dificil_select = gameimage.GameImage("Images\\peng\\dificil_botao_select.png")

facil.set_position(largura / 2 - facil.width / 2, 150)
medio.set_position(largura / 2 - medio.width / 2, 400)
dificil.set_position(largura / 2 - dificil.width / 2, 650)

facil_select.set_position(largura / 2 - facil_select.width / 2, 145)
medio_select.set_position(largura / 2 - medio_select.width / 2, 395)
dificil_select.set_position(largura / 2 - dificil_select.width / 2, 645)

teclado = janela.get_keyboard()
rato = Mouse()

def verificar_selecao(mouse, area, botao_select, dificuldade_valor):
    start_point = (area[0], area[1])
    end_point = (area[0] + area[2], area[1] + area[3])
    
    if mouse.is_over_area(start_point, end_point):  
        botao_select.draw()
        if mouse.is_button_pressed(1):  
            return True
    return False

def dificuldade():
    while True:
        bgmenu.draw()
        
        
        facil.draw()
        medio.draw()
        dificil.draw()
        
        if Mouse.is_over_area(rato, (largura / 2 - facil.width / 2, 150), (largura / 2 + facil.width / 2, facil.height + 150)):
            facil_select.draw()
            if Mouse.is_button_pressed(rato, 1):
                dif = 1
                jogo(1)

        if Mouse.is_over_area(rato, (largura / 2 - medio.width / 2, 400), (largura / 2 + medio.width / 2, medio.height + 400)):
            medio_select.draw()
            if Mouse.is_button_pressed(rato, 1):
                dif = 2
                jogo(2)

        if Mouse.is_over_area(rato, (largura / 2 - dificil.width / 2, 650), (largura / 2 + dificil.width / 2, dificil.height + 650)):
            dificil_select.draw()
            if Mouse.is_button_pressed(rato, 1):
                dif = 3
                jogo(3)

        if teclado.key_pressed("esc"):
            menu.menu()
            break
        
        janela.update()
