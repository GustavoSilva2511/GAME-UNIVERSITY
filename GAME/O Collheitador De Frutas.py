import pygame
from pygame.locals import *
from sys import exit
from random import randrange
from random import randint
import os


def abrir_jogo():
    pygame.init()

    # variaveis
    largura = 1080
    altura = 720
    velocidade = 2
    indice_drop_bom = 3
    indice_drop_ruim = 1

    # textos
    fonte_pontos = pygame.font.SysFont('arial', 30, True, False)
    fonte_menu = pygame.font.SysFont('arial', 50, True, False)
    fonte_cutcene = pygame.font.SysFont('arial', 35, False, False)

    # cores
    preta = (0, 0, 0)
    branco = (255, 255, 255)

    # tela
    tela = pygame.display.set_mode((largura, altura))
    frames = pygame.time.Clock()

    # diretorios
    diretorio_principal = os.path.dirname(__file__)
    diretorio_imagens = os.path.join(diretorio_principal, 'sprites')
    diretorio_sons = os.path.join(diretorio_principal, 'sons')

    diretorio_sprite = os.path.join(diretorio_imagens, 'jogador_sprites_direita.png')
    diretorio_itens_sprite = os.path.join(diretorio_imagens, 'itens_sprites.png')
    diretorio_icon_vida = os.path.join(diretorio_imagens, 'coracao_sprites.png')
    diretorio_cenario_fundo = os.path.join(diretorio_imagens, 'cenario_3.png')
    diretorio_cenario_1 = os.path.join(diretorio_imagens, 'cenario_1.png')
    diretorio_tela_gameover = os.path.join(diretorio_imagens, 'tela_gameover.jpg')
    diretorio_menu_tela = os.path.join(diretorio_imagens, 'menu_tela.png')
    diretorio_menu_tela_1 = os.path.join(diretorio_imagens, 'menu_tela_1.png')
    diretorio_sprite_bichoranha = os.path.join(diretorio_imagens, 'bichoranha_sprite.png')
    diretorio_game_icon = os.path.join(diretorio_imagens, 'Game_Icon.png')
    diretorio_chao = os.path.join(diretorio_imagens, 'cenario.jpg')

    diretorio_music_1 = os.path.join(diretorio_sons, 'music.wav')
    diretorio_song_coleta = os.path.join(diretorio_sons, 'coleta.wav')
    diretorio_song_dano = os.path.join(diretorio_sons, 'dano.wav')
    diretorio_song_coleta_vida = os.path.join(diretorio_sons, 'coleta_vida.wav')

    sprite_jogador = pygame.image.load(diretorio_sprite).convert_alpha()
    sprite_itens = pygame.image.load(diretorio_itens_sprite).convert_alpha()
    sprite_icon_vida = pygame.image.load(diretorio_icon_vida).convert_alpha()
    sprite_bichoranha = pygame.image.load(diretorio_sprite_bichoranha).convert_alpha()
    game_icon = pygame.image.load(diretorio_game_icon).convert()
    sprite_cenario_1 = pygame.image.load(diretorio_cenario_1).convert_alpha()

    # nome do game / icon
    pygame.display.set_caption("O Colheitador de Fruta")
    pygame.display.set_icon(game_icon)

    # funções
    def Remove_drops():

        for i in itens_bons:
            itens_bons.remove(i)

        for i in itens_ruins:
            itens_ruins.remove(i)

    def Respaw_drops():

        for i in range(indice_drop_bom):
            item = DropItens('bom')
            itens_bons.add(item)

        for i in range(indice_drop_ruim):
            item = DropItens('ruim')
            itens_ruins.add(item)

    def cutcene():
        while True:
            while True:
                tela.fill(branco)
                frames.tick(30)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            jogador.vida = 100
                            jogador.vida_mabur = 1000
                            pygame.mixer.music.set_volume(0.25)
                            Respaw_drops()
                            iniciar()
                            break

                tela.blit(chao, (0, 0))
                cenarios.draw(tela)
                cenarios.update()

                texto_cut = 'Mabur é uma velha arvore que anda magoada por deixarem seu frutos estragarem!'
                texto_formatado_menu = fonte_cutcene.render(texto_cut, True, preta)
                tela.blit(texto_formatado_menu, (cenario_1.rect[0]+600, 250))

                texto_cut_2 = 'ela apenas não entende que as pessoas migraram para a cidade e a abandonaram alí'
                texto_formatado_menu = fonte_cutcene.render(texto_cut_2, True, preta)
                tela.blit(texto_formatado_menu, (cenario_1.rect[0] + 700, 300))

                texto_cut_3 = 'Doi no coração ver mabur triste e solitaria, por isso você está aqui!'
                texto_creditos_formatado = fonte_cutcene.render(texto_cut_3, True, preta)
                tela.blit(texto_creditos_formatado, (cenario_1.rect[0] + 2800, 250))

                texto_cut_4 = 'Você não quer que mabur se suicide né? então não deixe que seus frutos caiam!'
                texto_creditos_formatado = fonte_cutcene.render(texto_cut_4, True, preta)
                tela.blit(texto_creditos_formatado, (cenario_1.rect[0] + 2800, 300))

                if not cenario_1.rect[0] <= -2780:
                    cenario_1.rect[0] -= 3

                pygame.display.flip()

    def menu_gameover(x_texto=largura, texto_var=randint(1, 5)):
        while True:

            tela.fill(branco)
            frames.tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        jogador.pontuacao = 0
                        Remove_drops()
                        menu()
                        break

            tela.blit(gameover, (0, 0))

            texto_menu = f'PONTUAÇÃO: {jogador.pontuacao}'
            texto_formatado_menu = fonte_menu.render(texto_menu, True, branco)
            tela.blit(texto_formatado_menu, (300, 600))

            texto_2_menu = f'Mabur não resistiu, volte no tempo e tente de novo, é so um jogo!'
            texto_formatado_menu = fonte_pontos.render(texto_2_menu, True, branco)
            tela.blit(texto_formatado_menu, (50, 680))

            if texto_var == 1:
                texto_motivador = f'Não deixe mabur tomar muito dano, nunca se sabe o quanto ela ainda aguenta'
                texto_motivador_formatado = fonte_pontos.render(texto_motivador, True, branco)
                tela.blit(texto_motivador_formatado, (x_texto, 10))

            if texto_var == 2:
                texto_motivador = f'Fique sempre atento às frutas que estão caindo, não esqueça de usar o dash pressionando a tecla "espaço"'
                texto_motivador_formatado = fonte_pontos.render(texto_motivador, True, branco)
                tela.blit(texto_motivador_formatado, (x_texto, 10))

            if texto_var == 3:
                texto_motivador = f'Voçê conhece o gui? que gui? o guiado por Deus pra te fazer feliz rs'
                texto_motivador_formatado = fonte_pontos.render(texto_motivador, True, branco)
                tela.blit(texto_motivador_formatado, (x_texto, 10))

            if texto_var == 4:
                texto_motivador = f'Como assim "colheiteiro", o certo não seria coleteiro? pois é, mas sejamos justo, colheiteiro é mais dahora'
                texto_motivador_formatado = fonte_pontos.render(texto_motivador, True, branco)
                tela.blit(texto_motivador_formatado, (x_texto, 10))

            if texto_var == 5:
                texto_motivador = f'Ja se perguntou o que fazer quando cai duas frutas ao mesmo tempo em areas diferente? Quando descobrir me ensina'
                texto_motivador_formatado = fonte_pontos.render(texto_motivador, True, branco)
                tela.blit(texto_motivador_formatado, (x_texto, 10))

            x_texto -= 5
            if x_texto < -1500:
                x_texto = 1100
                texto_var = randint(1, 5)

            pygame.display.flip()

    def menu(x_texto=largura):
        while True:
            tela.fill(branco)
            frames.tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        cutcene()
                        break

            tela.blit(cenario, (0, 0))
            tela.blit(menu_tela_1, (0, 0))
            tela.blit(menu_tela, (0, 0))

            texto_menu = '0.334 version alpha'
            texto_formatado_menu = fonte_menu.render(texto_menu, True, preta)
            tela.blit(texto_formatado_menu, (1, 1))

            texto_creditos = 'creditos.. deselvonvedor: Carlos Gustavo ... animaçoes e sprites: carlos gustavo, exeto a cenario principal ... musica: Dirge of Cerberus Final Fantasy VII - Calm Before the Storm'
            texto_creditos_formatado = fonte_pontos.render(texto_creditos, True, preta)
            tela.blit(texto_creditos_formatado, (x_texto, 690))

            x_texto -= 5

            if x_texto < - 2550:
                x_texto = largura

            pygame.display.flip()

    def iniciar():
        while True:
            tela.fill(branco)
            frames.tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        pausar = True

                        while pausar:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_p:
                                        pausar = False

                        pygame.display.flip()

            if pygame.key.get_pressed()[K_d]:
                jogador.AndarDireita()
                cenario_1.Andar_esquerda()

            if pygame.key.get_pressed()[K_a]:
                jogador.AndarEsquerda()
                cenario_1.Andar_direita()

            if pygame.key.get_pressed()[K_SPACE]:
                jogador.Dash()

            coleta_item_bom = pygame.sprite.spritecollide(jogador, itens_bons, True)
            coleta_item_ruim = pygame.sprite.spritecollide(jogador, itens_ruins, True)
            coleta_vida = pygame.sprite.spritecollide(jogador, vida_grupo, True)

            if randint(0, 750) == 1:
                vidinha = Drop_vida()
                vida_grupo.add(vidinha)

            if coleta_vida:
                coleta_vida_som.play()
                jogador.vida += 25

            if coleta_item_bom:
                coleta_som.play()
                item = DropItens('bom')
                itens_bons.add(item)
                jogador.pontuacao += 10

            if coleta_item_ruim:
                dano_som.play()
                item = DropItens('ruim')
                itens_ruins.add(item)
                jogador.vida -= 25

            if jogador.vida <= 0:
                pygame.mixer.music.set_volume(1)
                menu_gameover()
                break

            if jogador.vida_mabur <= 0:
                pygame.mixer.music.set_volume(1)
                menu_gameover()
                break

            tela.blit(chao, (0, 0))

            cenarios.draw(tela)
            cenarios.update()

            todas_sprites_jogador.draw(tela)
            todas_sprites_jogador.update()

            itens_bons.draw(tela)
            itens_bons.update()

            itens_ruins.draw(tela)
            itens_ruins.update()

            icons.draw(tela)
            icons.update()

            vida_grupo.draw(tela)
            vida_grupo.update()

            # texto na tela
            texto_pontos = f'PONTUAÇÂO: {jogador.pontuacao}'
            texto_formatado = fonte_pontos.render(texto_pontos, True, preta)
            tela.blit(texto_formatado, (largura - 300, 10))

            texto_vida_mabur = f'vida de Mabur: {jogador.vida_mabur}'
            texto_mabur_formatado = fonte_pontos.render(texto_vida_mabur, True, preta)
            tela.blit(texto_mabur_formatado, (10, 100))

            pygame.display.flip()

    # classes
    class Icon(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.icon_vida = []

            self.x_icon, self.y_icon = 0, 0

            for i in range(4):
                img = sprite_icon_vida.subsurface((i*32, 0), (32, 32))
                img = pygame.transform.scale(img, ((2 * 32), (2 * 32)))
                self.icon_vida.append(img)

            self.cont = 0
            self.image = self.icon_vida[int(self.cont)]

            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

            self.rect.topleft = self.x_icon, self.y_icon

        def update(self):
            if jogador.vida > 100:
                jogador.vida = 100

            if jogador.vida == 100:
                self.cont = 0
                self.image = self.icon_vida[int(self.cont)]
            elif jogador.vida == 75:
                self.cont = 1
                self.image = self.icon_vida[int(self.cont)]
            elif jogador.vida == 50:
                self.cont = 2
                self.image = self.icon_vida[int(self.cont)]
            elif jogador.vida == 25:
                self.cont = 3
                self.image = self.icon_vida[int(self.cont)]

    class DropItens(pygame.sprite.Sprite):
        def __init__(self, bom_ou_ruim):
            pygame.sprite.Sprite.__init__(self)
            self.sprite_itens = []
            self.x_itens, self.y_itens = randrange(0, 1020), -(randrange(0, 800, 50))
            self.bom_ou_ruim = bom_ou_ruim
            self.velocidade = 15

            if self.bom_ou_ruim == 'bom':
                for i in range(4):
                    img = sprite_itens.subsurface((i*32, 0), (32, 32))
                    img = pygame.transform.scale(img, ((2 * 32), (2 * 32)))
                    self.sprite_itens.append(img)

            if self.bom_ou_ruim == 'ruim':
                for i in range(4):
                    img = sprite_itens.subsurface((i*32, 1 * 32), (32, 32))
                    img = pygame.transform.scale(img, ((2 * 32), (2 * 32)))
                    self.sprite_itens.append(img)

            self.cont = randint(0, 3)
            self.image = self.sprite_itens[int(self.cont)]

            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

            self.rect.topleft = self.x_itens, self.y_itens

            self.reaparecer_tudo = False

            self.andar_direita = False
            self.andar_esquerda = False

        def Andar_direita(self):
            self.andar_direita = True
            self.andar_esquerda = False

        def Andar_esquerda(self):
            self.andar_esquerda = True
            self.andar_direita = False

        def reaparecer(self):
            self.reaparecer_tudo = True

        def update(self):
            self.rect[1] += velocidade
            self.rect[1] += velocidade + 5

            if self.rect[1] > 720:
                self.rect[0], self.rect[1] = randrange(0, 1020, 50), -100
                self.cont = randrange(0, 3)
                self.image = self.sprite_itens[int(self.cont)]
                if self.bom_ou_ruim == 'bom':
                    jogador.vida_mabur -= 25

            if self.reaparecer_tudo:
                if iniciar():
                    self.rect[0], self.rect[1] = randrange(0, 1020, 50), -100
                    self.cont = randrange(0, 3)
                    self.image = self.sprite_itens[int(self.cont)]
                self.reaparecer_tudo = False

            if pygame.key.get_pressed()[K_SPACE]:
                self.velocidade = 25
            else:
                self.velocidade = 15

            if cenario_1.andar_direita:
                if pygame.key.get_pressed()[K_a] and jogador.rect[0] <= 640:
                    self.rect[0] += self.velocidade

            if cenario_1.andar_esquerda:
                if pygame.key.get_pressed()[K_d] and jogador.rect[0] >= 440:
                    self.rect[0] -= self.velocidade

            # A lenda rotacionadora:  self.image = pygame.transform.rotate(self.image, self.rect[1])

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprite_parado = []
            self.sprite_andando = []
            self.sprite_pulando = []
            self.velocidade = 0
            self.x_jogador, self.y_jogador = 1080//2, altura-170

            for i in range(3):
                img = sprite_jogador.subsurface((i*16, 0), (16, 16))
                img = pygame.transform.scale(img, ((5*16), (5*16)))
                self.sprite_parado.append(img)

            for i in range(3, 5):
                img = sprite_jogador.subsurface((i*16, 0), (16, 16))
                img = pygame.transform.scale(img, ((5 * 16), (5 * 16)))
                self.sprite_andando.append(img)

            img = sprite_jogador.subsurface((5*16, 0), (16, 16))
            img = pygame.transform.scale(img, ((5 * 16), (5 * 16)))
            self.sprite_pulando.append(img)


            self.cont = 0
            self.image = self.sprite_parado[int(self.cont)]

            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = self.x_jogador, self.y_jogador

            self.dash = False
            self.animar = True
            self.andar_direita = False
            self.andar_esquerda = False
            self.gravidade = False

            self.vida_mabur = 1000
            self.vida = 100
            self.pontuacao = 0

        def AndarDireita(self):
            self.andar_direita = True
            self.animar = False
            self.andar_esquerda = False
            self.dash = False

        def AndarEsquerda(self):
            self.andar_esquerda = True
            self.animar = False
            self.andar_direita = False
            self.dash = False

        def Dash(self):
            self.dash = True
            self.animar = False


        def update(self):
            if self.rect[0] <= 0:
                self.andar_esquerda = False

            if self.rect[0] >= 1040:
                self.andar_direita = False

            if self.animar:

                self.cont += 0.25

                if self.cont > len(self.sprite_parado):
                    self.cont = 0

                self.image = self.sprite_parado[int(self.cont % len(self.sprite_parado))]

            if self.andar_direita:
                if pygame.key.get_pressed()[K_d]:

                    self.rect[0] += self.velocidade

                    if self.cont > len(self.sprite_andando):
                        self.cont = 0

                    self.cont += 0.25
                    self.image = self.sprite_andando[int(self.cont % len(self.sprite_andando))]

            if self.andar_esquerda:
                if pygame.key.get_pressed()[K_a]:

                    self.rect[0] -= self.velocidade

                    if self.cont > len(self.sprite_andando):
                        self.cont = 0

                    self.cont += 0.25
                    self.image = self.sprite_andando[int(self.cont % len(self.sprite_andando))]
                    self.image = pygame.transform.flip(self.image, True, False)

            if self.dash and not 640 >= jogador.rect[0] >= 440:
                if self.andar_esquerda:
                    self.rect[0] -= 30
                elif self.andar_direita:
                    self.rect[0] += 30

            if cenario_1.rect.topleft[0] >= 0:
                self.velocidade = 15

            elif cenario_1.rect.topright[0] <= 1080:
                self.velocidade = 15

            else:
                self.velocidade = 0

    class Bot(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprite_bichoranha = []
            self.x_bichoranha, self.y_bichoranha = (jogador.rect[0] - 20), (jogador.rect[1] + 15)
            self.velocidade = 15

            for i in range(2):
                for j in range(6):
                    img = sprite_bichoranha.subsurface(((j * 32), (i * 32)), (32, 32))
                    img = pygame.transform.scale(img, ((2 * 32), (2 * 32)))
                    self.sprite_bichoranha.append(img)

            self.cont = 0
            self.image = self.sprite_bichoranha[int(self.cont)]

            self.rect = self.image.get_rect()

            self.rect.topleft = self.x_bichoranha, self.y_bichoranha

            self.andar_direita = False
            self.andar_esquerda = False

        def update(self):

            if self.rect[0] < (jogador.rect[0] - 100):
                self.andar_direita = True
                self.andar_esquerda = False

            elif self.rect[0] > (jogador.rect[0] + 100):
                self.andar_direita = False
                self.andar_esquerda = True
            else:
                self.andar_direita = False
                self.andar_esquerda = False

            if self.andar_direita:

                self.rect[0] += 20

                if self.cont > len(self.sprite_bichoranha):
                    self.cont = 0

                self.cont += 0.5
                self.image = self.sprite_bichoranha[int(self.cont % len(self.sprite_bichoranha))]
                self.image = pygame.transform.flip(self.image, True, False)

            if self.andar_esquerda:

                self.rect[0] -= 20

                if self.cont > len(self.sprite_bichoranha):
                    self.cont = 0

                self.cont += 0.5
                self.image = self.sprite_bichoranha[int(self.cont % len(self.sprite_bichoranha))]

            if pygame.key.get_pressed()[K_SPACE]:
                self.velocidade = 25
            else:
                self.velocidade = 15

            if cenario_1.andar_direita:
                if pygame.key.get_pressed()[K_a] and jogador.rect[0] <= 640:
                    self.rect[0] += self.velocidade

            if cenario_1.andar_esquerda:
                if pygame.key.get_pressed()[K_d] and jogador.rect[0] >= 440:
                    self.rect[0] -= self.velocidade

    class Drop_vida(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.icon_vida = []
            self.velocidade = 15
            self.x_icon, self.y_icon = randrange(0, 1020), -(randrange(0, 800, 50))

            for i in range(4):
                img = sprite_icon_vida.subsurface((i*32, 0), (32, 32))
                img = pygame.transform.scale(img, ((2 * 32), (2 * 32)))
                self.icon_vida.append(img)

            self.cont = 0
            self.image = self.icon_vida[int(self.cont)]

            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

            self.rect.topleft = self.x_icon, self.y_icon

        def update(self):
            if self.rect[1] < 580:
                self.rect[1] += 5

            if pygame.key.get_pressed()[K_SPACE]:
                self.velocidade = 25
            else:
                self.velocidade = 15

            if cenario_1.andar_direita:
                if pygame.key.get_pressed()[K_a] and jogador.rect[0] <= 640:
                    self.rect[0] += self.velocidade

            if cenario_1.andar_esquerda:
                if pygame.key.get_pressed()[K_d] and jogador.rect[0] >= 440:
                    self.rect[0] -= self.velocidade

    class Cenario_1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprite_cenario_1 = []
            self.x_arvore, self.y_arvore = -500, (-3 * 720)-90
            self.velocidade = 15

            for i in range(3):
                for j in range(8):
                    img = sprite_cenario_1.subsurface((j * 2160, i * 1440), (2160, 1440))
                    img = pygame.transform.scale(img, (2 * 2160, 2 * 1440))
                    self.sprite_cenario_1.append(img)

            self.cont = 0
            self.image = self.sprite_cenario_1[int(self.cont)]

            self.rect = self.image.get_rect()

            self.rect.topleft = self.x_arvore, self.y_arvore

            self.andar_direita = False
            self.andar_esquerda = False

        def Andar_direita(self):
            self.andar_direita = True
            self.andar_esquerda = False

        def Andar_esquerda(self):
            self.andar_esquerda = True
            self.andar_direita = False

        def update(self):
            if self.rect.topleft[0] >= 0:
                self.andar_direita = False

            if self.rect.topright[0] <= 1080:
                self.andar_esquerda = False

            self.cont += 0.25

            if self.cont > len(self.sprite_cenario_1):
                self.cont = 0

            self.image = self.sprite_cenario_1[int(self.cont % len(self.sprite_cenario_1))]

            if pygame.key.get_pressed()[K_SPACE]:
                self.velocidade = 25
            else:
                self.velocidade = 15

            if self.andar_direita:
                if pygame.key.get_pressed()[K_a] and jogador.rect[0] <= 640:
                    self.rect[0] += self.velocidade

            if self.andar_esquerda:
                if pygame.key.get_pressed()[K_d] and jogador.rect[0] >= 440:
                    self.rect[0] -= self.velocidade

    # player
    todas_sprites_jogador = pygame.sprite.Group()
    jogador = Player()
    todas_sprites_jogador.add(jogador)

    # bots
    bichoranha = Bot()
    todas_sprites_jogador.add(bichoranha)

    # icons
    vida = Icon()
    icons = pygame.sprite.Group()
    icons.add(vida)

    # itens
    itens_ruins = pygame.sprite.Group()
    itens_bons = pygame.sprite.Group()
    vida_grupo = pygame.sprite.Group()

    # cenario
    cenario = pygame.image.load(diretorio_cenario_fundo).convert_alpha()
    cenario = pygame.transform.scale(cenario, (1080, 720))

    chao = pygame.image.load(diretorio_chao).convert_alpha()
    chao = pygame.transform.scale(chao, (1080, 720))

    cenario_1 = Cenario_1()
    cenarios = pygame.sprite.Group()
    cenarios.add(cenario_1)

    # menu e tela game over
    menu_tela = pygame.image.load(diretorio_menu_tela).convert_alpha()
    menu_tela = pygame.transform.scale(menu_tela, (largura, altura))

    menu_tela_1 = pygame.image.load(diretorio_menu_tela_1).convert_alpha()
    menu_tela_1 = pygame.transform.scale(menu_tela_1, (largura, altura))

    gameover = pygame.image.load(diretorio_tela_gameover).convert()
    gameover = pygame.transform.scale(gameover, (largura, altura))

    # musicas e sons
    pygame.mixer.music.load(diretorio_music_1)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    coleta_som = pygame.mixer.Sound(diretorio_song_coleta)
    coleta_som.set_volume(0.75)

    dano_som = pygame.mixer.Sound(diretorio_song_dano)
    dano_som.set_volume(0.25)

    coleta_vida_som = pygame.mixer.Sound(diretorio_song_coleta_vida)
    coleta_vida_som.set_volume(0.25)

    menu()


abrir_jogo()
