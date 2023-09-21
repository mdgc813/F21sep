import turtle
import math

# Configuración de la ventana de dibujo
ventana = turtle.Screen()
ventana.bgcolor("white")

# Creación de una instancia de Turtle
curva = turtle.Turtle()
curva.shape("classic")
curva.speed(0.05)  # Establece una velocidad más lenta (1 es la más lenta)
curva.fillcolor("yellow")
# Definición de la función r(a)
def r(a):
    return math.sin(7 * a / 2)  # Función r(a)

# Ángulo inicial para la curva
a = 0

# Longitud de paso para el dibujo
step_length = 0.012

# Mueve la Turtle a la posición inicial
curva.penup()
x = r(a) * math.cos(a) * 300  # Escala el resultado para que se ajuste a la ventana
y = r(a) * math.sin(a) * 300  # Escala el resultado para que se ajuste a la ventana
curva.goto(x, y)
curva.pendown()

# Dibuja la curva r = sin(7a/2)
curva.begin_fill()
while a <= 4 * math.pi:
    x = r(a) * math.cos(a) * 300  # Escala el resultado para que se ajuste a la ventana
    y = r(a) * math.sin(a) * 300  # Escala el resultado para que se ajuste a la ventana
    curva.goto(x, y)
    a += step_length
curva.end_fill()
# No se cierra la ventana al hacer clic
curva.hideturtle()
###################
#############
# Creación de una instancia de Turtle
curva2 = turtle.Turtle()
curva2.shape("classic")
curva2.speed(0.01)  # Establece una velocidad más lenta (1 es la más lenta)
curva2.fillcolor("brown")
# Definición de la función r(a)
def r(a):
    return math.sin(6 * a / 7)  # Función r(a)

# Ángulo inicial para la curva
a = 0

# Longitud de paso para el dibujo
step_length = 0.09

# Mueve la Turtle a la posición inicial
curva2.penup()
x = r(a) * math.cos(a) * 100  # Escala el resultado para que se ajuste a la ventana
y = r(a) * math.sin(a) * 100  # Escala el resultado para que se ajuste a la ventana
curva2.goto(x, y)
curva2.pendown()

# Dibuja la curva r = sin(7a/2)
curva2.begin_fill()
while a <= 14 * math.pi:
    x = r(a) * math.cos(a) * 100  # Escala el resultado para que se ajuste a la ventana
    y = r(a) * math.sin(a) * 100  # Escala el resultado para que se ajuste a la ventana
    curva2.goto(x, y)
    a += step_length
curva2.end_fill()
# No se cierra la ventana al hacer clic
curva2.hideturtle()




# Escribir el mensaje debajo del dibujo (desplazado 300 unidades hacia abajo)
turtle.penup()
turtle.goto(0, -375)  # Posición del mensaje más abajo del dibujo
turtle.pendown()

# Configuración del estilo del texto
turtle.color("red")  # Color de texto rojo
#turtle.textinput()
turtle.write("Que tengas buen día n.n", align="center", font=("cursive", 40, "italic"))

turtle.hideturtle()








###############
##############
turtle.done()  # Finaliza el programa correctamente
