# Nome: Allan Victor Gonçalves Evangelista


import turtle
from math import pi
from sys import exit


#  Desenha retangulo de lado L e altura A
def retangulo(dados, ladoRetangulo, alturaRetangulo):
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientacaneta) = dados# Separação da tupla que chegou

    caneta.pensize(penSize)
    caneta.color(penCor, corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)
    caneta.setheading(orientacaneta)
    caneta.pendown()
    caneta.begin_fill()

    for i in range(2):
        caneta.forward(ladoRetangulo)
        caneta.left(360 / 4)# resulta no angulo interno de um poligono de N lados. nesse caso 90
        caneta.forward(alturaRetangulo)
        caneta.left(360 / 4)# vira 90 graus e o laço repete o processo terminando o retangulo

    caneta.end_fill()
    caneta.penup()


def poligonoNLados(dados, Tamlado, qtdLados):# Desenha poligono de N lados
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientaCaneta) = dados

    caneta.setheading(orientaCaneta)
    caneta.pensize(penSize)
    caneta.color(penCor, corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)
    caneta.pendown()
    caneta.begin_fill()

    for i in range(qtdLados):
        caneta.forward(Tamlado)
        caneta.left(360 / qtdLados)#Caneta vira no angulo de acordo com a qtd de lados

    caneta.end_fill()
    caneta.penup()


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

    for i in range(360):
        caneta.forward(comprimentoCirc / 360)# determina o tamanho dos lados
        caneta.left(1)# vira a caneta em 1 grau

    caneta.end_fill()
    caneta.penup()

def trianguloRetangulo(dados, cateto1, cateto2):# Desenha triangulo retangulo
    (caneta, penCor, corPreenchimento, penSize, posi_X, posi_Y, orientaCaneta) = dados

    caneta.setheading(orientaCaneta)
    caneta.pensize(penSize)
    caneta.color(penCor)
    caneta.fillcolor(corPreenchimento)
    caneta.penup()
    caneta.goto(posi_X, posi_Y)
    caneta.pendown()
    caneta.begin_fill()

    #começa o desenho
    caneta.forward(cateto1)
    caneta.left(90)
    caneta.forward(cateto2)
    caneta.goto(posi_X, posi_Y)
    caneta.end_fill()
    caneta.penup()

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

def verificaNumInt(msg):
    ehNum = False

    while True:
        num = input(msg)
        try:
            num = int(num) # Se num for um str literal ex:'Oito'. Teremos erro na conversão para int e execução vai para except
            ehNum = True
        except:
            print("Erro! Apenas valores numéricos aqui.")
        if (ehNum):# Se ehNum for == true, então não tivemos erros no try, significando que num é um int.
            return num 

def verificaTxt(msg):# Verifica se o valor entrado é um texto
    while True:
        texto = input(msg)
        try:
            texto = int(texto) # se a conversão acontecer significa que o user entrou um número e é mostrado msg de erro.
            print("Erro! Apenas texto aqui")
        except:
            return texto # Como desejamos que haja erro no try se entrar no except retornamos a variavel.

def mostraCores():
    print("\nCores Disponiveis")
    for i in range(len(cores)):
        print(cores[i])

def verificaSeEhCorValida(msg):
    while True:
        mostraCores()
        cor = verificaTxt(msg)
        if(cor.lower() in cores):
            return cor
        else:
            print(f"{cor} não é uma cor disponivel. Tente novamente")
            continue

#  int main(){

cores = ("red", "green", "lightgreen", "blue", "lightblue", "pink", "orange", "yellow", "lightgrey", "brown", "black" "\n")
janela = turtle.Screen()
c = turtle.Turtle()
valores = []

while True:# Laço principal do programa.


    print("Escolha uma opção:")
    opcao = verificaNumInt("1-Retângulo\n2-Poligono de N lados\n3-Circulo\n4-Triângulo Retângulo\n0-Sair\n")
    continuar = 0 

    if(opcao == 1):
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
        
        while True:
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')
            if (continuar < 0 or continuar > 1):
                print("Opção invalida! Tente novamente.")
                continue
            else:
                break

    elif(opcao == 2):
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
        
        while True:
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')
            if(continuar < 0 or continuar > 1):
                continue
            else:
                break


    elif(opcao == 3):
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
        
        while True:
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')

            if (continuar < 0 or continuar > 1):
                continue
            else:
                break

    elif(opcao == 4):
        canetaCor = verificaSeEhCorValida("Cor da caneta:")
        corDesenho = verificaSeEhCorValida("Cor interna do desenho:")
        tamCaneta = verificaNum("Espessura da caneta em pixels:")
        posiX = verificaNumInt('Posição inicial da caneta no eixo X:')
        posiY = verificaNumInt("Posição inicial da caneta no eixo Y:")
        cateto_1 = verificaNum('Tamanho do 1° cateto:')
        cateto_2 = verificaNum('Tamanho do 2° cateto:')
        orientaPen = verificaNumInt('Orientação da caneta:')
        dados = (c, canetaCor, corDesenho, tamCaneta, posiX, posiY, orientaPen)
        trianguloRetangulo(dados, cateto_1, cateto_2)
        valores.append("Triângulo retângulo")
        valores.append(cateto_1)
        valores.append(cateto_2)
        valores.append(dados[1:])
        
        while True:
            continuar = verificaNumInt('\n1-Continuar\n0-Sair\n')
            if (continuar < 0 or continuar > 1):
                continue
            else:
                break
                
    elif(opcao == 0):# Opção de sair do programa.
        exit()
        break
    else:# caso opcao nao seja 1 2 3 4 ou 0 é opçao inválida.
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
