# cubo.py
import pygame
import math
from lib import*

pygame.init()
ventana = pygame.display.set_mode([800,650])
origen=[400,450]
grados=30
c=50

# Colores de las vistas
linea=negro
frontal=rojo
lateral=azul
superior=morado

def cubo(c):
    p1=[0,0]

    p1=CartesianoPos(origen,p1)
    p2=CartesianoPos(origen,p2)
    p3=CartesianoPos(origen,p3)
    p4=CartesianoPos(origen,p4)
    p5=CartesianoPos(origen,p5)
    p6=CartesianoPos(origen,p6)
    p7=CartesianoPos(origen,p7)
    p8=CartesianoPos(origen,p8)
    p9=CartesianoPos(origen,p9)
    p10=CartesianoPos(origen,p10)
    p11=CartesianoPos(origen,p11)
    p12=CartesianoPos(origen,p12)
    p13=CartesianoPos(origen,p13)
    p14=CartesianoPos(origen,p14)
    p15=CartesianoPos(origen,p15)
    p16=CartesianoPos(origen,p16)
    p1i=CartesianoPos(origen,p1i)




    Punto(ventana,amarillo,p1)

fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            print (event.pos)
            cubo(c)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                c -= 15
                ventana.fill([0,0,0])
                cubo(c)
            if event.key == pygame.K_UP:
                c += 15
                ventana.fill([0,0,0])
                cubo(c)
