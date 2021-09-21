# Nome: Allan Victor Gonçalves Evangelista
# Matrícula: 476334

import turtle
from math import pi
from sys import exit





#  Desenha retangulo de lado L e altura A
def retangulo(dados, ladoRetangulo, alturaRetangulo):# Desenha Retangulo
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientacaneta) = dados# Separação da tupla que chegou

    caneta.pensize(penSize)# definimos o tamanho da caneta com o que veio em dados
    caneta.color(penCor, corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)
    caneta.setheading(orientacaneta)
    caneta.pendown()
    caneta.begin_fill()

    for i in range(2):# para cada rodada do laço será desenhado um lado e uma altura do retangulo
        caneta.forward(ladoRetangulo)#caneta se move o tamanho que foi passado em ladoRetangulo
        caneta.left(360 / 4)# resulta no angulo interno de um poligono de N lados. nesse caso 90
        caneta.forward(alturaRetangulo)#Caneta se move o tamanhao da altura
        caneta.left(360 / 4)# vira 90 graus e o laço repete o processo terminando o retangulo

    caneta.end_fill()
    caneta.penup()# levantamos a caneta para poder move-la sem riscar.


def poligonoNLados(dados, Tamlado, qtdLados):# Desenha poligono de N lados
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientaCaneta) = dados

    caneta.setheading(orientaCaneta)
    caneta.pensize(penSize)
    caneta.color(penCor, corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)
    caneta.pendown()
    caneta.begin_fill()# inicia as cores para caneta e preenchimento

    for i in range(qtdLados):# Enquanto não fizer todos os lados
        caneta.forward(Tamlado)# caneta move pra frente
        caneta.left(360 / qtdLados)#Caneta vira no angulo de acordo com a qtd de lados

    caneta.end_fill()# encerra as cores preenchmento do desenho.
    caneta.penup()# levanta caneta para mover sem riscar.


def circulo(dados, raio):# desenha circulo
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientaCaneta) = dados

    comprimentoCirc = (2 * pi) * raio # determina o comprimento do circulo

    caneta.setheading(orientaCaneta)
    caneta.pensize(penSize)
    caneta.color(penCor, corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)
    caneta.pendown()
    caneta.begin_fill()

    for i in range(360):# laço para completar o circulo
        caneta.forward(comprimentoCirc / 360)# determina o tamanho dos lados
        caneta.left(1)# vira a caneta em 1 grau

    caneta.end_fill()
    caneta.penup()# levanta caneta

def trianguloRetangulo(dados, cateto1, cateto2):# Desenha triangulo retangulo
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientaCaneta) = dados

    caneta.setheading(orientaCaneta)
    caneta.pensize(penSize)
    caneta.color(penCor)
    caneta.fillcolor(corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)# leva a caneta ate a posiçao X, Y
    caneta.pendown()# abaixa caneta
    caneta.begin_fill()# inicia as cores

    #começa o desenho
    caneta.forward(cateto1)# caneta se move pra frente o tamanho passado para o cateto1
    caneta.left(90)# caneta vira 90 graus
    caneta.forward(cateto2)# move pra frente o tamanho passado para cateto2
    caneta.goto(posi_X, posi_Y)# retorna a caneta para a posição X, Y desenhando. Assim temos a hipotenusa
    caneta.end_fill()# encerra cores
    caneta.penup()# levanta caneta.

def verificaNum(msg):
    ehNum = False
    valor = 0
    while True:
        num = input(msg)
        if(num.isnumeric() and int(num) >= 0):
            valor = int(num)
            ehNum = True
        else:
            print("Erro! Apenas valores que sejam numéricos e maior ou igual a 0.")
        if(ehNum):
            break
    return valor

def verificaNumInt(msg):# Verifica se o valor entrado não é uma str diferende de um int
    ehNum = False

    while True:
        num = input(msg)# num recebe um input class str
        try:
            num = int(num) # Se num for um str literal ex:'Oito'. Teremos erro na conversão para int e execução vai para except
            ehNum = True
        except:# Caso de num não ter sido convertido pra int.
            print("Erro! Apenas valores numéricos aqui.")
        if (ehNum):# Se ehNum for == true, então não tivemos erros no try, significando que num é um int.
            return num # num é retornado e o laço é interrompido pelo return.

def verificaTxt(msg):# Verifica se o valor entrado é um texto
    while True:
        texto = input(msg)
        try: # Aqui é feito uma tentativa de converter a variavel texto para int
            texto = int(texto) # se a conversão acontecer significa que o user entrou um número e é mostrado msg de erro.
            print("Erro! Apenas texto aqui") # Após o print o laço volta ao início
        except:# no caso de haver erro no try entramos no except
            return texto # Como desejamos que haja erro no try se entrar no except retornamos a variavel e o laço é quebrado.

def mostraCores():
    print("\nCores Disponiveis")
    for i in range(len(cores)):
        print(cores[i])

def verificaSeEhCorValida(msg):
    while True:
        mostraCores()# chama a função mostra cores para printar cores disponiveis
        cor = verificaTxt(msg)# chama a funçao verificaTxt. Quando verificaTxt retornar, o valor retornado é atribuido em cor.
        if(cor.lower() in cores):# Verifica se a variavel cor esta contida na tupla cores.
            return cor # Retorna o valor que sera atribuido em outra variável
        else:# Caso cor nao esteja em cores o laço continua.
            print(f"{cor} não é uma cor disponivel. Tente novamente")
            continue

#  int main(){

# Cores disponiveis
cores = ("red", "green", "lightgreen", "blue", "lightblue", "pink", "orange", "yellow", "lightgrey", "brown", "black" "\n")
janela = turtle.Screen()
c = turtle.Turtle()
valores = []

while True:# Laço principal do programa.


    print("Escolha uma opção:")
    opcao = verificaNumInt("1-Retângulo\n2-Poligono de N lados\n3-Circulo\n4-Triângulo Retângulo\n0-Sair\n")
    # Variável opcao verifica a primitiva escolhida.
    continuar = 0 # variável continuar verifica se user deseja sair.

    if(opcao == 1):
        #  As funções verificaNum/verificaNumInt/verficaSeEhCorValida são chamadas e pedem um valor
        #  Se forem valores válidos as funções retornam o valor e a atribuição é feita. Se não, a função continua pedindo.
        canetaCor = verificaSeEhCorValida("Cor da caneta:")
        corDesenho = verificaSeEhCorValida("Cor interna do desenho:")
        tamCaneta = verificaNum("Espessura da caneta em pixels:")
        posiX = verificaNumInt("Posição inicial da caneta no eixo X:")
        posiY = verificaNumInt("Posição inicial da caneta no eixo Y:")
        lado = verificaNum("Tamanho do lado do retângulo:")
        altura = verificaNum("Altura do retângulo:")
        orientaPen = verificaNumInt("Orientação da caneta em graus:")
        dados = (c, canetaCor, corDesenho, tamCaneta, posiX, posiY, orientaPen)
        retangulo(dados, lado, altura)
        valores.append("Retângulo")
        valores.append(lado)
        valores.append(altura)
        valores.append(dados[1:])
        while True:# Laço para verificar se a variavel continuar é válida.
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')

            if (continuar < 0 or continuar > 1):
                print("Opção invalida! Tente novamente.")
                continue
            else:
                break

    elif(opcao == 2):
        #  As funções verificaNum/verificaNumInt/verficaSeEhCorValida são chamadas e pedem um valor
        #  Se forem valores válidos as funções retornam o valor e a atribuição é feita. Se não, a função continua pedindo.
        canetaCor = verificaSeEhCorValida("Cor da caneta:")
        corDesenho = verificaSeEhCorValida("Cor interna do desenho:")
        tamCaneta = verificaNum("Espessura da caneta em pixels:")
        posiX = verificaNumInt("Posição inicial da caneta no eixo X:")
        posiY = verificaNumInt("Posição inicial da caneta no eixo Y:")
        ladoTam = verificaNum("Tamanho dos lados(Pixels):")
        qtdLado = verificaNum("Número de lados:")
        orientaPen = verificaNumInt('Orientação da caneta em graus:')
        dados = (c, canetaCor, corDesenho, tamCaneta, posiX, posiY, orientaPen)
        poligonoNLados(dados, ladoTam, qtdLado)
        valores.append("Polígono")
        valores.append(ladoTam)
        valores.append(qtdLado)
        valores.append(dados[1:])
        while True:#Laço para verificar se a varriavel continuar é válida.
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')# Chamada da função verificaNumInt

            # Após a função ter retornado e a variavel ter sido atribuída verificação se é continuar < 0 ou continuar > 1
            if(continuar < 0 or continuar > 1):# Se for, foi entrado valor inválido e mantemos o laço até continuar ser 0 ou 1
                continue
            else:# Quebra do laço quando continuar é 0 ou 1.
                break


    elif(opcao == 3):
        #  As funções verificaNum/verificaNumInt/verficaSeEhCorValida são chamadas e pedem um valor
        #  Se forem valores válidos as funções retornam o valor e a atribuição é feita. Se não, a função continua pedindo.
        canetaCor = verificaSeEhCorValida("Cor da caneta:")
        corDesenho = verificaSeEhCorValida("Cor interna do desenho:")
        tamCaneta = verificaNum("Espessura da caneta em pixels:")
        posiX = verificaNumInt('Posição inicial da caneta no eixo X:')
        posiY = verificaNumInt("Posição inicial da caneta no eixo Y:")
        raioCirc = verificaNum('Raio do circulo:')
        orientaPen = verificaNumInt('Orientação da caneta:')
        dados = (c, canetaCor, corDesenho, tamCaneta, posiX, posiY, orientaPen)# Tupla dados guarda todas as primitivas que não raio/tamanhoLado/qtdlado
        circulo(dados, raioCirc)# função circulo é chamada. A tupla dados e o raio são passados como parâmetros.
        valores.append("Circulo")
        valores.append(raioCirc)
        valores.append(dados[1:])
        while True:#Laço para verificar se a varriavel continuar é válida.
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')# Chamada da função verificaNumInt

            # Após a função ter retornado e a variavel ter sido atribuída verificação se é continuar < 0 ou continuar > 1
            if (continuar < 0 or continuar > 1):# se a variavel continuar não estiver no intervalo o laço continua até ser um valor no intervalo
                continue
            else:
                break

    elif(opcao == 4):
        #  Valores são passados para as funções verificaNum/verificaNumInt/verificaCorValida.
        #  Se forem valores válidos as funções retornam o valor e a atribuição é feita, se for inválido a função continua pedindo.
        canetaCor = verificaSeEhCorValida("Cor da caneta:")
        corDesenho = verificaSeEhCorValida("Cor interna do desenho:")
        tamCaneta = verificaNum("Espessura da caneta em pixels:")
        posiX = verificaNumInt('Posição inicial da caneta no eixo X:')
        posiY = verificaNumInt("Posição inicial da caneta no eixo Y:")
        cateto_1 = verificaNum('Tamanho do 1° cateto:')
        cateto_2 = verificaNum('Tamanho do 2° cateto:')
        orientaPen = verificaNumInt('Orientação da caneta:')
        dados = (c, canetaCor, corDesenho, tamCaneta, posiX, posiY, orientaPen)# Tupla dados guarda todas as primitivas que não raio/tamanhoLado/qtdlado
        trianguloRetangulo(dados, cateto_1, cateto_2)# função trianguloRetang é chamada. A tupla dados e os catetos são passados como parâmetros.
        valores.append("Triângulo retângulo")
        valores.append(cateto_1)
        valores.append(cateto_2)
        valores.append(dados[1:])
        while True:#Laço para verificar se a varriavel continuar é válida.
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')# Chamada da função verificaNumInt

            # Após a função ter retornado e a variavel ter sido atribuída verificação se é continuar < 0 ou continuar > 1
            if (continuar < 0 or continuar > 1):# se a variavel continuar não estiver no intervalo o laço continua até ser um valor no intervalo..
                continue
            else:
                break
    elif(opcao == 0):# Opção de sair do programa.
        exit()# fecha a janela
        break
    else:# caso opcao nao seja 1 2 3 4 ou 0 é opçao inválida e o laço continua.
        print("\nOpção inválida! Tente novamente.\n")
        continue
    if (continuar == 1):# opção para continuar desenhando.
        continue
    else:
        print("Valores entrados:")
        print(valores)  # mostramos os valores entrados no programa
        exit()
        break

janela.exitonclick()
