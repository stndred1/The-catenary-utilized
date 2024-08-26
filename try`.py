import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

L = 0.8813

def catenary_solver(L, mu):
    g = 9.811  # gravitational acceleration

    # Boundary conditions
    x1, y1 = 0, 0
    x2, y2 = 0.5239, -0.2991

    # Define the system of equations
    def equations(vars):
        c1, c2, lambd = vars
        eq1 = (c1 / (mu * g)) * np.cosh((mu * g / c1) * c2) - (lambd / (mu * g)) - y1
        eq2 = (c1 / (mu * g)) * np.cosh((mu * g / c1) * (x2 + c2)) - (lambd / (mu * g)) - y2
        eq3 = (c1 / (mu * g)) * (np.sinh((mu * g / c1) * (x2 + c2)) - np.sinh((mu * g / c1) * c2)) - L
        return [eq1, eq2, eq3]

    # Initial guess for c1, c2, and lambda
    initial_guess = [0.01, 0.01, 0.008]

    # Solve the system of equations
    solution = fsolve(equations, initial_guess)
    return solution

def plot_catenary(c1, c2, mu):
    g = 9.811  # gravitational acceleration

    # Generate x values
    x_vals = np.linspace(0, 0.5239, 500)
    
    # Calculate y values using the catenary formula
    y_vals = (c1 / (mu * g)) * np.cosh((mu * g / c1) * (x_vals + c2)) - (lambd / (mu * g)) 
    
    # Plot the catenary
    plt.plot(x_vals, y_vals, label='Catenary Curve')
    plt.scatter([0, 0.5239], [0, -0.2991], color='red', label='Boundary Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Catenary Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    mu = float(input("Enter the mass per unit length (mu): "))

    c1, c2, lambd = catenary_solver(L, mu)

    print(f"Solution:\n c1 = {c1}\n c2 = {c2}\n lambda = {lambd}")

    plot_catenary(c1, c2, mu)
