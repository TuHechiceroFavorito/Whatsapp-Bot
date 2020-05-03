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
    salida['text']="Iniciando bot"
    global bot
    bot=PutoBotTocaCojones()
    salida['text']="Bot iniciado"

def buscar(nombre):
    salida['text']="Buscando a %s" %(nombre)
    global bot
    bot.buscar(nombre)

def seleccionar():
    global bot
    bot.seleccionar()
    salida['text']="Contacto seleccionado"

def enviar(mensaje,numero):
    global bot
    numero=int(numero)
    bot.enviar(mensaje,numero)
    salida['text']='"%s" enviado %i veces' %(mensaje, numero)

def salir():
    global bot
    bot.salir()
    salida['text']="Bot cerrado"


screen = tk.Tk()

screen.title("Bot Whatsapp")

screen.iconbitmap("bot.ico")

fondo=PhotoImage(file="bot.png")

canvas=tk.Canvas(screen, height=550, width=700, bg="#FF6B21")
canvas.pack()
#canvas.place(relwidth=1,relheight=1)

back=Label(canvas, image=fondo)
back.place(relwidth=1, relheight=1)

frame1=tk.Frame(canvas, bd=5,bg="#35CCD1")
frame1.place(relx=0.5,rely=0.025, relheight=0.05, relwidth=0.2, anchor='n')

frame2=tk.Frame(canvas, bd=3,bg="#35CCD1")
frame2.place(relx=0.5,rely=0.1, relheight=0.05, relwidth=0.8, anchor='n')

iniciar=tk.Button(frame1, text="Iniciar bot", bg="green", command=iniciar)
iniciar.place(relheight=1, relwidth=1)

contacto=Label(frame2, text="Contacto:", bg="white")
contacto.place(relwidth=0.2, relheight=1)

entrada=Entry(frame2,bd=5)
entrada.place(relheight=1, relwidth=0.6, relx=0.2)

botonBuscar=tk.Button(frame2, text="Buscar contacto", bg="green", command=lambda: buscar(entrada.get()))
botonBuscar.place(relheight=1, relwidth=0.2,relx=0.8)

frame3=tk.Frame(canvas, bd=3, bg="#35CCD1")
frame3.place(relx=0.5,rely=0.2, relheight=0.05, relwidth=0.2, anchor='n')

seleccionar=tk.Button(frame3, text="Seleccionar contacto", bg="green", command=seleccionar)
seleccionar.place(relheight=1, relwidth=1)

frame4=tk.Frame(canvas,bd=5, bg="#35CCD1")
frame4.place(relx=0.5,rely=0.3, relheight=0.2, relwidth=0.8, anchor='n')

text1=Label(frame4,bg="White", text="Mensaje:")
text1.place(relwidth=0.15, relheight=0.25)

mensaje=Entry(frame4,bd=5)
mensaje.place(relheight=0.25, relwidth=0.85, relx=0.15)

text2=tk.Label(frame4,text="Número de mensajes:")
text2.place(relwidth=0.27, relheight=0.25, rely=0.3)

numero=Entry(frame4,bd=5)
numero.place(relheight=0.25, relwidth=0.73,relx=0.27,rely=0.3)

botonEnviar=tk.Button(frame4, text="Enviar mensaje", bg="green",command=lambda: enviar(mensaje.get(),numero.get()))
botonEnviar.place(relheight=0.25, relwidth=0.25,relx=0.375,rely=0.65)

frame5=Frame(canvas,bd=5, bg="#35CCD1")
frame5.place(relx=0.5,rely=0.6, relheight=0.2, relwidth=0.8, anchor='n')

salida=Label(frame5,bd=5, font=("Modern",18),text="Bienvenido al bot tocacojones de Whatsapp. \n Disfrute de su uso poco responsable")
salida.place(relheight=1,relwidth=1)

frame6=Frame(canvas,bd=5, bg="#35CCD1")
frame6.place(relx=0.5,rely=0.85, relheight=0.05, relwidth=0.2, anchor='n')

botonSalir=tk.Button(frame6,text="Cerrar bot", bg="green", command=salir)
botonSalir.place(relheight=1, relwidth=1)

screen.mainloop()
