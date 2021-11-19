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

def integrale(f,a,b):
    return primitive(f,b)-primitive(f,a)

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
