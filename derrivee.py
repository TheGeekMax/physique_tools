from math import *

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


#primitive de la fonction 2x en 5
print(primitive(lambda x: 2*x,5))