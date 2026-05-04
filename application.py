import streamlit as st
import Num_methods
import plotly.graph_objects as go
import numpy as np 
col1,col2 = st.columns(2)

with col1:
    st.title("Polynomial Equation solver")
    st.write("Select the degree of your equation and choose the solver")

    n = st.number_input("Degree",step = 1,format = "%d")
    coeffs = []

    for i in range(0,n+1):
        coff = st.number_input(f"Enter a{i}", format = "%.6f")
        coeffs.append(coff)
    
    solver = st.selectbox("Select Solver",[
        "Bisection Method",
        "False Position(Regula Falsi)",
        "Newton Raphson",
        "Secant Method"
    ])

func = lambda x,coeffs: sum(c*x**k for k,c in enumerate(coeffs))

with col2:
        st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>",unsafe_allow_html = True)
        x1 = st.number_input("Plotting range lower limit: ")
        x2 = st.number_input("Plotting range upper limit: ")
        x = np.linspace(x1,x2,1000)
        y = func(x,coeffs)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = x,y = y,mode = 'lines'))
        st.plotly_chart(fig,use_container_width = True)     


with col1:
    match solver:
        case "Bisection Method":
            a = st.number_input("Enter left sided initial value: ",format = "%.3f")
            b = st.number_input("Enter right sided initial value: ",format = "%.3f")
            
            tol_log = st.slider("Tolerence(log scale)",min_value =-12,max_value = 0, step = 1,format = "%d")
            tol = 10**(tol_log)
            max_iter = st.number_input("Maximum Iterations",step = 1,format = "%d")

            if st.button("Solve"):
                (sol,itr) = Num_methods.bisect(func,a,b,tol,coeffs,max_iter)
                
                if sol == "invalid limits":
                    st.warning("Invalid Limits!  \n[a,b] must fulfill the condition f(a)*f(b)<0 ")
                elif sol == "CF":
                    st.error("Convergence Failed.Maximum Iteration reached!")
                else:
                    st.success(f"One solution : {sol}  \nNumber of Iterations: {itr}")
                    st.info(f"Range = [{a},{b}]  \nTolerence = {tol}  \nMethod : Bisection")
        
        case "Newton Raphson":
            x0 = st.number_input("Initial guess",format = "%0.3f")
            tol_log = st.slider("Tolerance(log scale)",min_value = -12,max_value = 0,step = 1)
            tol = 10**tol_log 
            hlog = st.slider("Step Size(log)",min_value = -15, max_value = 0,step = 1)
            h = 10**hlog
            max_iter = st.number_input("Maximum Iteration",step = 1, format = "%d")

            if st.button("Solve"):
                
                (sol,itr) = Num_methods.NR(func,x0,coeffs,tol,h,max_iter)
                
                if sol == "CF":
                    st.error("Convergence Failed. Maximum Iteration reached!")
                else:
                    st.success(f"One Solution: {sol}  \nNumber of Iterations: {itr}")
                    st.info(f"initial guess: {x0}  \nTolerance: {tol}  \nStep Size: {h}  \nMethod: Newton Raphson")

        case "Secant Method":
            x0 = st.number_input("First initial guess")
            x1 = st.number_input("Second initial guess")
            max_iter = st.number_input("Maximum Iterations",step = 1,format = "%d")
            tol_log = st.slider("Tolerance(log scale)",min_value = -12,max_value = 0,step = 1)
            tol = 10**tol_log

            if st.button("Solve"):
                (sol,itr) = Num_methods.secant(func,x0,x1,coeffs,max_iter,tol)

                if sol == "CF":
                    st.error("Convergence Failed. Maximum iteration reached!")
                else:
                    st.success(f"One solution: {sol}  \nNumber of iterations: {itr}")
                    st.info(f"initial guesses: ({x0},{x1})  \nTolerance: {tol}  \nMethod: Secant")
        
        case "False Position(Regula Falsi)":
            a = st.number_input("Enter left sided initial value")
            b = st.number_input("Enter right sided initial value")
            tol_log = st.slider("Tolerance(log scale)",min_value = -12,max_value = 0, step = 1)
            tol = 10**tol_log
            max_iter = st.number_input("Maximum Iteration",step = 1,format = "%d")

            if st.button("Solve"):
                (sol,itr) = Num_methods.regula_falsi(func,a,b,coeffs,tol,max_iter)

                if sol == "invalid limits":
                    st.warning("Invalid limits. The limits must satisfy the condition f(a)*f(b)<0")
                elif sol == "CF":
                    st.error("Convergence Failed. Maximum iterations reached")
                else:
                    st.success(f"One solution: {sol}  \nNumber of iterations: {itr}")
                    st.info(f"Tolerance: :{tol}  \nMethod: False Position")
                
        

            
                

                    
            
                       
        


            