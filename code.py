from datetime import datetime
from datetime import date
import json


def formulario():
    for iteracion in range(3):
        iteracion+=1
        fecha = validarDate()
        print("ingrese turno")
        turno1 = capturarNumero()
        print("Ingresa la hora inicial")
        horaIncial = validarhora()
        print("Ingresa la hora final")
        horaFinal = validarhora()
        jefe_turno = input("ingrese el jefe de turno: ")
        print()
        print("Maquinaria #", iteracion)
        maquinaria = input("ingrese la maquinaria a emplear: ")

        resumen = []

        desperdicio = ["preforma", "envase"]
        datos = {
            "produccion": 0,
            "desperdicio": [],
            "conforme": 0
        }
        for i in desperdicio:
            print("Desperdicio "+i+":")
            x = capturarNumero()
            datos["desperdicio"].append(x)
        print("Producción total:")
        x = capturarNumero()
        datos["produccion"] = x
        datos["conforme"] = datos["produccion"] - sum(datos["desperdicio"])
        resumen.append(datos)
    print()
    print(
        "fecha:",
        fecha,
        "- Hora inicial:",
        horaIncial,
        "- Hora Final:",
        horaFinal,
        "- Jefe de turno:",
        jefe_turno,
        "- Maquinaria Usada:",
        maquinaria
    )
    print()
    neta = 0
    for e in resumen:
        print("Maquina", iteracion)
        print("Despercicio preforma:", e["desperdicio"][0])
        print("Despercicio envase:", e["desperdicio"][1])
        print("Producción Total:", e["produccion"])
        print("Producción Conforme:", e["conforme"])
        neta += e["conforme"]
        print()
    print("Produccion neta: ", neta)


def capturarNumero():
    while True:
        try:
            number = int(input("Ingrese un valor: "))
            return number
        except Exception as e:
            print("valor erroneo")


def validarDate():
    while True:
        try:
            date = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Fecha inválida")


def validarhora():
    while True:
        try:
            h = input("HH:MM : ")
            datetime.strptime(h, "%H:%M")
            return h
        except ValueError:
            print("Hora inválida")


def main():
    formulario()


main()
