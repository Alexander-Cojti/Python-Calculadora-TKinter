from tkinter import *
import parser
import tkinter.font as font

root = Tk()
root.title("Calculadora")
root.resizable(0, 0) 
# Input Fields
display = Entry(root, font=('arial', 22, 'bold'), bd=0, justify=LEFT)
display.grid(row=0, columnspan=4,  sticky=W+E)

# Get Numbers to Display
i = 0

def Obtener_Numeros(n):
    global i
    display.insert(i, n)
    i += 1

def Obtener_Operacion(operator):
    global i
    opertor_length = len(operator)
    display.insert(i, operator)
    i+=opertor_length

def Calcular():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        LimpiarPantalla()
        display.insert(0, result)
    except Exception:
        LimpiarPantalla()

def LimpiarPantalla():
    display.delete(0, END)


def Rehacer():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        LimpiarPantalla()
        display.insert(0, display_new_state)
    else:
        LimpiarPantalla()

myFont = font.Font(size=12,weight = "bold")
altura=2
ancho=8
ColorNumeric ="gray26"
ForeGround="white"
ColorOperators="orange"
ColorExpresion="black"
ColorClear="gray58"

# Numeric Buttons
Button(root, font=myFont, text="7", height = altura , width = ancho,bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(7)).grid(row=4, column=0)
Button(root, font=myFont,text="8", height = altura , width = ancho,bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(8)).grid(row=4, column=1)
Button(root, font=myFont,text="9", height = altura , width = ancho,bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(9)).grid(row=4, column=2)

Button(root,font=myFont,  text="4", height = altura, width = ancho,bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(4)).grid(row=5, column=0)
Button(root,font=myFont,  text="5", height = altura, width = ancho,bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(5)).grid(row=5, column=1)
Button(root,font=myFont,  text="6", height = altura, width = ancho,bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(6)).grid(row=5, column=2)

Button(root,font=myFont, text="1", height = altura , width = ancho, bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(1)).grid(row=6, column=0)
Button(root,font=myFont, text="2", height = altura , width = ancho, bg=ColorNumeric, fg=ForeGround, command=lambda: Obtener_Numeros(2)).grid(row=6, column=1)
Button(root,font=myFont, text="3", height = altura , width = ancho, bg=ColorNumeric, fg=ForeGround,command=lambda: Obtener_Numeros(3)).grid(row=6, column=2)

# Bottom Button
Button(root, font=myFont, text="(",  height = altura , width = ancho, bg=ColorExpresion, fg=ForeGround,command=lambda: Obtener_Operacion("(")).grid(row=3, column=0,sticky=W+E)
Button(root, font=myFont, text=")",height = altura , width = ancho, bg=ColorExpresion, fg=ForeGround,command=lambda:Obtener_Operacion(")")).grid(row=3, column=1, sticky=W+E)
Button(root, font=myFont, text="exp",height = altura , width =ancho, bg=ColorExpresion, fg=ForeGround,command=lambda: Obtener_Operacion("**")).grid(row=3, column=2)

Button(root, font=myFont, text="AC", height = altura , width = ancho,bg=ColorClear, fg=ForeGround,command=lambda: LimpiarPantalla()).grid(row=2, column=0)
Button(root, font=myFont, text="⟵", height = altura, width = 16,bg=ColorClear, fg=ForeGround,command=lambda: Rehacer()).grid(row=2, column=1, sticky=W+E, columnspan=2)

# More Math Operators
Button(root, font=myFont, text="^2", height = altura , width = ancho,bg=ColorOperators, fg=ForeGround,command=lambda: Obtener_Operacion("**2")).grid(row=2, column=3)
Button(root, font=myFont, text="*",height = altura , width = ancho, bg=ColorOperators, fg=ForeGround,command=lambda: Obtener_Operacion("*")).grid(row=3, column=3)
Button(root, font=myFont, text="/",height = altura , width = ancho, bg=ColorOperators, fg=ForeGround,command=lambda: Obtener_Operacion("/")).grid(row=4, column=3)
Button(root, font=myFont, text="+",height = altura , width = ancho, bg=ColorOperators, fg=ForeGround,command=lambda: Obtener_Operacion("+")).grid(row=5, column=3)
Button(root, font=myFont, text="-",height = altura , width = ancho, bg=ColorOperators, fg=ForeGround,command=lambda: Obtener_Operacion("-")).grid(row=6, column=3)

Button(root,font=myFont, text="0",height = altura , width = 16, bg=ColorNumeric, fg=ForeGround,command=lambda: Obtener_Numeros(0)).grid(row=7, column=0, sticky=W+E,columnspan=2)
Button(root,font=myFont, text=".",height = altura , width = ancho, bg=ColorNumeric, fg=ForeGround, anchor=CENTER,command=lambda: Obtener_Numeros(".")).grid(row=7, column=2, sticky=W+E)
Button(root,font=myFont, text="=",height = altura , width = ancho,bg=ColorOperators, fg=ForeGround, command=lambda: Calcular()).grid(row=7, column=3, sticky=W+E)

root.mainloop()
