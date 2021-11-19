from math import *
from numpy import *
from matplotlib.pyplot import *

#fonction qui permet de faire automatiquement la dérivée d'une fonction
def derivee(f,x):
    h=1e-10
    return (f(x+h)-f(x))/h

 #fonction pour calculer une integrale d'une fonction de 0 a x
def primitive(f,x):
    h=1e-2
    #partie calcul integrale par methode des rectangles
    s=0
    for i in range(0,int(x/h)):
        s+=h*f(h*i)
    return s

#fonction qui derrive un tableau par rapport a une fonction avec un pas de h
def derivee_tableau(f,h,tab):
    #on cree un tableau de la meme taille que le tableau d'entree
    tab_derivee=[]
    for i in range(0,len(tab)):
        tab_derivee.append(0)
    #on parcourt le tableau d'entree
    for i in range(0,len(tab)):
        #on calcule la derivee de la fonction
        tab_derivee[i]=derivee(f,tab[i])
    return tab_derivee

#fonction qui fait la primitive d'un tableau par rapport a une fonction avec un pas de h
def primitive_tableau(f,h,tab):
    #on cree un tableau de la meme taille que le tableau d'entree
    tab_primitive=[]
    for i in range(0,len(tab)):
        tab_primitive.append(0)
    #on parcourt le tableau d'entree
    for i in range(0,len(tab)):
        #on calcule la primitive de la fonction
        tab_primitive[i]=primitive(f,tab[i])
    return tab_primitive

#partie exemples !

#primitive de la fonction sinus avec un pas de 0.1 de 0 a pi
x = linspace(0,8*pi,1000)
tab_primitive=primitive_tableau(sin,0.1,x)
tab_derivee=derivee_tableau(sin,0.1,x)

#creer un tableau qui contient sin(x) de 0 a pi avec un pas de 0.1
tab_sin=[]
for i in range(0,len(x)):
    tab_sin.append(sin(x[i]))

#afficher les tableaux
plot(x,tab_sin,label="sin(x)",color="red")
plot(x,tab_primitive,label="primitive",color="blue")
plot(x,tab_derivee,label="derivee",color="green")
legend(loc="upper left")
show()