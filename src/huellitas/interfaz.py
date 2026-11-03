import tkinter as tk
from tkinter import messagebox, ttk

from .modelo import Categoria, Punto, Rectangulo
from .servicio import ServicioHuellitas


ANCHO_MAPA = 660
ALTO_MAPA = 440
COLORES = {
    Categoria.MASCOTA_PERDIDA: "#e36f52",
    Categoria.AVISTAMIENTO: "#e6ad46",
    Categoria.REFUGIO: "#388b79",
}


class VentanaHuellitas(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Huellitas | Primer avance")
        self.configure(bg="#f4f6f3")
        self.resizable(False, False)
        self.servicio = ServicioHuellitas(Rectangulo(0, 0, ANCHO_MAPA, ALTO_MAPA))
        self.categoria = tk.StringVar(value=Categoria.MASCOTA_PERDIDA.value)
        self.descripcion = tk.StringVar()
        self.mostrar_divisiones = tk.BooleanVar(value=True)
        self.estado = tk.StringVar(value="Completa el registro y haz clic en el mapa.")
        self.resumen = tk.StringVar()
        self._crear_estilos()
        self._crear_interfaz()
        self._actualizar_vista()

    def _crear_estilos(self) -> None:
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("TCombobox", padding=7, fieldbackground="white", arrowsize=14)
        estilo.configure("TEntry", padding=8, fieldbackground="white")
        estilo.configure("Accion.TButton", padding=(14, 10), font=("Segoe UI", 10, "bold"))

    def _crear_interfaz(self) -> None:
        encabezado = tk.Frame(self, bg="#173e36", padx=28, pady=17)
        encabezado.pack(fill="x")
        tk.Label(encabezado, text="HUELLITAS", bg="#173e36", fg="white",
                 font=("Segoe UI", 19, "bold")).pack(anchor="w")
        tk.Label(encabezado, text="Un mapa para organizar pistas y puntos de ayuda",
                 bg="#173e36", fg="#c8ded6", font=("Segoe UI", 10)).pack(anchor="w")

        contenido = tk.Frame(self, bg="#f4f6f3", padx=24, pady=20)
        contenido.pack(fill="both", expand=True)
        lateral = tk.Frame(contenido, bg="white", padx=18, pady=17, width=270)
        lateral.pack(side="left", fill="y", padx=(0, 18))
        lateral.pack_propagate(False)
        tk.Label(lateral, text="Nuevo registro", bg="white", fg="#1f3d36",
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=(0, 6))
        tk.Label(lateral, text="Selecciona una categoría y\ncoloca el punto en el mapa.",
                 bg="white", fg="#65766f", justify="left", font=("Segoe UI", 9)).pack(anchor="w", pady=(0, 17))
        self._etiqueta(lateral, "CATEGORÍA")
        ttk.Combobox(lateral, textvariable=self.categoria, state="readonly",
                     values=[categoria.value for categoria in Categoria]).pack(fill="x", pady=(5, 15))
        self._etiqueta(lateral, "NOMBRE O DESCRIPCIÓN")
        ttk.Entry(lateral, textvariable=self.descripcion).pack(fill="x", pady=(5, 8))
        tk.Label(lateral, text="Ejemplo: Perrita vista en el parque", bg="white", fg="#81908a",
                 font=("Segoe UI", 8)).pack(anchor="w", pady=(0, 19))
        tk.Checkbutton(lateral, text="Mostrar divisiones", variable=self.mostrar_divisiones,
                       command=self._actualizar_vista, bg="white", fg="#27483d",
                       activebackground="white", font=("Segoe UI", 10)).pack(anchor="w")
        ttk.Button(lateral, text="Cargar ejemplo", style="Accion.TButton",
                   command=self.cargar_ejemplo).pack(fill="x", pady=(16, 7))
        ttk.Button(lateral, text="Limpiar mapa", command=self.limpiar).pack(fill="x")

        panel = tk.Frame(contenido, bg="#f4f6f3")
        panel.pack(side="left", fill="both")
        barra = tk.Frame(panel, bg="#f4f6f3")
        barra.pack(fill="x", pady=(0, 8))
        tk.Label(barra, text="Mapa de registros", bg="#f4f6f3", fg="#1f3d36",
                 font=("Segoe UI", 15, "bold")).pack(side="left")
        tk.Label(barra, textvariable=self.resumen, bg="#f4f6f3", fg="#61766b",
                 font=("Segoe UI", 9)).pack(side="right")
        self.mapa = tk.Canvas(panel, width=ANCHO_MAPA, height=ALTO_MAPA, bg="#eef4ec",
                              highlightthickness=1, highlightbackground="#d1ddd1")
        self.mapa.pack()
        self.mapa.bind("<Button-1>", self._al_hacer_clic)
        leyenda = tk.Frame(panel, bg="#f4f6f3")
        leyenda.pack(fill="x", pady=(10, 0))
        for categoria, color in COLORES.items():
            tk.Label(leyenda, text="●", fg=color, bg="#f4f6f3", font=("Segoe UI", 11)).pack(side="left")
            tk.Label(leyenda, text=categoria.value, fg="#52685e", bg="#f4f6f3",
                     font=("Segoe UI", 9)).pack(side="left", padx=(2, 16))
        tk.Label(panel, textvariable=self.estado, bg="#f4f6f3", fg="#516b60",
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(8, 0))

    @staticmethod
    def _etiqueta(contenedor: tk.Frame, texto: str) -> None:
        tk.Label(contenedor, text=texto, bg="white", fg="#566c62",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")

    def _al_hacer_clic(self, evento: tk.Event) -> None:
        try:
            self.servicio.registrar(Categoria(self.categoria.get()), self.descripcion.get(),
                                   Punto(evento.x, evento.y))
        except ValueError as error:
            messagebox.showwarning("No se pudo registrar", str(error), parent=self)
            return
        self.estado.set(f"Registro agregado: {self.descripcion.get().strip()}.")
        self.descripcion.set("")
        self._actualizar_vista()

    def cargar_ejemplo(self) -> None:
        self.servicio.reiniciar()
        ejemplos = (
            (Categoria.MASCOTA_PERDIDA, "Luna", 120, 100),
            (Categoria.AVISTAMIENTO, "Avistamiento de Luna", 210, 145),
            (Categoria.REFUGIO, "Refugio Patitas", 480, 110),
            (Categoria.AVISTAMIENTO, "Perro junto al parque", 140, 290),
            (Categoria.MASCOTA_PERDIDA, "Milo", 375, 300),
            (Categoria.REFUGIO, "Centro de ayuda", 545, 340),
            (Categoria.AVISTAMIENTO, "Gato en el jardín", 300, 90),
            (Categoria.AVISTAMIENTO, "Avistamiento en la plaza", 75, 185),
        )
        for categoria, descripcion, x, y in ejemplos:
            self.servicio.registrar(categoria, descripcion, Punto(x, y))
        self.estado.set("Ejemplo cargado. Haz clic en el mapa para agregar puntos.")
        self._actualizar_vista()

    def limpiar(self) -> None:
        self.servicio.reiniciar()
        self.estado.set("Mapa limpio. Completa el registro y haz clic en el mapa.")
        self._actualizar_vista()

    def _actualizar_vista(self) -> None:
        self.mapa.delete("all")
        if self.mostrar_divisiones.get():
            for nodo in self.servicio.arbol.recorrer_nodos():
                if nodo.es_hoja:
                    continue
                region = nodo.region
                centro_x = region.izquierda + region.ancho / 2
                centro_y = region.superior + region.alto / 2
                self.mapa.create_line(centro_x, region.superior, centro_x,
                                      region.superior + region.alto, fill="#a7c5b2", width=2)
                self.mapa.create_line(region.izquierda, centro_y,
                                      region.izquierda + region.ancho, centro_y,
                                      fill="#a7c5b2", width=2)
        for registro in self.servicio.registros:
            x, y = registro.posicion.x, registro.posicion.y
            self.mapa.create_oval(x - 7, y - 7, x + 7, y + 7,
                                  fill=COLORES[registro.categoria], outline="white", width=2)
            self.mapa.create_text(x + 12, y - 11, text=registro.descripcion, anchor="sw",
                                  fill="#355349", font=("Segoe UI", 9))
        cantidad = len(self.servicio.arbol)
        self.resumen.set(f"{cantidad} registro{'s' if cantidad != 1 else ''} · capacidad 4")


def iniciar_aplicacion() -> None:
    VentanaHuellitas().mainloop()
