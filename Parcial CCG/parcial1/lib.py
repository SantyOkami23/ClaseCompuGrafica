# lib.py
import math
import pygame
# --------------------------------COLORES--------------------------------------------------
rojo=[255,0,0]
blanco=[255,255,255]
azul=[0,255,255]
verde=[54,228,11]
morado=[116,11,228]
negro=[0,0,0]
rosado=[228,11,175]
naranja=[228,136,11]
amarillo=[228,218,11]
listColores=[rojo,amarillo,blanco,rosado,azul,rojo,verde,naranja,morado]
# -------------------------------VECTORES------------------------------------------------
pos=[0,0]
# --------------------------------ENTEROS-------------------------------------------------
x=0
y=0
# -------------------------------FUNCIONES-----------------------------------------------

def Punto (ventana,color,pos):
    pygame.draw.circle(ventana,color,pos,3)
    pygame.display.flip()

def Linea (ventana,color,pos_inicio,pos_final):
    pygame.draw.line(ventana,color,pos_inicio,pos_final,5)
    pygame.display.flip()

def Cartesiano (ventana,pos):
    pygame.draw.line(ventana,azul,[pos[0],(pos[1]-600)],[pos[0],(pos[1]+600)],5)
    pygame.draw.line(ventana,azul,[(pos[0]-600),pos[1]],[(pos[0]+600),pos[1]],5)
    pygame.display.flip()

def Triangulo (ventana,color,a,b,c):
    pygame.draw.polygon(ventana,color,[a,b,c])
    pygame.display.flip()

def RotarHorario (pos,grados):
    grados=math.radians(grados)
    sen=math.sin(grados)
    cose=math.cos(grados)
    x=(pos[0]*cose)-(pos[1]*sen)
    y=(pos[0]*sen)+(pos[1]*cose)
    pos=[int (x),int (y)]
    return pos

def RotarAntihorario (pos,grados):
    grados=math.radians(grados)
    sen=math.sin(grados)
    cose=math.cos(grados)
    x=(pos[0]*cose)-(pos[1]*sen)
    y=(pos[0]*sen)+(pos[1]*cose)
    return [int(x),int(y)]

def CartesianoPos (origen,pos):
    p1=pos[0]+origen[0]
    p2=origen[1]-pos[1]
    return [int(p1),int(p2)]

def PosCartesiano (origen,pos):
    x=pos[0]-origen[0]
    y=origen[1]-pos[1]
    return [int(x),int(y)]

def Polar(r,a):
    ar=math.radians(a)
    x=r*math.cos(ar)
    y=r*math.sin(ar)
    return [int(x),int(y)]
