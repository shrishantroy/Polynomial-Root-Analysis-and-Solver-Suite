from numpy import nan
def derivative(f,x0,h,coeffs):
    der = (f(x0+h,coeffs) - f(x0,coeffs))/h
    return der 

def NR(f,xi,coeffs,tol,h,max_iter):
    iteration = 0

    while True:
        x_new = xi - f(xi,coeffs)/derivative(f,xi,h,coeffs)
        iteration = iteration + 1
        if abs(x_new - xi)<tol:
            return x_new,iteration
        elif iteration == max_iter:
            return "CF",iteration
        else:
            xi = x_new

def bisect(f,a,b,tol,coeffs,max_iter):
    
    iterations = 0
    if f(a,coeffs)*f(b,coeffs)>0:
        return "invalid limits",iterations
   
    while iterations<max_iter:
        c = (a+b)/2
        if abs(f(c,coeffs))<tol:
            return c,iterations
        elif f(c,coeffs)*f(b,coeffs)<0:
            a = c
            iterations = iterations +1
        elif f(c,coeffs)*f(a,coeffs)<0:
            b = c
            iterations = iterations+1
    if iterations == max_iter:
        return "CF",iterations

def secant(f,x0,x1,coeffs,max_iter,tol):
    iterations = 0

    while True:
        slope = (x1 - x0)/(f(x1,coeffs) - f(x0,coeffs))
        x2 = x1 - f(x1,coeffs)*slope
        iterations = iterations + 1 

        if abs(x2 - x1)<tol:
            return x2,iterations
        elif iterations == max_iter:
            return "CF",iterations
        else:
            x0 = x1
            x1 = x2
def regula_falsi(f,a,b,coeffs,tol,max_iter):
    
    iteration = 0
    if f(a,coeffs)*f(b,coeffs)>0:
        return "invalid limits",iteration

    while iteration<max_iter:
        c = (a*f(b,coeffs) - b*f(a,coeffs))/(f(b,coeffs) - f(a,coeffs))
        if abs(f(c,coeffs))<tol:
            return c,iteration 
        elif f(c,coeffs)*f(b,coeffs)<0:
            a = c
            iteration = iteration + 1
        elif f(c,coeffs)*f(a,coeffs)<0:
            b = c
            iteration = iteration + 1
    if iteration == max_iter:
        return "CF",iteration

