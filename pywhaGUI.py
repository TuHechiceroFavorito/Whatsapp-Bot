from selenium import webdriver as wd
from time import sleep

import tkinter as tk
from tkinter import *

class PutoBotTocaCojones:
    def __init__(self):
        self.driver=wd.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        self.nombreS="Busca"

        #buscar=self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]')

    def buscar(self,nombre):
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click()      #Click busqueda chat
                break

            except:
                print("Escanea el puto código me cago en dios")
                sleep(1)
        while True:
            try:
                
                #Borramos la entrada por si hubiera texto de busquedas anteriores
                self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').clear()

                #Buscamos el contacto especificado por el usuario
                self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(nombre)

                #Guardamos el nomnre en la variable nombreS para seleccionar el chat correcto
                self.nombreS=nombre
                sleep(0.5)
                break
            
            except:
                print("Esperando a que cargue la página")
                sleep(0.5)
                break


    def seleccionar(self):
        try:
            self.driver.find_element_by_xpath('//*[@title="'+self.nombreS+'"]').click()    #Click en chat
        except:
            print("Error buscando el elemento.")


    def enviar(self,mensaje,n):
        putosmensajesenviados=0

        while True:
            if(putosmensajesenviados==n):
                break
            while True:
                try:
                    self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(mensaje)    #Mensaje escrito en caja de texto del chat
                    break
                except:
                    print("Esperando a que cargue la página")
                    sleep(0.5)
            while True:
                try:
                    self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                    print("HECHO")
                    putosmensajesenviados+=1
                    break
                except:
                    print("Esperando a que cargue la página")
                    sleep(0.5)

    def borrar(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').clear()
        except:
            print("Error buscando el elemento")
    
    def salir(self):
        print("Cerrando ventana")
        self.driver.quit()
        print("Ventana cerrada")

bot=0

def iniciar():
    global bot
    bot=PutoBotTocaCojones()

def buscar(nombre):
    global bot
    bot.buscar(nombre)

def seleccionar():
    global bot
    bot.seleccionar()

def enviar(mensaje,numero):
    global bot
    numero=int(numero)
    bot.enviar(mensaje,numero)

def salir():
    global bot
    bot.salir()


screen = tk.Tk()

canvas=tk.Canvas(screen, height=600, width=600, bg="#FF6B21")
canvas.pack()

#frame=tk.Frame(screen,bg="white")
#frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

iniciar=tk.Button(canvas, text="Iniciar bot", bg="green", command=iniciar)
iniciar.place(relheight=0.05, relwidth=0.3,relx=0.35,rely=0.2)

entrada=Entry(canvas,bd=5)
entrada.place(relheight=0.05, relwidth=0.3,relx=0.35,rely=0.35)

#texto=Text(screen)
#texto.place(relheight=0.05, relwidth=0.3,relx=0.35,rely=0.35)

botonBuscar=tk.Button(canvas, text="Buscar contacto", bg="green", command=lambda: buscar(entrada.get()))
botonBuscar.place(relheight=0.05, relwidth=0.3,relx=0.2,rely=0.4)

seleccionar=tk.Button(canvas, text="Seleccionar contacto", bg="green", command=seleccionar)
seleccionar.place(relheight=0.05, relwidth=0.3,relx=0.5,rely=0.4)


mensaje=Entry(canvas,bd=5)
mensaje.place(relheight=0.05, relwidth=0.3,relx=0.35,rely=0.5)

numero=Entry(canvas,bd=5)
numero.place(relheight=0.05, relwidth=0.05,relx=0.6,rely=0.5)

botonEnviar=tk.Button(canvas, text="Enviar mensaje", bg="green",command=lambda: enviar(mensaje.get(),numero.get()))
botonEnviar.place(relheight=0.05, relwidth=0.3,relx=0.35,rely=0.55)

botonSalir=tk.Button(canvas,text="Cerrar bot", bg="green", command=salir)
botonSalir.place(relheight=0.05, relwidth=0.3,relx=0.35,rely=0.9)

#texto=Text(screen)
#texto.pack()

screen.mainloop()
"""
while True:
    g=texto.get()
    print(g)"""