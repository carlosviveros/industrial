import datetime
from dataclasses import dataclass, field
from tkinter import (
    Button,
    Canvas,
    Entry,
    Frame,
    Label,
    Scrollbar,
    Text,
    Toplevel,
    Tk,
    ttk
)

#Como su nombre lo indica, el método _today_date retorna la fecha de hoy
def _today_date():
    return datetime.date.today().strftime("%d/%m/%Y")


#Con el decorador "Dataclass" se pretende facilitar la creación de clases. 
@dataclass
class Formulario:
    #Se definen los atributos de la clase con sus correspondientes tipos de datos:
    fecha: str
    turno: int
    #Field describe el cada campo definido
    hora_inicial: str = field(default="00:00")
    hora_final: str = field(default="00:00")
    jefe_turno: str = ""
    maquinaria: str = ""
    preforma: str = ""
    envase: str = ""
    produccion_total: str = ""
    #Total_desperidicio y producción conforme tomarán un valor booleano que en este caso será falso
    total_desperdicio: str = field(init=False)
    produccion_conforme: str = field(init=False)
#Con el método post_init se inicalizan variables que dependerán de uno o más campos 
    def __post_init__(self):
        #en caso de no haber un valor en "desperdicio" y  "conforme", el total desperidicio y producción conforme tendrán por defecto un 0 que tra
        
        try:
            desperdicio = float(self.preforma) + float(self.envase)
            conforme = float(self.produccion_total) - desperdicio
            self.total_desperdicio = str(desperdicio)
            self.produccion_conforme = str(conforme)
        except ValueError:
            self.total_desperdicio = "0" 
            self.produccion_conforme = "0"
#El método str como su nombre lo indica devolverá en String (cadena de texto), los datos de la clase para luego "mostrarlos" en donde se deseen poner
    def to_str(self):
        return (
            f"Fecha: {self.fecha}\n"
            f"Turno: {self.turno}\n"
            f"Hora inicial: {self.hora_inicial}\n"
            f"Hora final: {self.hora_final}\n"
            f"Jefe turno: {self.jefe_turno}\n"
            f"Maquinaria: {self.maquinaria}\n"
            f"Preforma: {self.preforma}\n"
            f"Envase: {self.envase}\n"
            f"Producción total: {self.produccion_total}\n"
            f"Total desperdicio: {self.total_desperdicio}\n"
            f"Producción conforme: {self.produccion_conforme}\n"
        )

#La clase widget hereda la clase frame
class Widget(Frame):
     #el método init de la clase widget tendrá dos atributos: master y turno
    def __init__(self, master, turno):
        #Para acceder a los elementos(métodos y atributos) de la clase padre frame se hará uso del método super(Herencia):
        super().__init__(master)
        self.turno = turno
        self.setup_ui()
        #Se recorre cada widget para agregar un "espaciado" de en 5  "x" y 5 en "y"  
        for widget in self.winfo_children():
            widget.grid_configure(padx=5, pady=5)
        #En este método se crean todos los widgets que se utilizarán,es decir, tanto labels como entradas de texto. Y de igual forma, se establecerá la  posición de acuerdo al grid 
        # de la ventanas (celdas)
        #Apreciaciones:
        #columnspan:2  Indica la posición del widget en  dos columnas
        #sticky: expandir el widget. "e" indica la posición este
    def setup_ui(self):
        Label(self, text="Hora inicial").grid(row=1, column=0, sticky="e")
        self.ent_hora_inicial = Entry(self)
        self.ent_hora_inicial.grid(row=1, column=1)
        Label(self, text="Hora final").grid(row=2, column=0, sticky="e")
        self.ent_hora_final = Entry(self)
        self.ent_hora_final.grid(row=2, column=1)
        Label(self, text="Jefe de turno").grid(row=3, column=0, sticky="e")
        self.ent_jefe_turno = Entry(self)
        self.ent_jefe_turno.grid(row=3, column=1)
        Label(self, text="Maquinaria").grid(row=4, column=0, sticky="e")
        self.ent_maquinaria = Entry(self)
        self.ent_maquinaria.grid(row=4, column=1)
        Label(self, text="Nombre de la Referencia").grid(row=5, columnspan=2)
        Label(self, text="P.T.").grid(row=6, column=0, sticky="e")
        self.ent_pt = Entry(self)
        self.ent_pt.grid(row=6, column=1)
        Label(self, text="M.P.").grid(row=7, column=0, sticky="e")
        self.ent_mp = Entry(self)
        self.ent_mp.grid(row=7, column=1)
        Label(self, text="Produccion Turno").grid(row=8, columnspan=2)
        Label(self, text="Desperdicio Preforma").grid(
            row=9, column=0, sticky="e"
        )
        self.ent_preforma = Entry(self)
        self.ent_preforma.grid(row=9, column=1)
        Label(self, text="Desperdicio Envase").grid(
            row=10, column=0, sticky="e"
        )
        self.ent_envase = Entry(self)
        self.ent_envase.grid(row=10, column=1)
        Label(self, text="Produccion Total").grid(
            row=11, column=0, sticky="e"
        )
        self.ent_produccion_total = Entry(self)
        self.ent_produccion_total.grid(row=11, column=1)
        self.btn_calcular = Button(
            self, text="Calcular", bg="#EFDAD7", command=self.calcular
        )
        self.btn_calcular.grid(row=12, column=0)
        self.btn_limpiar = Button(
            self, text="Limpiar", bg="#EFDAD7", command=self.limpiar
        )
        self.btn_limpiar.grid(row=12, column=1)
        self.lbf_informe = ttk.LabelFrame(self)
        self.lbf_informe.grid(row=13, columnspan=2, sticky="we")
        Label(self.lbf_informe, text="Total de desperdicio").grid(
            row=0, column=0,
        )
        self.lbl_total_desperdicio = Label(self.lbf_informe, text="")
        self.lbl_total_desperdicio.grid(row=0, column=1)
        Label(self.lbf_informe, text="Producción Conforme").grid(
            row=1, column=0,
        )
        self.lbl_produccion_conforme = Label(self.lbf_informe, text="")
        self.lbl_produccion_conforme.grid(row=1, column=1)
        self.btn_informe = Button(
            self, text="Informe", bg="#EFDAD7", command=self.informe
        )
        self.btn_informe.grid(row=14, columnspan=2)
  
  #El método "calcular" captura en la instancia "formulario"  las diferentes entradas de texto
    def calcular(self):
        formulario = Formulario(
            fecha=_today_date(),
            turno=self.turno,
            hora_inicial=self.ent_hora_inicial.get(),
            hora_final=self.ent_hora_final.get(),
            jefe_turno=self.ent_jefe_turno.get(),
            maquinaria=self.ent_maquinaria.get(),
            preforma=self.ent_preforma.get(),
            envase=self.ent_envase.get(),
            produccion_total=self.ent_produccion_total.get(),
        )
        self.f = formulario
        #El texto del label "total_desperdicio" será igual al atributo de instancia ".total_desperdicio", y  de la misma forma ocurre con 
        #produccion conforme
        self.lbl_total_desperdicio.config(text=formulario.total_desperdicio)
        self.lbl_produccion_conforme.config(text=formulario.produccion_conforme)
        #retorna  la instancia
        return formulario

    def informe(self):
        #Toplevel: ventana superior
        display = Toplevel()
        display.title("Informe")
        #dimensiones del texto en la ventana
        w = Text(display, width=36, height=12)
        #inserta los strings accediando al método to_str()
        w.insert("end", self.f.to_str())
        #Para que no sea modificado el texto de la ventana, el state deberá ser  disabled
        w.config(state="disabled")
        w.pack()
        
        #"Limpia" o "resetea" las diferentes entradas 
    def limpiar(self):
        self.ent_hora_inicial.delete("0", "end")
        self.ent_hora_final.delete("0", "end")
        self.ent_jefe_turno.delete("0", "end")
        self.ent_maquinaria.delete("0", "end")
        self.ent_preforma.delete("0", "end")
        self.ent_envase.delete("0", "end")
        self.ent_produccion_total.delete("0", "end")

#La clase Container hereda la clase frame
class Container(Frame):
  
    def __init__(self, master, turno):
        super().__init__(master)
        #Número de columnas:3
        self.N = 3
        self.widgets = []
        self.turno = turno
        Label(self, text=f"Turno {self.turno}").grid(
            row=0, column=0, sticky="w"
        )
        Label(self, text=f"Fecha: {_today_date()}").grid(row=0, column=1)
        self.setup_ui()
        self.master.after(1000, self.update)
#Frame de totales
    def setup_ui(self):
        for n in range(self.N):
            w = Widget(self, n + 1)
            w.grid(row=1, column=n, padx=15, pady=15)
            self.widgets.append(w)
        self.lbf_informe = ttk.LabelFrame(self, text="Totales")
        self.lbf_informe.grid(row=13, columnspan=self.N, sticky="we")
        self.actualizar = Button(
            self.lbf_informe, text="Actualizar", command=self.update,
        )
        self.actualizar.grid(row=0, column=0, padx=5, pady=5)
        Label(self.lbf_informe, text="Total de desperdicio").grid(
            row=0, column=1,
        )
        self.lbl_total_desperdicio = Label(self.lbf_informe, text="")
        self.lbl_total_desperdicio.grid(row=0, column=2)
        Label(self.lbf_informe, text="Porcentaje de desperdicio").grid(
            row=0, column=3,
        )
        self.lbl_porcentaje_desperdicio = Label(self.lbf_informe, text="")
        self.lbl_porcentaje_desperdicio.grid(row=0, column=4)
        Label(self.lbf_informe, text="Total de producción").grid(
            row=0, column=5,
        )
        self.lbl_produccion = Label(self.lbf_informe, text="")
        self.lbl_produccion.grid(row=0, column=6)

    def update(self):
        #Suma los totales de desperdicio y producción de cada maquina
        desperdicio = sum([
            float(w.calcular().total_desperdicio) for w in self.widgets
        ])
        produccion = sum([
            float(w.calcular().produccion_conforme) for w in self.widgets
        ])
        #El texto del label total_desperdicio será igual a desperdicio
        self.lbl_total_desperdicio.config(text=str(desperdicio))
        #El texto del label porcentaje desperdicio será igual a desperdicio/100
        self.lbl_porcentaje_desperdicio.config(
            text=f"{(desperdicio / 100):.2f}%"
        )
        #El texto del label produccion será igual a produccion
        self.lbl_produccion.config(text=str(produccion))

#lA clase FrameScrollbar hereda la clase frame
#En resumidas cuentas la barra de desplazamiento
class FrameScrollbar(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.scroll = Scrollbar(self, orient="vertical")
        self.scroll.pack(side="right", fill="y")
        self.canvas = Canvas(self, borderwidth=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll.set)
        self.frame = Frame(self.canvas)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#La venta raíz:
class App(Tk):

    def __init__(self, N):
        super().__init__()
        self.widgets = []
        self.N = N
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame = FrameScrollbar(self)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.geometry("920x630")
        self.setup()

    def setup(self):
        Label(
            self.frame.frame,
            text="Arranque de Producción Máquina y control de eficiencia",
        ).grid(row=0, columnspan=self.N)
        for n in range(self.N):
            w = Container(self.frame.frame, n + 1)
            w.grid(row=n, column=0, padx=15, pady=15)
            self.widgets.append(w)


if __name__ == "__main__":
    #Como son dos turnos, N deberá ser igual a 2, pues se precisa un número de fila por cada turno: Turno1 arriba, Turno2 abajo 
    app = App(N=2)
    app.mainloop()