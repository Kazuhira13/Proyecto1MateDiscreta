import tkinter as tk
import math

def calcular_primer_problema():
    n = 15
    k = 2
    combinaciones = math.comb(n, k)
    partidos = combinaciones
    resultado_label2.config(text="Si en el torneo inter universidades participan 15 universidades latinoamericanas para poder ganar el torneo de futbol,"
                               "y sabiendo que las reglas indican que cada equipo se enfrentara a todos los demás equipos sin revancha\n"
                               "¿Cuántos partidos de 30 minutos se deben de programar a lo largo del torneo? \n n es 15 \n k es 2")
    resultado_label.config(text=f"el Resultado es: para {n} universidades jugando sin revancha, se deben programar {partidos} partidos de 30 minutos.")

def calcular_segundo_problema():
    ListaA = {'a', 2, 'c', 3, 'e', 4, 'g', 5, 'i', 6, 'k', 7, 'm'}
    ListaB = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
    resultado = ListaA - ListaB
    resultado_label2.config(text="Cual es el conjunto resultante de la operación A-B si A = {a, 2, c, 3, e, 4, g, 5, i, 6, k, 7, m} y B = {a, b, c, d, e, f, g, h, i}")
    resultado_label.config(text="El Resultado de los conjuntos nos da:\n" + str(resultado))

def calcular_tercer_problema():
    a = 19
    b = 35
    Residuo1 = b // a
    Residuo1_1 = b % a
    Residuo2 = a // Residuo1_1
    Residuo2_1 = a % Residuo1_1
    Residuo3 = Residuo1_1 // Residuo2_1
    Residuo3_1 = Residuo1_1 % Residuo2_1
    Residuo4 = Residuo2_1 % Residuo1_1
    Residuo4_1 = Residuo2_1 // Residuo1_1
    resultado_label2.config(text="Por medio del Algoritmo de Euclides calcular el MCD de 19 - 35")
    resultado_label.config(text="Resultado:\n"
                           f"{b} = {a} * {Residuo1} + {Residuo1_1}\n"
                           f"{a} = {Residuo1_1} * {Residuo2} + {Residuo2_1}\n"
                           f"{Residuo1_1} = {Residuo2_1} * {Residuo3} + {Residuo3_1}\n"
                           f"{Residuo2_1} = {Residuo3_1} * {Residuo4} + {Residuo4_1}")

ventana = tk.Tk()
ventana.title("Proyecto No.1")
ventana.geometry("1000x600")
ventana.configure(bg="#F3F4F6")

titulo_label = tk.Label(ventana, text="Matematica Discreta Proyecto No.1 \nTimothy Gerald Palma Perez 0907-20-6162", font=("Helvetica", 16), bg="#F3F4F6")
titulo_label.pack(pady=10)

instrucciones_label = tk.Label(ventana, text="Preciones cualquier de las opciones mostrara\n la pregunta y su resultado:", font=("Helvetica", 12), bg="#F3F4F6")
instrucciones_label.pack(pady=10)

resultado_label2 = tk.Label(ventana, text="", wraplength=800, font=("Helvetica", 12), bg="#F3F4F6")
resultado_label2.pack(pady=10)

resultado_label = tk.Label(ventana, text="", wraplength=800, font=("Helvetica", 12), bg="#F3F4F6")
resultado_label.pack(pady=10)

boton_problema1 = tk.Button(ventana, text="Primer Problema", command=calcular_primer_problema, bg="#3498db", fg="white", font=("Helvetica", 12))
boton_problema1.pack(pady=5)

boton_problema2 = tk.Button(ventana, text="Segundo Problema", command=calcular_segundo_problema, bg="#27ae60", fg="white", font=("Helvetica", 12))
boton_problema2.pack(pady=5)

boton_problema3 = tk.Button(ventana, text="Tercer Problema", command=calcular_tercer_problema, bg="#e74c3c", fg="white", font=("Helvetica", 12))
boton_problema3.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, bg="#95a5a6", fg="white", font=("Helvetica", 12))
boton_salir.pack(pady=10)

ventana.mainloop()
