import pygame
from pygame.locals import *
import sys
from sys import exit
from random import randint

pygame.init()
#Música de fundo
musica_de_fundo = pygame.mixer.music.load('./music_project/BoxCat Games - Map Theme.mp3')
pygame.mixer.music.play(-1)

#Som de ataque do heroi
ataque_heroi = pygame.mixer.Sound('./music_project/smw_bubble_pop.wav')

# Configurações da tela
WIDTH = 1024 #Largura
HEIGHT = 552 #Altura
SCREEN_SIZE = (WIDTH, HEIGHT)

# Configurações do botão
BUTTONWIDTH = 200
BUTTONHEIGHT = 100
BUTTONCOLOR = (194, 245, 66)  # Verde
BUTTONTEXT = "Start"
BUTTONTEXTCOLOR = (255, 255, 255)  # Branco
BUTTONPOSITION = (WIDTH // 2 - BUTTONWIDTH // 2, HEIGHT // 2 - BUTTONHEIGHT // 2)

# Inicialização da tela
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Start")

# Carregar a imagem de fundo
background_image = pygame.image.load("./img_project/cenario.png")
background_rect = background_image.get_rect()

# Carregando a fonte
fonteborda = pygame.font.Font(None, 82)
fontetitle = pygame.font.Font(None, 80)
fontbutton = pygame.font.Font(None, 50)
fonteinfo = pygame.font.Font(None, 30)

# Variável de controle do botão
button_pressed = False

# Configuração do clock
clock = pygame.time.Clock()

# Loop principal
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(*BUTTONPOSITION, BUTTONWIDTH, BUTTONHEIGHT).collidepoint(mouse_pos):
                # Iniciar o jogo aqui
                print("Iniciando o jogo...")
                button_pressed = True

    # Desenhar a imagem de fundo
    screen.blit(background_image, background_rect)

    # Desenhar o nome do jogo no centro da tela
    gamename = fontetitle.render("Guardians of Nature", True, [156, 51, 30])  
    borda = fonteborda.render("Guardians of Nature", True, [194, 245, 66])  
    gamenamerect = gamename.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 100))
    bordarect = borda.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(gamename, gamenamerect)
    screen.blit (borda, bordarect)

    # Desenhar o botão
    button_rect = pygame.Rect(*BUTTONPOSITION, BUTTONWIDTH, BUTTONHEIGHT)
    pygame.draw.rect(screen, BUTTONCOLOR, button_rect)
    text = fontbutton.render(BUTTONTEXT, True, BUTTONTEXTCOLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    # Desenhar instruções
    infotext = fonteinfo.render ("Como jogar:     andar para direita - S        andar para esquerda - A        atacar - Espaço", True, (255, 255, 255))
    infotextrect = infotext.get_rect(center= (WIDTH // 2, HEIGHT // 2 + 200))
    screen.blit(infotext, infotextrect)

    pygame.display.flip()

    # Verificar se o botão foi pressionado e sair do loop
    if button_pressed:
        break

    # Limitar a taxa de atualização
    clock.tick(60)

#tela do jogo
largura = 1024
altura = 552
tela = pygame.display.set_mode((largura, altura)) #alterando a altura e largura da tela
cenario = pygame.image.load('./img_project/cenario.png') #inserindo o cenario
pygame.display.set_caption('Guardians of nature') #nome do jogo no topo da pagina
frame = pygame.time.Clock() #função para aplicar os frames por segundo

#textos na tela
fonte = pygame.font.SysFont('arial', 30, True, False)

#tamanho do heroi
tamanho_heroi = (180, 180)

#MONSTRO
#inserindo o monstro
imagen = pygame.image.load('./img_project/monstrojognormal.png')
define = 10
x2 = 800 #posição inicial
y2 = 420 #posição inicial
tamanho_vilao = (160, 160)
imagen = pygame.transform.scale(imagen,(tamanho_vilao))

#vida do vilao
ponto = 240
vida_v = 25
print(f'vilao com {vida_v} de vida')

#HEROI
#inserindo o heroi no codigo
heroi = pygame.image.load('./img_project/aldeao.png')
heroi = pygame.transform.scale(heroi, tamanho_heroi)
heroi_invertido = pygame.image.load('./img_project/aldeao h.png')
heroi_invertido = pygame.transform.scale(heroi_invertido, tamanho_heroi)

#posição inicial do heroi
x1 = 300
y1 = 370

#inserindo o heroi atacando no codigo
heroi_atacando = pygame.image.load('./img_project/aldeao atacando.png')
heroi_atacando = pygame.transform.scale(heroi_atacando, (188,188))
heroi_atacando_i = pygame.image.load('./img_project/aldeao atacando h.png')
heroi_atacando_i = pygame.transform.scale(heroi_atacando_i, (188,188))

vida_h = 5

#ponto do heroi
img_pontoheroi = pygame.image.load('./img_project/monstrojognormal.png')
pontoheroix = x1
pontoheroiy = y1
tamanho_ponto = (1, 1)
imagem_ponto = pygame.transform.scale(img_pontoheroi,(tamanho_ponto))

venceu = False

def reiniciar_jogo():
    global vida_v, x1, y1, x2, y2, venceu
    vida_v = 25
    x1 = 300
    y1 = 370
    x2 = 800
    y2 = 420
    venceu = False

#inicio do jogo
while True:
    while vida_v>=0:
        while vida_h!=0:
            #tela e frames
            frame.tick(22)
            tela.blit(cenario, (0,0))

            #texto de vida
            if vida_v>=1:
                    contador = f'Monstro'
            else:
                    contador = 'Monstro derrotado'
            barra_formatacao = fonte.render(contador, True, (255,0,0))

            #criação dos personagens na tela
            if x1<x2:
                tela.blit(heroi, (x1, y1))
            else:
                tela.blit(heroi_invertido, (x1,y1))

            #monstro
            tela.blit(imagen, (x2, y2))

            #eventos do jogo
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                #ataque do heroi
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:#tecla espaço para atacar
                        if x1<x2:#imagem do heroi atacando
                            tela.blit(heroi_atacando, (x1, y1))
                        else:
                            tela.blit(heroi_atacando_i, (x1, y1))

                        if x1+10 < x2+60 and x1 > x2-130:  #tira dano caso atacar na area do monstro
                            ##x1+= -20 #um pulo pra tras quando houver dano
                            ##x2+= +20
                            vida_v+= -1
                            ponto+= -10
                            ataque_heroi.play() #Efeito sonoro de ataque do heroi
                            if vida_v>=1:
                                print(f'vilao com {vida_v} de vida')  
                            elif vida_v == 0:
                                print('vilao sem vida')
                                
                                fonte2 = pygame.font.SysFont('arial', 20, True, True)
                                mensagem = 'You Win! Pressione a tecla R para jogar novamente'
                                texto_formatado = fonte2.render(mensagem, True,(255,0,0))
                                ret_texto = texto_formatado.get_rect()
                                venceu = True
                                while venceu:
                                    tela.fill((0,255,0))
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            pygame.quit()
                                            exit()
                                        if event.type == KEYDOWN:
                                            if event.key == K_r:
                                                reiniciar_jogo()
                                    ret_texto.center = (largura//2, altura//2)
                                    tela.blit(texto_formatado, ret_texto)
                                    pygame.display.update()


            #movimentação do vilao
            x2 += define
            if x2 > 920 : # quando o obejto monstro chega no final da tela, vai inverter o valor da variavel para o negativo,
                # mudando o sentido do movimento.
                define = -define
                print(define)
            if x2 < 0: # quando o objeto  monstro chega no ponto 0 no eixo x, vai novamente inverter o valor da varivel,
                # fazendo com que o valor da variavel volte para o positivo.
                define = -define
                print(define)

            #movimentação do heroi
            if pygame.key.get_pressed()[K_a]:
                x1+= -5
            if pygame.key.get_pressed()[K_s]:
                x1+= 5

            listaheroi = [x1, y1] # armazenando a posicao do heroi em uma lista
            lstavilao = [x2, y2] # armazenando a posicao do monstro em uma lista

            # condicao quando o monstro entra em modo de ataque
            if listaheroi < lstavilao :
                imagen = pygame.image.load('./img_project/monstrojogatacando.png')
                imagen = pygame.transform.scale(imagen,(tamanho_vilao))
                tela.blit(imagen, (x2, y2))

                # condicao quando o monstro estiver no mesmo posicionamento do heroi no eixo x, ele explodi
                if x1==x2 :
                
                    imagen = pygame.image.load('./img_project/explosão1.png')
                    imagen = pygame.transform.scale(imagen, (tamanho_vilao))
                    tela.blit(imagen, (x1, y1))
                    vida_h+= -1
                    print(f'vida heroi: {vida_h}')
                    print('explosão!!')
        
            #condicao quando o monsto estiver na esquerda do heroi ele volta para o modo normal
            if listaheroi > lstavilao :
                imagen = pygame.image.load('./img_project/monstrojognormal.png')
                imagen = pygame.transform.scale(imagen,(tamanho_vilao))
                tela.blit(imagen, (x2, y2))

            
            #print(x2)
            #print(x1)

            #barra de vida na tela
            tela.blit(barra_formatacao, (470, 40))
            barra1 = pygame.draw.rect(tela, (255,0,0), (400, 80, 10+ponto, 20))
            
            #ponto do heroi na tela
            tela.blit(imagem_ponto,(x1+50, y1+130))

            pygame.display.flip()
        print('heroi morreu') #mensagem quando heroi morrer
    print('monstro morreu') #mensagem quando o vilao morrer
    break;