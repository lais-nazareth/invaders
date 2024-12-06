from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *

def criar_matriz(matriz, lmonstro = 3, cmonstro = 5):
    Yinicial = 100
    for i in range(lmonstro):
        distX = 0
        Xinicial = 150
        linha = []
        for j in range(cmonstro):
            inimigo = Sprite("Images//inimigo.png")
            inimigo.x = Xinicial + distX
            inimigo.y = Yinicial + i*1.5*inimigo.height
            distX += inimigo.width + inimigo.width/2
            linha.append(inimigo)
        matriz.append(linha)
    return matriz

def desenha_matriz(matriz):
    for linha in matriz:
        for sprite in linha:
            sprite.draw()

def game_over(janela):
    bg = GameImage("Images//gameover.png")
    bg.draw()
    janela.draw_text("Game Over", janela.height/2, janela.width/2, size=100, color=(255,255,255))
    

def update_inimigo(matriz, nave, janela, velx, vely):
    inverte = False
    
    for linha in matriz:
        for sprite in linha:
            sprite.move_x(velx * janela.delta_time())
            if (sprite.x < 0.1*sprite.width):
                inverte = True
            elif (sprite.x >= janela.width - sprite.width - (0.1*sprite.width)):
                inverte = True
        if inverte:
            velx = -velx
        
        return velx