#Rebecca Smith
#Seccion 20

from gl import Renderer, color, v2
import random

w=800
h=500

rend= Renderer(w,h)

def drawP(poligono,color=None):
    for i in range(len(poligono)):
        rend.glLine(poligono[i], poligono[(i+1)% len(poligono)],color)


pol1 = [v2(165, 380), v2(185, 360), v2(180, 330), v2(207, 345), 
        v2(233, 330) ,v2(230, 360), v2(250, 380) ,v2(220, 385), 
        v2(205, 410) ,v2(193, 383)]
pol2=[v2(321, 335) ,v2(288, 286),v2 (339, 251) ,v2(374, 302)]
pol3=[v2(377, 249),v2(411, 197) ,v2(436, 249)]
pol4=[v2(413, 177),v2(448, 159),v2(502, 88),v2(553, 53),v2(535, 36),v2(676, 37),v2(660, 52),v2(750, 145),v2(761, 179),v2(672, 192) ,v2(659, 214) ,v2(615, 214) ,v2(632, 230),v2 (580, 230),v2(597, 215) ,v2(552, 214) ,v2(517, 144),v2 (466, 180)]
pol5=[v2(682, 175),v2 (708, 120) ,v2(735, 148),v2 (739, 170)]



drawP(pol1,color(1,1,0))
drawP(pol2,color(1,0,1))
drawP(pol3,color(1,0.5,0))
drawP(pol4,color(1,1,1))
drawP(pol5,color(1,1,1))




rend.glFinish("output.bmp")