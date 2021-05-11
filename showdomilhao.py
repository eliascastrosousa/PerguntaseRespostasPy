import pygame
from time import sleep



print('####### BEM VINDO AO QUIZ SOBRE CINEMA 1.0 #######')

sleep(1)
print('Este Quiz tera 4 rodadas de perguntas, de forma decrescente')
sleep(1)
print('sendo a ultima rodada sendo a pergunta do milhão!')

sleep(1)
print('Você Gosta de cinema? vamos testar seus conhecimentos!')


pygame.init()
pygame.mixer.music.load('show-do-milhao2.mp3') #tema de abertura
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
sleep(1.5)

print('VAMOS JOGAR!')
sleep(1)


pygame.init()
pygame.mixer.music.load('perguntashowdomilhao.mp3') #musica para pergunta
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
sleep(1.5)
resposta_certa = 0
print('---'*20)
sleep(1)

print('PRIMEIRA RODADA, 4 PERGUNTAS! ')
sleep(1)

#('PERGUNTA 1.1')

print('Qual é a maior bilheteria do cinema? ')
sleep(2)
print('1) Avatar – US$ 2.790 bilhões')
sleep(1)
print('2) Titanic – US$ 2.196 bilhões')
sleep(1)
print('3) Vingadores: Ultimato – US$ 2.797 bilhões')
sleep(1)
print('4) Star Wars: Episódio VII – O Despertar da Força – US$ 2.068 bilhões')
sleep(1)
print('5) Vingadores: Guerra Infinita – US$ 2.048 bilhões')
sleep(1)
p1_1 = int(input('Resposta: '))

sleep(2)

if p1_1 == 3:
    print('CERTA RESPOSTA!')
    resposta_certa += 1
    pygame.init()
    pygame.mixer.music.load('certaresposta.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)


else:
    print('ERROU!')
    pygame.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)


pygame.init()
pygame.mixer.music.load('perguntashowdomilhao.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
sleep(1.5)

#('PERGUNTA 1.2')


print('Em que ano foi lançado Titanic:')
sleep(2)
print('1) 1995')
sleep(1)
print('2) 1997')
sleep(1)
print('3) 2001')
sleep(1)
print('4) 2000')
sleep(1)
print('5) 1994')
sleep(1)
p1_2 = int(input('Resposta: '))
sleep(2)


if p1_2 == 2:
    print('CERTA RESPOSTA!')
    resposta_certa += 1
    pygame.init()
    pygame.mixer.music.load('certaresposta.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)


else:
    print('ERROU!')
    pygame.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)


pygame.init()
pygame.mixer.music.load('perguntashowdomilhao.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
sleep(1.5)

#('PERGUNTA 1.3')


print('Qual o primeiro longa metragem de Quantim Tarantino')
sleep(2)
print('1) Django Livre')
sleep(1)
print('2) À Prova de Morte')
sleep(1)
print('3) Pulp Fiction - Tempo de Violência')
sleep(1)
print('4) Cães de Aluguel')
sleep(1)
print('5) Kill Bill - Volume 1')
p1_3 = int(input('Resposta: '))
sleep(2)
if p1_3 == 4:
    print('CERTA RESPOSTA!')
    resposta_certa += 1
    pygame.init()
    pygame.mixer.music.load('certaresposta.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)

else:
    print('ERROU!')
    pygame.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)


pygame.init()
pygame.mixer.music.load('perguntashowdomilhao.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
sleep(1.5)

#('PERGUNTA 1.4')


print('Quantos filmes tem a franquia "Rocky" ')
sleep(2)
print('1) Um')
sleep(1)
print('2) Três')
sleep(1)
print('3) Sete')
sleep(1)
print('4) Cinco')
sleep(1)
print('5) Oito')
sleep(1)
p1_4 = int(input('Resposta: '))
sleep(2)


if p1_4 == 4:
    print('CERTA RESPOSTA!')
    resposta_certa += 1
    pygame.init()
    pygame.mixer.music.load('certaresposta.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)


else:
    print('ERROU!')
    pygame.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)

print('VOCÊ TEVE UM TOTAL DE {} RESPOSTAS CERTAS!'.format(resposta_certa))
sleep(2)

if resposta_certa == 4:
    print('Você passou para a proxima fase!! Parabens')
    sleep(1.5)
    print('Vamos para mais uma rodada de perguntas!')
    sleep(1.5)
    resposta_certa2 = 0
    print('---'*20)

    print('SEGUNDA RODADA, 3 PERGUNTAS! ')
    sleep(1)

    sleep(2)
    pygame.init()
    pygame.mixer.music.load('perguntashowdomilhao.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)

    print('De Qual filme vem a cena épica de Mel Gibson clamando por Liberdade?')
    sleep(2)
    print('1) Braveheart')
    sleep(1)
    print('2) A Paixão de Cristo ')
    sleep(1)
    print('3) Máquina Mortifera')
    sleep(1)
    print('4) Mad Max')
    sleep(1)
    print('5) O Patriota ')
    sleep(1)
    p2_1 = int(input('Resposta: '))
    sleep(2)


    if p2_1 == 1:
        print('CERTA RESPOSTA!')
        resposta_certa2 += 1
        pygame.init()
        pygame.mixer.music.load('certaresposta.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)


    else:
        print('ERROU!')
        pygame.init()
        pygame.mixer.music.load('errou.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)


    pygame.init()
    pygame.mixer.music.load('perguntashowdomilhao.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)

    #('PERGUNTA 2.2')

    print('Qual ator e Atriz são os maiores ganhadores \ndo oscar de melhor ator e atriz respectivamente?')
    sleep(2)
    print('1) Brad Pitt e angelina jolie')
    sleep(1)
    print('2) Tom Hanks e Meryl Streep')
    sleep(1)
    print('3) Marlon Brando e Sophia Loren')
    sleep(1)
    print('4) Christian Bale e Julia Roberts')
    sleep(1)
    print('5) Daniel Day-Lewis e Katharine Hepburn')
    sleep(1)
    p2_2 = int(input('Resposta: '))
    sleep(2)

    if p2_2 == 5:
        print('CERTA RESPOSTA!')
        resposta_certa2 += 1
        pygame.init()
        pygame.mixer.music.load('certaresposta.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)


    else:
        print('ERROU!')
        pygame.init()
        pygame.mixer.music.load('errou.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)


    pygame.init()
    pygame.mixer.music.load('perguntashowdomilhao.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass
    sleep(1.5)

    #('PERGUNTA 2.3')
    sleep(1)

    print('Qual filme nacional com mais indicações ao oscar')
    sleep(2)
    print('1) Central do Brasil')
    sleep(1)
    print('2) O Pagador de Promessas (1963)')
    sleep(1)
    print('3) Cidade de Deus')
    sleep(1)
    print('4) O Beijo da Mulher-Aranha ')
    sleep(1)
    print('5) Bacurau')
    sleep(1)
    p2_3 = int(input('Resposta: '))
    sleep(2)


    if p2_3 == 3:
        print('CERTA RESPOSTA!')
        resposta_certa2 += 1
        pygame.init()
        pygame.mixer.music.load('certaresposta.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)


    else:
        print('ERROU!')
        pygame.init()
        pygame.mixer.music.load('errou.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)

    print('NESTA RODADA VOCÊ TEVE UM TOTAL DE {} RESPOSTAS CERTAS!'.format(resposta_certa2))
    sleep(2)

    if resposta_certa2 == 3:
        print('Você passou para a proxima fase!! Parabens!')
        sleep(1)
        print('Vamos para a pnultima rodada de perguntas!')
        sleep(1.5)
        resposta_certa3 = 0
        print('---' * 20)

        print('TERCEIRA RODADA, 2 PERGUNTAS! ')
        sleep(1)


        pygame.init()
        pygame.mixer.music.load('perguntashowdomilhao.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)

        #('PERGUNTA 3.1')


        print('Em que ano surgiu o cinema?')
        sleep(2)
        print('1) 1900')
        sleep(1)
        print('2) 1897')
        sleep(1)
        print('3) 1940')
        sleep(1)
        print('4) 1895')
        sleep(1)
        print('5) 1945')
        p3_1 = int(input('Resposta: '))
        sleep(2)


        if p3_1 == 2:
            print('CERTA RESPOSTA!')
            resposta_certa3 += 1
            pygame.init()
            pygame.mixer.music.load('certaresposta.mp3')
            pygame.mixer.music.play()
            while (pygame.mixer.music.get_busy()): pass
            sleep(1.5)


        else:
            print('ERROU!')
            pygame.init()
            pygame.mixer.music.load('errou.mp3')
            pygame.mixer.music.play()
            while (pygame.mixer.music.get_busy()): pass
            sleep(1.5)


        pygame.init()
        pygame.mixer.music.load('perguntashowdomilhao.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        sleep(1.5)

        #('PERGUNTA 3.2')

        print('A Qual filme está atrelado a musica "singing in the rain"  ')
        sleep(2)
        print('1) Tempos Modernos')
        sleep(1)
        print('2) Sherlock Jr.')
        sleep(1)
        print('3) Cantando na Chuva')
        sleep(1)
        print('4) La La land')
        sleep(1)
        print('5) Grease')
        sleep(1)
        p3_2 = int(input('Resposta: '))
        sleep(2)


        if p3_2 == 3:
            print('CERTA RESPOSTA!')
            resposta_certa3 += 1
            pygame.init()
            pygame.mixer.music.load('certaresposta.mp3')
            pygame.mixer.music.play()
            while (pygame.mixer.music.get_busy()): pass
            sleep(1.5)


        else:
            print('ERROU!')
            pygame.init()
            pygame.mixer.music.load('errou.mp3')
            pygame.mixer.music.play()
            while (pygame.mixer.music.get_busy()): pass
            sleep(1.5)

        print('NESTA RODADA VOCÊ ACERTOU {}!'.format(resposta_certa3))
        sleep(2)


        if resposta_certa3 == 2:
            print('Você passou para a ULTIMA fase!!!')
            sleep(1)
            sleep(1.5)

            resposta_certa4 = 0
            print('AGORA VALENDO UM MILHÃO! ')
            sleep(2)

            print('QUARTA E ULTIMA RODADA, 1 PERGUNTA! ')
            sleep(2)

            print('Quem matou odete roitman')
            sleep(2)
            print('1) Leila')
            sleep(1)
            print('2) Carminha')
            sleep(1)
            print('3) Tereza Cristina')
            sleep(1)
            print('4) Yvone  ')
            sleep(1)
            print('5) Aline Noronha')
            sleep(1)
            p4_1 = int(input('Resposta: '))
            sleep(2)


            if p4_1 == 1:
                print('CERTA RESPOSTA!')

                resposta_certa4 += 1
                pygame.init()
                pygame.mixer.music.load('certaresposta.mp3')
                pygame.mixer.music.play()
                while (pygame.mixer.music.get_busy()): pass
                sleep(1.5)
                print('PARABENS, VOCÊ VENCEU O QUIZ SOBRE CINEMA 1.0!! E GANHOU UM MILHÃO!! ')
                print('file:///C:/Users/elias/Downloads/download%20(1).jpg')
                print('AQUI ESTA ELE! ATÉ A PROXIMA! ')

            else:
                print('ERROU!')
                pygame.init()
                pygame.mixer.music.load('errou.mp3')
                pygame.mixer.music.play()
                while (pygame.mixer.music.get_busy()): pass
                sleep(1.5)

                print('POXA, CHEGOU TÃO LONGE PRA PERDER AQUI? QUE PENA.\n SEE YOU LATER!')
        else:
            print('VOCÊ QUASE CONSEGUIU, MAS NAO VAI SER DESSA VEZ.\n  SEE YOU LATER!')

    else:
        print('Infelizmente sua tragetoria se encerra por aqui. SEE YOU LATER!')

else:
    print('Infelizmente sua tragetoria se encerra por aqui. até a proxima!')



