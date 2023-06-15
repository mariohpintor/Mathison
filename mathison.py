import pygame
import sys
import random
import time

#Iniciar ventana
pygame.init()
pygame.display.set_caption("MATHISON")
screen = pygame.display.set_mode((800, 900))
#Fuentes
main_font = pygame.font.SysFont("arial", 80)
sub_font = pygame.font.SysFont("arial", 50)

#Nivel de multiplicación
fuente = pygame.font.SysFont("arial", 50)
res =[None for _ in range(4)]
palomita = pygame.image.load("paloma.png")
palomita = pygame.transform.scale(palomita, (150, 150))
equis = pygame.image.load("error.png")
equis = pygame.transform.scale(equis, (150, 150))
estrellita = pygame.image.load("estrellita.png")
estrellita = pygame.transform.scale(estrellita, (90, 90))
contador = [0,0]
#parametros de class cuadricula_res
posx = 150
posy = 400
deltax = 300
deltay = 200
sizerect = (150,150)
color_rects = (100, 30, 22 )
#------------
tiempo = 1
color_fondo = (21, 67, 96)
color_letras = (166, 172, 175)

primos = [2,3,5,7,11,13,17]

class Boton():
    def __init__(self, x_pos, y_pos, text_input, alto, largo):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.largo = largo
        self.alto = alto
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect =  self.text.get_rect(center=(self.x_pos,self.y_pos))

    def update(self):
        pygame.draw.rect(screen, color_rects,(self.x_pos-int(self.largo/2) ,self.y_pos-int(self.alto/2),self.largo,self.alto))
        screen.blit(self.text, self.text_rect)
        

    def checkForInput(self, position,funcion):
        if position[0] in range(self.x_pos-int(self.largo/2),self.x_pos+ int(self.largo/2)) and position[1] in range(self.y_pos-int(self.alto/2),self.y_pos + int(self.alto/2)):
            funcion()

    def changeColor(self, position):
        if position[0] in range(self.x_pos-int(self.largo/2),self.x_pos+ int(self.largo/2)) and position[1] in range(self.y_pos-int(self.alto/2),self.y_pos + int(self.alto/2)):
            self.text = main_font.render(self.text_input, True, "red")
        else:
            self.text = main_font.render(self.text_input, True, "white")

def menu():
    miTexto = main_font.render("MATHISON", 0, color_letras)
    subtitulo = sub_font.render("[Un juego de ecuaciones]", 0, color_letras)
    button1 = Boton(400, 300, "Iniciar",120,280)
    miTexto_rect = miTexto.get_rect(center=(400,100))
    subtitulo_rect = subtitulo.get_rect(center=(400,200))

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(300-int(120/2), 300 + int(120/2)):
                    mapa_niveles1()    

        screen.fill(color_fondo)
        screen.blit(miTexto,miTexto_rect)
        screen.blit(subtitulo,subtitulo_rect)
        button1.update()
        button1.changeColor(pygame.mouse.get_pos())

        pygame.display.flip()

def mapa_niveles1():
    miTexto = main_font.render("Niveles", 0, color_letras)
    button1 = Boton(400, 250, "Suma",120,280)
    button2 = Boton(400, 400, "Resta",120,280)
    button3 = Boton(400, 550, "Producto",120,380)
    button4 = Boton(400, 700, "Más niveles",120,500)
    miTexto_rect = miTexto.get_rect(center=(400,100))

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(250-int(120/2), 220 + int(120/2)):
                    nivel_1()
                elif position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(400-int(120/2), 400 + int(120/2)):
                    nivel_2()    
                elif position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(550-int(120/2), 550 + int(120/2)):
                    nivel_3()      
                elif position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(700-int(120/2), 700 + int(120/2)):
                    mapa_niveles2()                          

        screen.fill(color_fondo)
        screen.blit(miTexto,miTexto_rect)
        button1.update()
        button1.changeColor(pygame.mouse.get_pos())
        button2.update()
        button2.changeColor(pygame.mouse.get_pos())
        button3.update()
        button3.changeColor(pygame.mouse.get_pos())
        button4.update()
        button4.changeColor(pygame.mouse.get_pos())

        pygame.display.flip()

def mapa_niveles2():
    button1 = Boton(400, 300, "División",120,350)
    button2 = Boton(400, 500, "Potencias",120,600)
    button3 = Boton(400, 700, "Dos ecuaciones",120,600)

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(300-int(120/2), 300 + int(120/2)):
                    nivel_4()
                elif position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(500-int(120/2), 500 + int(120/2)):
                    nivel_6()
                elif position[0] in range(400-int(280/2),400+ int(280/2)) and position[1] in range(700-int(120/2), 700 + int(120/2)):
                    nivel_5()    
                

        screen.fill(color_fondo)
        button1.update()
        button1.changeColor(pygame.mouse.get_pos())
        button2.update()
        button2.changeColor(pygame.mouse.get_pos())
        button3.update()
        button3.changeColor(pygame.mouse.get_pos())
        pygame.display.flip()

class cuadricula_res():
    def __init__(self, posx,posy,respuestas):
        self.posx = posx
        self.posy = posy
        self.respuestas = respuestas 

    def dibujar(self):
        pygame.draw.rect(screen, color_rects,(self.posx,self.posy,sizerect[0],sizerect[1]))
        respuesta1 = main_font.render(str(self.respuestas[0]), 0, color_letras)
        screen.blit(respuesta1,(self.posx + 30,self.posy + 20))

        pygame.draw.rect(screen, color_rects,(self.posx+deltax,self.posy,sizerect[0],sizerect[1]))
        respuesta2 = main_font.render(str(self.respuestas[1]), 0, color_letras)
        screen.blit(respuesta2,(self.posx+deltax+ 30,self.posy + 20))

        pygame.draw.rect(screen, color_rects,(self.posx,self.posy+deltay,sizerect[0],sizerect[1]))
        respuesta3 = main_font.render(str(res[2]), 0, color_letras)
        screen.blit(respuesta3,(self.posx + 30,self.posy+deltay+ 20))

        pygame.draw.rect(screen, color_rects,(self.posx+deltax,self.posy+deltay,sizerect[0],sizerect[1]))
        respuesta4 = main_font.render(str(res[3]), 0, color_letras)
        screen.blit(respuesta4,(self.posx+deltax + 30,self.posy+deltay + 20))
   
def gen_ecuaciones(res,opcion):
    #Generación de ecuaciones
    a = random.randint(2,20)
    if opcion == 0:
       b = a + random.randint(2,20)
       res[0] = b - a  
    elif opcion == 1:
        b = a - random.randint(2,20)
        res[0] = a - b
    elif opcion == 2:
        b = a * random.randint(2,20)
        res[0] = int(b/a)
    elif opcion == 3:
        b = random.choice(primos)
        res[0] = random.choice(primos)
        a = b*res[0]
    elif opcion == 4:
        b = random.randint(2,10)
        res[0] = a                       

    res[1] = res[0]+random.randint(1,3)
    res[2] = res[0]+random.randint(4,6)
    res[3] = res[0]+random.randint(7,9)
    for i in range(4):
        indice_aleatorio = random.randint(0, 3)
        temporal = res[i]
        res[i] = res[indice_aleatorio]
        res[indice_aleatorio] = temporal
    return a,b  

def revisar(respuesta,res_correcta, posx,posy):
    if respuesta == res_correcta:
        screen.blit(palomita,(posx,posy))
        contador[0]+=1
    else:
        screen.blit(equis,(posx,posy))
        contador[1]+=1

#suma
def nivel_1():
    contador[0]=contador[1]=0
    temporizador = 90
    a,b = gen_ecuaciones(res,0)
    res_correcta = b - a
    cuadricula= cuadricula_res(posx,posy,res)
    tiempo = int(pygame.time.get_ticks()/1000)
    aux = tiempo

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()


                if position[0] in range(posx,posx+sizerect[0]) and position[1] in range(posy,posy+sizerect[1]):
                    #Se puede unir estas funciones
                    revisar(res[0], res_correcta,posx,posy)
                    a,b= gen_ecuaciones(res,0)

                elif position[0] in range(posx + deltax,posx+ deltax+sizerect[0]) and position[1] in range(posy,posy + sizerect[1]):
                    revisar(res[1], res_correcta,posx + deltax,posy)
                    a,b= gen_ecuaciones(res,0)

                elif position[0] in range(posx,posx + sizerect[0]) and position[1] in range(posy+deltay,posy+deltay + sizerect[1]):
                    revisar(res[2], res_correcta,posx,posy+deltay)
                    a,b= gen_ecuaciones(res,0)

                elif position[0] in range(posx + deltax,posx + deltax+sizerect[0]) and position[1] in range(posy+ deltay,posy+ deltay + sizerect[1]):
                    revisar(res[3], res_correcta,posx + deltax,posy+ deltay)
                    a,b= gen_ecuaciones(res,0)

                res_correcta = b - a 
                pygame.display.flip()
                time.sleep(0.5)
                
                    

        screen.fill(color_fondo)
        screen.blit(estrellita,(500,20))
        screen.blit(estrellita,(600,20))
        screen.blit(estrellita,(700,20))

        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(800 - contador[1]*100,20, contador[1]*100,90))                
        
        reloj = main_font.render(str(temporizador)+"seg", 0, color_letras)
        screen.blit(reloj,(20,20))

        tiempo = int(pygame.time.get_ticks()/1000)
        if aux == tiempo:
            aux+=1
            temporizador-=1


        ecuacion = main_font.render(str(a)+" + "+" ? "+" = "+str(b), 0, color_letras)
        screen.blit(ecuacion,(120,150))

        cuadricula.dibujar()

        if temporizador < 0 or contador[1] == 3:
            termina_nivel()

        pygame.display.flip()

#resta
def nivel_2():
    contador[0]=contador[1]=0
    temporizador = 90
    a,b = gen_ecuaciones(res,1)
    res_correcta = a - b
    cuadricula= cuadricula_res(posx,posy,res)
    tiempo = int(pygame.time.get_ticks()/1000)
    aux = tiempo

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()


                if position[0] in range(posx,posx+sizerect[0]) and position[1] in range(posy,posy+sizerect[1]):
                    #Se puede unir estas funciones
                    revisar(res[0], res_correcta,posx,posy)
                    a,b= gen_ecuaciones(res,1)

                elif position[0] in range(posx + deltax,posx+ deltax+sizerect[0]) and position[1] in range(posy,posy + sizerect[1]):
                    revisar(res[1], res_correcta,posx + deltax,posy)
                    a,b= gen_ecuaciones(res,1)

                elif position[0] in range(posx,posx + sizerect[0]) and position[1] in range(posy+deltay,posy+deltay + sizerect[1]):
                    revisar(res[2], res_correcta,posx,posy+deltay)
                    a,b= gen_ecuaciones(res,1)

                elif position[0] in range(posx + deltax,posx + deltax+sizerect[0]) and position[1] in range(posy+ deltay,posy+ deltay + sizerect[1]):
                    revisar(res[3], res_correcta,posx + deltax,posy+ deltay)
                    a,b= gen_ecuaciones(res,1)

                res_correcta = a - b 
                pygame.display.flip()
                time.sleep(0.5)
                
                    

        screen.fill(color_fondo)
        screen.blit(estrellita,(500,20))
        screen.blit(estrellita,(600,20))
        screen.blit(estrellita,(700,20))

        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(800 - contador[1]*100,20, contador[1]*100,90))                
        
        reloj = main_font.render(str(temporizador)+"seg", 0, color_letras)
        screen.blit(reloj,(20,20))

        tiempo = int(pygame.time.get_ticks()/1000)
        if aux == tiempo:
            aux+=1
            temporizador-=1


        ecuacion = main_font.render(str(a)+" - "+" ? "+" = "+str(b), 0, color_letras)
        screen.blit(ecuacion,(120,150))

        cuadricula.dibujar()

        if temporizador < 0 or contador[1] == 3:
            termina_nivel()

        pygame.display.flip()         

#multiplicación
def nivel_3():
    contador[0]=contador[1]=0
    temporizador = 90
    a,b = gen_ecuaciones(res,2)
    res_correcta = int(b/a)
    cuadricula= cuadricula_res(posx,posy,res)
    tiempo = int(pygame.time.get_ticks()/1000)
    aux = tiempo

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()


                if position[0] in range(posx,posx+sizerect[0]) and position[1] in range(posy,posy+sizerect[1]):
                    #Se puede unir estas funciones
                    revisar(res[0], res_correcta,posx,posy)
                    a,b= gen_ecuaciones(res,2)

                elif position[0] in range(posx + deltax,posx+ deltax+sizerect[0]) and position[1] in range(posy,posy + sizerect[1]):
                    revisar(res[1], res_correcta,posx + deltax,posy)
                    a,b= gen_ecuaciones(res,2)

                elif position[0] in range(posx,posx + sizerect[0]) and position[1] in range(posy+deltay,posy+deltay + sizerect[1]):
                    revisar(res[2], res_correcta,posx,posy+deltay)
                    a,b= gen_ecuaciones(res,2)

                elif position[0] in range(posx + deltax,posx + deltax+sizerect[0]) and position[1] in range(posy+ deltay,posy+ deltay + sizerect[1]):
                    revisar(res[3], res_correcta,posx + deltax,posy+ deltay)
                    a,b= gen_ecuaciones(res,2)

                res_correcta = int(b/a) 
                pygame.display.flip()
                time.sleep(0.5)
                
                    

        screen.fill(color_fondo)
        screen.blit(estrellita,(500,20))
        screen.blit(estrellita,(600,20))
        screen.blit(estrellita,(700,20))
        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(800 - contador[1]*100,20, contador[1]*100,90))                
        
        reloj = main_font.render(str(temporizador)+"seg", 0, color_letras)
        screen.blit(reloj,(20,20))

        tiempo = int(pygame.time.get_ticks()/1000)
        if aux == tiempo:
            aux+=1
            temporizador-=1


        ecuacion = main_font.render(str(a)+" x "+" ? "+" = "+str(b), 0, color_letras)
        screen.blit(ecuacion,(120,150))

        cuadricula.dibujar()

        if temporizador < 0 or contador[1] == 3:
            termina_nivel()

        pygame.display.flip()

#division
def nivel_4():
    contador[0]=contador[1]=0
    temporizador = 90
    a,b = gen_ecuaciones(res,3)
    res_correcta = a//b
    cuadricula= cuadricula_res(posx,posy,res)
    tiempo = int(pygame.time.get_ticks()/1000)
    aux = tiempo

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()


                if position[0] in range(posx,posx+sizerect[0]) and position[1] in range(posy,posy+sizerect[1]):
                    #Se puede unir estas funciones
                    revisar(res[0], res_correcta,posx,posy)
                    a,b= gen_ecuaciones(res,3)

                elif position[0] in range(posx + deltax,posx+ deltax+sizerect[0]) and position[1] in range(posy,posy + sizerect[1]):
                    revisar(res[1], res_correcta,posx + deltax,posy)
                    a,b= gen_ecuaciones(res,3)

                elif position[0] in range(posx,posx + sizerect[0]) and position[1] in range(posy+deltay,posy+deltay + sizerect[1]):
                    revisar(res[2], res_correcta,posx,posy+deltay)
                    a,b= gen_ecuaciones(res,3)

                elif position[0] in range(posx + deltax,posx + deltax+sizerect[0]) and position[1] in range(posy+ deltay,posy+ deltay + sizerect[1]):
                    revisar(res[3], res_correcta,posx + deltax,posy+ deltay)
                    a,b= gen_ecuaciones(res,3)

                res_correcta = a//b 
                pygame.display.flip()
                time.sleep(0.5)
                
                    

        screen.fill(color_fondo)
        screen.blit(estrellita,(500,20))
        screen.blit(estrellita,(600,20))
        screen.blit(estrellita,(700,20))
        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(800 - contador[1]*100,20, contador[1]*100,90))                
        
        reloj = main_font.render(str(temporizador)+"seg", 0, color_letras)
        screen.blit(reloj,(20,20))

        tiempo = int(pygame.time.get_ticks()/1000)
        if aux == tiempo:
            aux+=1
            temporizador-=1


        ecuacion = main_font.render(str(a)+" / "+" ? "+" = "+str(b), 0, color_letras)
        screen.blit(ecuacion,(120,150))

        cuadricula.dibujar()

        if temporizador < 0 or contador[1] == 3:
            termina_nivel()

        pygame.display.flip()

def gen_vec(vector1,vector2):
    vector1 = [random.randint(2,15),random.randint(2,15),random.randint(2,15)]
    vector2 = [random.randint(2,15),random.randint(2,15),random.randint(2,15)]

#resolver el sistema de ecuaciones
def res_sis(vector1,vector2,vector_res):
    det = vector1[0]*vector2[1] - vector1[1]*vector2[0]
    if det != 0:
        vector_res[0] =vector1[2]*vector2[1] - vector1[1]*vector2[2]
        vector_res[1] =vector1[0]*vector2[2] - vector1[0]*vector2[1]
        vector_res[2] = det
        #hay una única solución
        respuesta = 0 
    else:
        if vector2[2] > vector1[2]:
            if vector2[2]%vector1[2]==0:
                respuesta = 1
                #son la misma recta y hay infinitas soluciones
            else:
                respuesta = 2
                #son rectas paralelas y no hay soluciones    
        else:   
            if vector1[2]%vector2[2]==0:
                respuesta = 1
                #son la misma recta y hay infinitas soluciones
            else:
                respuesta = 2
                #son rectas paralelas y no hay soluciones 
    return respuesta             

#potencias
def nivel_6():
    contador[0]=contador[1]=0
    temporizador = 90
    a,b = gen_ecuaciones(res,4)
    res_correcta = a
    cuadricula= cuadricula_res(posx,posy,res)
    tiempo = int(pygame.time.get_ticks()/1000)
    aux = tiempo

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()


                if position[0] in range(posx,posx+sizerect[0]) and position[1] in range(posy,posy+sizerect[1]):
                    #Se puede unir estas funciones
                    revisar(res[0], res_correcta,posx,posy)
                    a,b= gen_ecuaciones(res,4)

                elif position[0] in range(posx + deltax,posx+ deltax+sizerect[0]) and position[1] in range(posy,posy + sizerect[1]):
                    revisar(res[1], res_correcta,posx + deltax,posy)
                    a,b= gen_ecuaciones(res,4)

                elif position[0] in range(posx,posx + sizerect[0]) and position[1] in range(posy+deltay,posy+deltay + sizerect[1]):
                    revisar(res[2], res_correcta,posx,posy+deltay)
                    a,b= gen_ecuaciones(res,4)

                elif position[0] in range(posx + deltax,posx + deltax+sizerect[0]) and position[1] in range(posy+ deltay,posy+ deltay + sizerect[1]):
                    revisar(res[3], res_correcta,posx + deltax,posy+ deltay)
                    a,b= gen_ecuaciones(res,4)

                res_correcta = b - a 
                pygame.display.flip()
                time.sleep(0.5)
                
                    

        screen.fill(color_fondo)
        screen.blit(estrellita,(500,20))
        screen.blit(estrellita,(600,20))
        screen.blit(estrellita,(700,20))

        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(800 - contador[1]*100,20, contador[1]*100,90))                
        
        reloj = main_font.render(str(temporizador)+"seg", 0, color_letras)
        screen.blit(reloj,(20,20))

        tiempo = int(pygame.time.get_ticks()/1000)
        if aux == tiempo:
            aux+=1
            temporizador-=1


        ecuacion = main_font.render("x^"+str(b)+"= "+str(a**b), 0, color_letras)
        screen.blit(ecuacion,(120,150))

        cuadricula.dibujar()

        if temporizador < 0 or contador[1] == 3:
            termina_nivel()

        pygame.display.flip()

#coeficientes fraccionales

#sistema de ecuaciones
def nivel_5():
    contador[0]=contador[1]=0
    temporizador = 180
    tiempo = int(pygame.time.get_ticks()/1000)
    aux = tiempo
    vector1 = [random.randint(2,15),random.randint(2,15),random.randint(2,15)]
    vector2 = [random.randint(2,15),random.randint(2,15),random.randint(2,15)]
    vector_res=[0,0,0] 
    respuesta = res_sis(vector1,vector2,vector_res)
    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()

                if position[0] in range(120,120+550) and position[1] in range(400,400+80):
                    #Se puede unir estas funciones
                    revisar(2,respuesta,120,400)
                    
                elif position[0] in range(120,120+550) and position[1] in range(500,500 + 80):
                    revisar(1,respuesta,120,500)

                elif position[0] in range(120,120 + 550) and position[1] in range(600,600+ 80):
                    revisar(0,respuesta,120,600)

                elif position[0] in range(120 ,120 +550) and position[1] in range(700,700+ 80):
                    revisar(3,respuesta,120,700)
                
                gen_vec(vector1,vector2)
                respuesta = res_sis(vector1,vector2,vector_res)
                pygame.display.flip()
                time.sleep(0.5)
                
                    

        screen.fill(color_fondo)
        screen.blit(estrellita,(500,20))
        screen.blit(estrellita,(600,20))
        screen.blit(estrellita,(700,20))
        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(800 - contador[1]*100,20, contador[1]*100,90))                
        
        reloj = main_font.render(str(temporizador)+"seg", 0, color_letras)
        screen.blit(reloj,(20,20))

        tiempo = int(pygame.time.get_ticks()/1000)
        if aux == tiempo:
            aux+=1
            temporizador-=1


        ecuacion1 = main_font.render(str(vector1[0]) + "x" + " + " + str(vector1[1]) + "y = " + str(vector1[2]), 0, color_letras)
        ecuacion2 = main_font.render(str(vector2[0]) + "x" + " + " + str(vector2[1]) + "y = " + str(vector2[2]), 0, color_letras)

        screen.blit(ecuacion1,(120,150))
        screen.blit(ecuacion2,(120,250))
        #cuadritos de respuestas

        pygame.draw.rect(screen, color_rects,(120 ,400,550,80))
        respuesta1 = sub_font.render("No hay solución", 0, color_letras)
        screen.blit(respuesta1,(125 ,400))

        pygame.draw.rect(screen, color_rects,(120,600,550,80))
        respuesta2 = sub_font.render("x="+str(vector_res[0])+"/"+ str(vector_res[2])+", "+"y="+ str(vector_res[1])+"/"+ str(vector_res[2]), 0, color_letras)
        screen.blit(respuesta2,(125,600))

        pygame.draw.rect(screen, color_rects,(120, 500,550,80))
        respuesta3 = sub_font.render("Hay soluciones infinitas", 0, color_letras)
        screen.blit(respuesta3,(125, 500))

        pygame.draw.rect(screen, color_rects,(120,700,550,80))
        respuesta4 = sub_font.render("x="+str(vector_res[0]+1)+"/"+ str(vector_res[2]+1)+", "+"y="+ str(vector_res[1]+1)+"/"+ str(vector_res[2]+1), 0, color_letras)
        screen.blit(respuesta4,(125,700))

        if temporizador < 0 or contador[1] == 3:
            termina_nivel()

        pygame.display.flip()

def termina_nivel():
    button = Boton(400,700, "Regresar",130,350)
    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.checkForInput(pygame.mouse.get_pos(),menu())
        
        screen.fill(color_fondo)
        correctas = fuente.render("Aciertos: " + str(contador[0]) , 0, color_letras)
        screen.blit(correctas,(10,300))

        screen.blit(estrellita,(10,400))
        screen.blit(estrellita,(110,400))
        screen.blit(estrellita,(210,400))
        if contador[1] > 0:
            pygame.draw.rect(screen, color_fondo,(310 - contador[1]*100,400, contador[1]*100,90))
            if contador[1] == 1 or contador[1] == 2:
                gameover = fuente.render("¡Lo puedes hacer mejor!" , 0, color_letras)
            else:
                gameover = fuente.render("¡Estás un poco distraído!" , 0, color_letras) 
        else:
            gameover = fuente.render("¡Bien hecho!" , 0, color_letras)
                                
        screen.blit(gameover,(10,100))
        button.update()
        button.changeColor(pygame.mouse.get_pos())
        pygame.display.flip()       

if __name__ =='__main__':
    menu()