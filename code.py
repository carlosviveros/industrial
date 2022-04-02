from datetime import datetime
from datetime import date


def menu():
     fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
     turno1 = int(input("ingrese turno"))
     horaIncial = int(input("ingrese hora inicial"))
     horaFinal = int(input("ingrese fecha final"))
     jefe_turno=input("ingrese el jefe de turno")
     maquinaria=input("ingrese la maquinaria a emplear")

def validarDate(date):
    while True:
        try:
            date = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
            datetime.strptime(date, '%Y-%m-%d')
            print("Fecha válida")
            return date
        except ValueError:
            print("Fecha inválida")
   


def validarhora(h):
       while True:
        try:
            date = input("Ingresa hora en el formato HH:MM : ")
            datetime.strptime(h, "%H:%M")
            print("Hora válida")
            return h
        except ValueError:
              print("Hora inválida")
    
       
    
def main():
    menu()
    
    
    
       
        