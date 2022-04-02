from datetime import datetime
from datetime import date

def capturarNumero():
    while True:
        try:
            number = float(input("Inserte el valor"))
            return number
        except Exception:
            print("volver a intentar")