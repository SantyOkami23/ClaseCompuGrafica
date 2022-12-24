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
    p2=[(-c*3),0]
    p2=RotarHorario(p2,-grados)
    p13=[(c*3),0]
    p13=RotarAntihorario(p13,grados)
    p3=[p2[0],(p2[1]+(c*3))]
    p4=[0,0]
    p4[1]=p1[1]+(c*6)
    p6=[(-c*2),0]
    p6=RotarHorario(p6,-grados)
    p6[1]=(p6[1]+(c*3))
    p8=[p6[0],(p6[1]-c)]
    p12=[(-c),0]
    p12=RotarHorario(p12,-grados)
    p12[1]=(p12[1]+(c*2))
    p16=[c,0]
    p16=RotarAntihorario(p16,grados)
    p5=[p16[0],(p16[1]+(c*5))]
    p7=[p5[0],(p5[1]-c)]
    p14=[(c*2),0]
    p14=RotarAntihorario(p14,grados)
    p9=[p14[0],(p14[1]+(c*3))]
    p11=[p1[0],(p1[1]+(c*3))]
    p10=[p16[0],(p16[1]+(c*3))]
    p15=[p16[0],(p16[1]+c)]
    p1i=[p1[0],(p1[1]+c)]

# Se cambian todas las posiciones a coordenadas de pantalla
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

# Se dibujas las vistas invisibles
    pygame.draw.polygon(ventana,superior,[p1,p2,p11,p13,p14,p15,p1i,p16])
    pygame.draw.polygon(ventana,lateral,[p2,p3,p4,p11])
    pygame.draw.polygon(ventana,frontal,[p11,p4,p5,p7,p9,p13])
    pygame.draw.polygon(ventana,lateral,[p1i,p15,p10,p11])
# Se dibuja el isometrico
    pygame.draw.polygon(ventana,frontal,[p1,p2,p3,p6,p8,p12])
    pygame.draw.polygon(ventana,superior,[p3,p4,p5,p6])
    pygame.draw.polygon(ventana,superior,[p8,p7,p9,p12])
    pygame.draw.polygon(ventana,lateral,[p8,p7,p5,p6])
    pygame.draw.polygon(ventana,lateral,[p1,p12,p11,p16])
    pygame.draw.polygon(ventana,lateral,[p14,p13,p9,p10])
    pygame.draw.polygon(ventana,frontal,[p14,p15,p10])

# Se dibujan las lineas invisibles
    """pygame.draw.polygon(ventana,linea,[p1,p2,p11,p13,p14,p15,p1i,p16],3)
    pygame.draw.polygon(ventana,linea,[p2,p3,p4,p11],3)
    pygame.draw.polygon(ventana,linea,[p11,p4,p5,p7,p9,p13],3)
    pygame.draw.polygon(ventana,linea,[p1i,p15,p10,p11],3)"""
# Se dibujan las lineas del isometrico
    pygame.draw.polygon(ventana,linea,[p1,p2,p3,p6,p8,p12],3)
    pygame.draw.polygon(ventana,linea,[p3,p4,p5,p6],3)
    pygame.draw.polygon(ventana,linea,[p8,p7,p9,p12],3)
    pygame.draw.polygon(ventana,linea,[p8,p7,p5,p6],3)
    pygame.draw.polygon(ventana,linea,[p1,p12,p11,p16],3)
    pygame.draw.polygon(ventana,linea,[p14,p13,p9,p10],3)
    pygame.draw.polygon(ventana,linea,[p14,p15,p10],3)
    Punto(ventana,amarillo,p13)
    pygame.display.flip()

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
