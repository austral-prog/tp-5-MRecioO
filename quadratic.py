def roots(a, b, c):
    disc = ((b*b)- 4 * a * c)
    if disc < 0:
        return ("( )")
    elif disc == 0:
        return (f"({-b/2*a})")
    elif disc > 0:
        return (f"({(-b+(disc)**0.5)/(2 * a)}, {(-b-(disc)**0.5)/(2 * a)})")

def value_y(a, b, c, x):
    y = a * (x**2)+ b * x + c

    return y
def to_string(a, b, c):
    if (a == 0) and (b == 0):
        f_de_x_constante_str = (f"f(x) = {c}")
        return f_de_x_constante_str
    elif a == 0:
        f_de_x_lineal_str = (f"f(x) = {b} * X + {c}")
        return f_de_x_lineal_str
    elif a != 0:
            if b == 0:
                f_de_x_cuadratica_lineal_str =  (f"f(x) = {a} * X^2 + {c}")
                return f_de_x_cuadratica_lineal_str
            elif b != 0:
                f_de_x_cuadratica_str = (f"f(x) = {a} * X^2 + {b} * X + {c}")
                return f_de_x_cuadratica_str

def derivation(a, b):
    if (a == 0) and ( b == 0):
        dx_f_constante = ((f"f'(x) = 0"))
        return dx_f_constante
   
    elif (a == 0) and (b != 0) :
        dx_f_lineal = ((f"f'(x) = {b}"))
        return dx_f_lineal
    
    elif (a != 0):
        if b == 0:
            dx_f_cuadratica = ((f"f'(x) = {a * 2} * X"))
            return dx_f_cuadratica
        else:
            dx_f_cuadratica_lineal = ((f"f'(x) = {a * 2} * X + {b}"))
            return dx_f_cuadratica_lineal
