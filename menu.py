from PPlay.sprite import *
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from jogo import jogar_game

def mostrar_menu():
    janela = Window(840,620)
    janela.set_title("Menu Principal")

    # Carregar a imagem de fundo do menu
    fundo_menu = Sprite("Images//fundomenu.jpg")

    # Criar os botões
    jogar = Sprite("Images//jogar.png")
    jogar.x = 300
    jogar.y = 100

    niveis = Sprite("Images//niveis.png")
    niveis.x = 300
    niveis.y = 200

    ranking = Sprite("Images//ranking.png")
    ranking.x = 300
    ranking.y = 300

    sair = Sprite("Images//sair.png")
    sair.x = 300
    sair.y = 400

    # Mouse e teclado
    mouse = Mouse()
    teclado = Keyboard()
    while True:
        fundo_menu.draw()  # Desenha o fundo do menu

        # Desenha os botões
        jogar.draw()
        niveis.draw()
        ranking.draw()
        sair.draw()

        # Pega a posição do mouse
        mouse_x, mouse_y = mouse.get_position()

        # Verifica se o mouse clicou em algum botão
        if mouse.is_button_pressed(1):  # Clique do botão esquerdo do mouse
            if dentro_do_botao(jogar, mouse_x, mouse_y):
                jogar_game()  # Função que entra no game loop
            elif dentro_do_botao(niveis, mouse_x, mouse_y):
                escolher_dificuldade()  # Função para escolher dificuldade

            elif dentro_do_botao(sair, mouse_x, mouse_y):
                janela.close()  # Fecha a janela e sai do jogo

        # Verifica se a tecla ESC foi pressionada para sair do menu
        if teclado.key_pressed("ESC"):
            janela.close()

        janela.update()  # Atualiza a janela

# Função que verifica se o mouse está dentro do botão
def dentro_do_botao(botao, mouse_x, mouse_y):
    # Verifica se as coordenadas do mouse estão dentro do retângulo do botão
    if botao.x <= mouse_x <= botao.x + botao.width and botao.y <= mouse_y <= botao.y + botao.height:
        return True
    return False


# Função para escolher a dificuldade
def escolher_dificuldade():


    janela = Window(840,620)
    janela.set_title("Escolher Dificuldade")

    # Carregar a imagem de fundo da tela de dificuldade
    fundo_menu = Sprite("Images//game.png")

    # Criar os botões de dificuldade
    facil = Sprite("Images//facil.png")
    medio = Sprite("Images//medio.png")
    dificil = Sprite("Images//dificil.png")
    
    facil.x = 300
    facil.y = 100


    medio.x = 300
    medio.y = 200


    dificil.x = 300
    dificil.y = 300

    # Mouse e teclado
    mouse = Mouse()
    teclado = Keyboard()
    while True:
            fundo_menu.draw()  # Desenha o fundo da tela de dificuldade

            # Desenha os botões de dificuldade (sprites)
            facil.draw()
            medio.draw()
            dificil.draw()

            # Pega a posição do mouse
            mouse_x, mouse_y = mouse.get_position()



            # Verifica se a tecla ESC foi pressionada para voltar ao menu
            if teclado.key_pressed("ESC"):
                break  # Retorna para o menu principal

            janela.update()  # Atualiza a janela