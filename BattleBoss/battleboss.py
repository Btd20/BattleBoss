#Importamos librerias

from os import O_RDONLY
from re import X
import pygame
from pygame import *
import time
import random
import sys, math
pygame.init() # Inicio pygame

#Colores

VERD=(0,211,112)
VERMELL=(255,0,0)
BLAU=(0,205,255)
BLANC=(255,255,255)
NEGRE=(0,0,0)
GROC=(245,182,0)

#Pantalla videojuego

pantalla=pygame.display.set_mode([800,500]) # Ponemos tamaño a la pantalla
pygame.display.set_caption("BattleBoss") # Ponemos titulo a la ventana

########## PANTALLA DE CARGA ##########

#Fondo de pantalla de carga

pantallainicio=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\pfondo1.jpg") # Cargamos imagen
pantallainicio=pygame.transform.scale(pantallainicio,[800,500]) # Le damos tamaño a una imagen
controles=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\controles.png")

#Título videojuego

battleboss=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\battleboss.png")
battleboss=pygame.transform.scale(battleboss,[550,150])
rectbattleboss=battleboss.get_rect() # Hacemos un rectangulo a partir de la imagen
rectbattleboss.center=([400,140]) # Le damos un centro al rectangulo

#Ratón i colisiones - Flecha de madera que actua como cursor

class Raton(pygame.sprite.Sprite): # Creamos una clase para el cursor
    def __init__(self): # Iniciamos constructor
        super().__init__()
        pygame.mouse.set_visible(False) # Ponemos el cursor en invisible
        self.superficie=pygame.Surface([4,4]) # Creamos una superfície de 4x4
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\cursor.png") # Cargamos la imagen
        self.rect=self.superficie.get_rect() # Hacemos un rectangulo a partir de la superficie
        self.rect.x=0 # El rectangulo se engancha en x 0
        self.rect.y=0 # El rectangulo se engancha en y 0
    def update_pos(self): # Función para que la superfície esté en medio
        self.rect.x=pygame.mouse.get_pos()[0]-2 # Le restamos 2 a x
        self.rect.y=pygame.mouse.get_pos()[1]-2 # Le restamos 2 a y
    def chocke(self): # Funcion que comprueba una colision
        if pygame.sprite.collide_rect(self, BotonPlay): # If que comprueba si la colision es verdadera o falsa
            empezar() # Se ejecuta la función empezzar que inicia el juego
    def colisionvida(self): # Funcion que comprueba una colision
        if pygame.sprite.collide_rect(self, botonvida): # If que comprueba si la colision es verdadera o falsa
            botonvida.sumarvida() # Se ejecuta la función sumarvida
    def colisionfuerza(self): # Funcion que comprueba una colision
        if pygame.sprite.collide_rect(self, botonfuerza):# If que comprueba si la colision es verdadera o falsa
            botonfuerza.sumarfuerza() # Se ejecuta la función sumarfuerza
  
cursor=Raton() # Le damos el nombre cursor al objeto de la clase Raton

#Botón de play - Botón al que clicas para iniciar el juego

class CuadradoPlay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\pplay.png")
        self.image=pygame.transform.scale(self.image,[180,120])
        self.rect=self.image.get_rect()
        self.rect.center=([400,340])

BotonPlay=CuadradoPlay()

#Sumar +10 de vida

class Curacion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.curacion=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\curacion.png")
        self.curacion=pygame.transform.scale(self.curacion,[90,90])
        self.rect=self.curacion.get_rect()
        self.rect.x=10
        self.rect.y=400
        self.vida=100 # Creamos la variable de vida que es 100
    def sumarvida(self):
        if monedas.oro>=250: # Si las monedas son igual o más que 250 se ejecuta
            self.vida=self.vida+10 # Se suma 10 de vida
            monedas.oro=monedas.oro-250 # Se resta 250 de oro

botonvida=Curacion()

#Sumar +10 fuerza

class Fuerza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fuerzaimagen=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\fuerza.png")
        self.fuerzaimagen=pygame.transform.scale(self.fuerzaimagen,[90,90])
        self.rect=self.fuerzaimagen.get_rect()
        self.rect.x=110
        self.rect.y=400
        self.fuerza=100 # Creamos la variable fuerza que es 100
    def sumarfuerza(self):
        if monedas.oro>=250:
            self.fuerza=self.fuerza+10 # Sumamos 10 de fuerza
            monedas.oro=monedas.oro-250 # Restamos 250 de oro

botonfuerza=Fuerza()

#Dinero del videojuego

class Oro():
    def __init__(self):
        super().__init__()
        self.oro=500 # Creamos la variable oro que es 500

monedas=Oro()

#Enemigo 1 personaje y ataque

class Nivel():
    def __init__(self):
        super().__init__()
        self.nivelenemigo=1 # Creamos el nivel para los enemigos

nivelenemigo=Nivel()


class Enemigo1(pygame.sprite.Sprite): # Clase para el primer enemigo
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\enemigo1.png")
        self.image=pygame.transform.scale(self.image,[80,130])
        self.rect=self.image.get_rect()
        self.rect.x=600
        self.rect.y=305
        self.vida=25 # Vida inicial del enemigo
        self.muertes=1 # Numero de muertes del enemigo

enemigo1=Enemigo1()

class Ataqueenemigo1(pygame.sprite.Sprite): # Clase para el ataque del enemigo
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\disparoenemigo1.png")
        self.rect=self.image.get_rect()
        self.dañoenemigo=15 # Definimos el daño del enemigo que es 15
        self.velocidad=2 # La velocidad de disparo es 2
        self.constancia=0.5 # La constancia del disparo es 0.5
    def update(self):
        self.rect.x-=15+self.velocidad # Le vamos sumando velocidad al disparo cada vez que se ejecuta la funcion
    def colision(self):
        if pygame.sprite.collide_rect(self, yo):
            botonvida.vida=botonvida.vida-self.dañoenemigo # Si colisiona su ataque con nuestro personaje nos quita vida

disparoenemigo=Ataqueenemigo1()

#Enemigo 2 personaje y ataque

class Enemigo2(pygame.sprite.Sprite): # Clase para el segundo enemigo
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\enemigo2.png")
        self.image=pygame.transform.scale(self.image,[80,130])
        self.rect=self.image.get_rect()
        self.rect.x=600
        self.rect.y=305
        self.vida=25
        self.muertes=1

enemigo2=Enemigo2()

#Enemigo 3 personaje y ataque

class Enemigo3(pygame.sprite.Sprite): # Clase para el tercer enemigo
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\enemigo3.png")
        self.image=pygame.transform.scale(self.image,[110,130])
        self.rect=self.image.get_rect()
        self.rect.x=600
        self.rect.y=305
        self.vida=25
        self.muertes=1

enemigo3=Enemigo3()

#Disparo normal y personaje

class Personaje(pygame.sprite.Sprite): # Clase para nuestro personaje
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\personaje.png")
        self.image=pygame.transform.scale(self.image,[80,130])
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=305

yo=Personaje()

class Midisparo(pygame.sprite.Sprite): # Clase para nuestro disparo normal
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\disparo.png")
        self.rect=self.image.get_rect()
        self.midaño=botonfuerza.fuerza*0.02 # Daño del disparo se multiplica por la fuerza que tengamos
    def update(self):
        self.rect.x+=15 # La velocidad de nuestro disparo siempre es la misma

#Disparo definitivo personaje

class Midefinitiva(pygame.sprite.Sprite): # Clase para nuestro disparo definitivo
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\definitiva.png")
        self.image=pygame.transform.scale(self.image,[100,68])
        self.rect=self.image.get_rect()
        self.daño=botonfuerza.fuerza*0.05 # El daño de nuestra definitiva es más que el normal
    def update(self):
        self.rect.x+=15 # La velocidad de la definitiva es siempre la misma

#Disparo definitivo enemigo

class Enemigodefinitiva(pygame.sprite.Sprite): # Definitiva del enemigo
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\definitivaenemigo.png")
        self.image=pygame.transform.scale(self.image,[100,68])
        self.rect=self.image.get_rect()
        self.daño=25
        self.velocidad=2
    def update(self):
        self.rect.x-=20 # La definitiva del enemigo es más rápida que la nuestra, va restando 20

definitivaenemigo=Enemigodefinitiva()

#Reiniciar stats

def reinicioenemigo(enemigoelegido): # Función para cuando matemos a un enemigo

    enemigo1.muertes=enemigo1.muertes+1 # Sumamos una muerte al enemigo 1
    enemigo2.muertes=enemigo2.muertes+1 # Sumamos una muerte al enemigo 2
    enemigo3.muertes=enemigo3.muertes+1 # Sumamos una muerte al enemigo 3

    enemigo1.vida=25*enemigo1.muertes # Multiplicamos la vida del enemigo 1 por sus muertes
    enemigo2.vida=25*enemigo2.muertes # Multiplicamos la vida del enemigo 2 por sus muertes
    enemigo3.vida=25*enemigo3.muertes # Multiplicamos la vida del enemigo 3 por sus muertes

    barrera.rect.x=520 # Decimos donde se enganchará la barrera en x
    barrera.rect.y=0 # Decimos donde se enganchará la barrera en y

    nivelenemigo.nivelenemigo=nivelenemigo.nivelenemigo+1 # Sumamos 1 nivel al enemigo
    enemigoelegido.image=enemigoelegido.image # Ponemos la imagen del enemigo

    monedas.oro=monedas.oro+150*nivelenemigo.nivelenemigo # Sumamos 150 de oro multiplicado por el nivel del enemigo

    disparoenemigo.dañoenemigo=15*nivelenemigo.nivelenemigo # Multiplicamos el daño del enemigo por su nivel
    definitivaenemigo.daño=25*nivelenemigo.nivelenemigo # Multiplicamos el daño de la definitiva del enemigo por su nivel

    definitivaenemigo.velocidad=definitivaenemigo.velocidad*1.5 # Multiplicamos la velocidad de la definitiva del enemigo x1.5

    disparoenemigo.velocidad=disparoenemigo.velocidad*1.5 # Multiplicamos la velocidad del disparo del enemigo x1.5

    empezar() # Volvemos a iniciar el juego

#Barrera

class Barrerainicio(pygame.sprite.Sprite): # Clase para la barrera al comenzar
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\barrera.png")
        self.rect=self.image.get_rect()
        self.rect.x=520
        self.rect.y=0

barrera=Barrerainicio()

#GameOver

def gameover(): # Función que se ejecuta al perder y aparece una imagen de que has perdido
    gameover=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\gameover.png")
    pantalla.blit(gameover,[0,0]) # Enganchamos imagen de game over

#Funcion del videojuego

def empezar(): # Función del videojuego

    aleatorio=random.randrange(3) # Aleatorio entre 3 para elegir un enemigo
    lista_enemigos=[enemigo1,enemigo2,enemigo3] # Lista de los 3 objetos enemigos
    enemigoelegido=lista_enemigos[aleatorio] # Elegimos un enemigo de la lista a partir del aleatorio

    #Cargar y reescalar imagenes
    
    pantallainicio=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\fondojuego.jpg")
    corazon=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\corazon.png")
    corazon=pygame.transform.scale(corazon,[25,20])
    textodefinitiva=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\definitivatexto.png")
    pantallainicio=pygame.transform.scale(pantallainicio,[800,500])
    fuerzatexto=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\fuerzatexto.png")
    fuerzatexto=pygame.transform.scale(fuerzatexto,[100,35])
    curaciontexto=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\vidatexto.png")
    curaciontexto=pygame.transform.scale(curaciontexto,[80,35])
    cartel=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\cartelmoneda.png")
    cartel.set_colorkey(BLANC) # Quitamos el fondo blanco a la imagen

    #Variables
    
    listadisparo=pygame.sprite.Group() # Lista de mis disparos como grupo de sprites
    listadefinitiva=pygame.sprite.Group() # Lista de mis definitivas como grupo de sprites
    listadisparoenemigo=pygame.sprite.Group() # Lista de disparos del enemigo como grupo de sprites
    listadefinitivaenemigo=pygame.sprite.Group() # Lista de definitivas del enemigo como grupo de sprites
    battleboss=0 # Quitamos la imagen de titulo
    BotonPlay.image=0 # Quiramos la imagen de boton de play
    global menuempezar # Hacemos que la variable menuempezar sea global
    menuempezar=True # Definimos la variable menuempezar
    tempsinicial=time.time() # Hacemos que la variable tempsinicial sea el tiempo inicial al ejecutar esta funcion
    tiempoataque=3 # Tiempo entre ataque y ataque del enemigo
    tiempodefinitiva=15 # Tiempo entre cada definitiva del enemigo
    tiempobarrera=6 # Tiempo que dura la barrera
    posx=100 # Posicion x es 100
    posy=305 # Posicion y es 305
    angulo=0.0 # Angulo que usaremos para el salto
    vely=0 # Velocidad de movimiento de nuestro personaje
    rellotge=pygame.time.Clock() # Reloj de pygame

    #Fuentes y textos

    fuente1=pygame.font.SysFont("Arial",28) # Fuente que usaremos para los textos
    fuente1sombra=pygame.font.SysFont("Arial",28) # Fuente secundaria que enganchamos detras como sombra

    #Bucle del juego

    while menuempezar: # Mientras menuempezar sea True se ejecutará el bucle
        tempsactual=int(time.time()-tempsinicial) # El tempsactual es una variable int amb el time.time menys el tempsinicial

        #Redondear vidas

        vidaenemigo=round(enemigoelegido.vida,2) # Redondeamos la vidaenemigo para que no muestre muchos decimales

        #Eventos de teclado y ratón

        for evento in pygame.event.get(): # Bucle for para los eventos de pygame
            if evento.type==pygame.QUIT: # Si salimos del programa
                menuempezar=False # menuempezar finaliza
                CondicionRaton=False # CondicionRaton finaliza
            if evento.type==pygame.MOUSEBUTTONDOWN: # Si pulsamos el boton del raton
                cursor.colisionvida() # Ejecutamos la funcion colisionvida de la clase cursor
                cursor.colisionfuerza() # Ejecutamos la funcion colisionfuerza de la clase cursor
                disparo=Midisparo() # Le damos nombre al objeto disparo de la clase Midisparo
                disparo.rect.x=yo.rect.x+65 # Le damos una posicion de donde queremos que salga nuestro disparo en x
                disparo.rect.y=yo.rect.y+45 # Le damos una posicion de donde queremos que salga nuestro disparo en y
                listadisparo.add(disparo) # Añadimos nuestro disparo a la lista de disparos
            if evento.type==pygame.KEYDOWN: # Si pulsamos una tecla
                if evento.key==pygame.K_e and monedas.oro>=50: # Si pulsamos la tecla E y las monedas son mas o igual a 50 se ejecuta
                        monedas.oro=monedas.oro-50 # Restamos 50 monedas
                        definitiva=Midefinitiva() # Damos nombre al objeto definitiva de la clase Midefinitiva
                        definitiva.rect.x=yo.rect.x+65 # Le damos una posicion de donde queremos que salga nuestra definitiva en x
                        definitiva.rect.y=yo.rect.y+45 # Le damos una posicion de donde queremos que salga nuestra definitiva en y
                        listadefinitiva.add(definitiva) # Añadimos nuestra definitiva a la lista de definitivas
            if yo.rect.y==305:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==pygame.K_SPACE:
                        angulo=0.001

        #Es mou el personatge a la dreta
        if key.get_pressed()[K_d]:
            yo.rect.x=yo.rect.x+7
        #Es mou el personatge a la esquerra
        if key.get_pressed()[K_a]:
            yo.rect.x=yo.rect.x-7
        #Salto del personaje - Lo vi de google no se explicar que hace
        yo.rect.y=305-math.sin(angulo)*200
        if angulo > 0:
            angulo=angulo+0.15
        if angulo >= math.pi:
            angulo=0.0

        #Ataques automáticos del enemigo

        if tempsactual==tiempoataque: # Si el tiempo actual es igual al tiempo de ataque (3) se ejecuta
            disparoenemigo.rect.x=600 # Decimos de donde queremos que salga el disparo del enemigo en x
            disparoenemigo.rect.y=350 # Decimos de donde queremos que salga el disparo del enemigo en y
            listadisparoenemigo.add(disparoenemigo) # Añadimos el disparenemigo a la lista de disaparos del enemigo
            tiempoataque=tiempoataque+3 # Sumamos 3 la variable tiempo ataque para que se ejecute el disparo en los siguientes 3 segundos
        
        if tempsactual==tiempodefinitiva: # Si el tiempo actual es igual al tiempo de definitiva (15) se ejecuta
            definitivaenemigo.rect.x=600 # Decimos de donde queremos que salga la definitiva del enemigo en x
            definitivaenemigo.rect.y=350 # Decimos de donde queremos que salga la definitiva del enemigo en y
            listadefinitivaenemigo.add(definitivaenemigo) # Añadimos la definitiva del enemigo a la lista de definitivas enemigo
            tiempodefinitiva=tiempodefinitiva+15 # Sumamos 15 al tiempodefinitiva para que se ejecute en los siguientes 15 segundos

        if tempsactual==tiempobarrera: # Si el tiempo actual es igual al tiempo barrera (6) se ejecuta
            barrera.rect.x=2000 # Enganchamos la barrera fuera de la pantalla para que no esté en medio y bloquee los disparos
            barrera.rect.y=2000 # Enganchamos la barrera fuera de la pantalla para que no esté en medio y bloquee los disparos

        #Limites personaje

        if yo.rect.x<0: # Si mi personaje está en x menos de 0 se ejecuta
            yo.rect.x=0 # Hacemos que no se mueva de 0 enganchandolo en 0
        if yo.rect.x>740: # Si mi personaje está en x mayor que 740 se ejecuta
            yo.rect.x=740 # Hacemos que no se mueva de 740 enganchandolo en 740
        
        #Actualizar lista de disparos ejecutando las funciones update() que hay en las clases

        listadisparo.update()
        listadefinitiva.update()
        listadisparoenemigo.update()
        listadefinitivaenemigo.update()

        #Comprobar colisiones de disparos

        comprobar=pygame.sprite.spritecollide(yo,listadisparoenemigo, True)
        if comprobar:
            botonvida.vida=botonvida.vida-disparoenemigo.dañoenemigo

        comprobar2=pygame.sprite.spritecollide(enemigoelegido,listadisparo, True)
        if comprobar2:
            enemigoelegido.vida=enemigoelegido.vida-disparo.midaño

        comprobar3=pygame.sprite.spritecollide(enemigoelegido,listadefinitiva, True)
        if comprobar3:
            enemigoelegido.vida=enemigoelegido.vida-definitiva.daño

        comprobar4=pygame.sprite.spritecollide(yo,listadefinitivaenemigo, True)
        if comprobar4:
            botonvida.vida=botonvida.vida-definitivaenemigo.daño

        comprobarbarrera1=pygame.sprite.spritecollide(barrera,listadisparo, True)
        comprobarbarrera2=pygame.sprite.spritecollide(barrera,listadisparoenemigo, True)
        comprobarbarrera3=pygame.sprite.spritecollide(barrera,listadefinitiva, True)
        comprobarbarrera4=pygame.sprite.spritecollide(barrera,listadefinitivaenemigo, True)

        if enemigoelegido.vida<=0: # Si la vida del enemigo es igual o menor a 0 se ejecuta
           reinicioenemigo(enemigoelegido) # Se ejecuta la función reinicioenemigo

        #Enganchar imagenes, textos y dibujamos listas

        pantalla.blit(pantallainicio,[0,0])
        listadisparo.draw(pantalla)
        listadefinitiva.draw(pantalla)
        listadisparoenemigo.draw(pantalla)
        listadefinitivaenemigo.draw(pantalla)
        pantalla.blit(yo.image,yo.rect)
        pantalla.blit(enemigoelegido.image,enemigoelegido.rect)
        pantalla.blit(corazon,[600,270])

        textomivida=fuente1.render(str(botonvida.vida),True,VERMELL)
        textomividasombra=fuente1sombra.render(str(botonvida.vida),True,NEGRE)
        textovidaenemigo1=fuente1.render(str(vidaenemigo),True,VERMELL)
        textovidaenemigo1sombra=fuente1sombra.render(str(vidaenemigo),True,NEGRE)
        textomifuerza=fuente1.render(str(botonfuerza.fuerza),True,BLAU)
        textomifuerzasombra=fuente1sombra.render(str(botonfuerza.fuerza),True,NEGRE)
        textooro=fuente1.render(str(monedas.oro),True,GROC)
        textoorosombra=fuente1sombra.render(str(monedas.oro),True,NEGRE)
        textonivelenemigo=fuente1.render("Nivel: "+str(nivelenemigo.nivelenemigo),True,VERD)
        textonivelenemigosombra=fuente1sombra.render("Nivel: "+str(nivelenemigo.nivelenemigo),True,NEGRE)

        pantalla.blit(textovidaenemigo1sombra,[642,264])
        pantalla.blit(textovidaenemigo1,[640,262])
        pantalla.blit(textonivelenemigosombra,[597,234])
        pantalla.blit(textonivelenemigo,[595,232])
        pantalla.blit(textomividasombra,[117,72])
        pantalla.blit(textomivida,[115,70])
        pantalla.blit(textomifuerzasombra,[135,35])
        pantalla.blit(textomifuerza,[133,33])
        pantalla.blit(cartel,[570,-55])
        pantalla.blit(textoorosombra,[602,52])
        pantalla.blit(textooro,[600,50])
        pantalla.blit(botonvida.curacion,botonvida.rect)
        pantalla.blit(fuerzatexto,[30,30])
        pantalla.blit(curaciontexto,[30,65])
        pantalla.blit(textodefinitiva,[220,450])
        pantalla.blit(botonfuerza.fuerzaimagen,botonfuerza.rect)
        pantalla.blit(barrera.image,barrera.rect)
        cursor.rect.x,cursor.rect.y=pygame.mouse.get_pos()
        pantalla.blit(cursor.image,(cursor.rect.x,cursor.rect.y))
        if botonvida.vida<=0: # Si nuestra vida es igual o inferior a 0 se ejecuta y nos muestra que hemos perdido
            gameover=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\gameover.png")
            pantalla.blit(gameover,[0,0])
        pygame.display.flip() # Actualiza todos los cambios y lo aplica
        rellotge.tick(30) # Limitamos fps del juego
    return enemigoelegido # Devolvemos la variable enemigoelegido

#Menú principal

def menuprincipal(): # Función para el menú principal antes de jugar

    #Cargar imagenes

    BotonPlay.image=pygame.image.load("C:\\Users\\Yeray Lorenzo\\Downloads\\pplay.png")
    BotonPlay.image=pygame.transform.scale(BotonPlay.image,[180,120])
    global CondicionRaton # Hacemos global la CondicionRaton
    CondicionRaton=True # La condiciónraton es True para poder usarla en el bucle
    posXcursor=400 # Posicion x del cursor
    posYcursor=250 # Posiciony y del cursor

    while CondicionRaton: # Mientras CondicionRaton sea True se ejecutará el bucle
        for evento in pygame.event.get(): # Bucle for para los eventos del pygame
            if evento.type==pygame.QUIT: # Si salimos se ejeuta
                CondicionRaton=False # CondicionRaton finaliza
            if evento.type==pygame.MOUSEBUTTONDOWN: # Si apretamos el botón del ratón
                cursor.chocke() # Se ejecuta la función chocke
        # Enganchamos imagenes
        pantalla.blit(pantallainicio,[0,0])
        pantalla.blit(controles,[0,0])
        pantalla.blit(battleboss,rectbattleboss)
        cursor.rect.x,cursor.rect.y=pygame.mouse.get_pos() # Hacemos que las posiciones del objeto cursor sean las del pygame.mouse.get_pos()
        pantalla.blit(BotonPlay.image,BotonPlay.rect)
        pantalla.blit(cursor.image,(cursor.rect.x-35,cursor.rect.y-35)) # Enganchamos la imagen restandole 35 porque queremos que la imagen esté en medio
        pygame.display.flip()
    pygame.quit()

menuprincipal() # Iniciamos menuprincipal
