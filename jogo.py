from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *


# Função para o loop do jogo
def jogar_game():

    velocidade_player = 120

    largura = 900
    altura = 600

    janela = Window(largura, altura)
    janela.set_title("Jogo")
    teclado = Keyboard()

    bg = Sprite("Images//bg.png")
    
    nave = Sprite("Images//nave.png")
    nave.x = largura/2 - nave.width/2
    nave.y = altura - nave.height

    while True:
        
        bg.draw()
        nave.draw()

        if teclado.key_pressed("right") and nave.x + nave.width <= largura:
            nave.x += velocidade_player * janela.delta_time()
        elif teclado.key_pressed("left") and nave.x >= 0:
            nave.x -= velocidade_player * janela.delta_time()

        


        if teclado.key_pressed("ESC"):
            break  # Sai do game loop e volta para o menu

        janela.update()  # Atualiza a janela
