from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from constants import *
from PPlay.gameobject import *


def posInicialTiro(player,tiros):
    tiro = Sprite("images/tiro.png")
    tiro.x = player.x + player.width/2 - tiro.width/2  
    tiro.y = player.y - tiro.height             
    tiros.append(tiro)
    return tiros

# Função para o loop do jogo
def jogar_game():

    largura = 900
    altura = 600

    janela = Window(largura, altura)
    janela.set_title("Jogo")
    teclado = Keyboard()

    bg = Sprite("Images//bg.png")
    
    nave = Sprite("Images//nave.png")
    nave.x = largura/2 - nave.width/2
    nave.y = altura - nave.height

    tiro = Sprite("Images//tiro.png")
    tiros = []
    

    while True:
        
        bg.draw()
        nave.draw()

        if teclado.key_pressed("right") and nave.x + nave.width <= largura:
            nave.x += velocidade_player * janela.delta_time()
        elif teclado.key_pressed("left") and nave.x >= 0:
            nave.x -= velocidade_player * janela.delta_time()

    
        if teclado.key_pressed("ESC"):
            break  # Sai do game loop e volta para o menu


        if teclado.key_pressed("space") and len(tiros) == 0:
            tiros = posInicialTiro(nave, tiros)
        elif teclado.key_pressed("space") and tiros[len(tiros)-1].y < velocidade_tiro:
            tiros = posInicialTiro(nave, tiros)
            
        if len(tiros) > 0:
            for i in tiros:
                i.draw()
                if i.y > 0 - i.height:
                    i.y -= velocidade_tiro * janela.delta_time()
                else:
                    tiros.remove(i)

        janela.update()  # Atualiza a janela