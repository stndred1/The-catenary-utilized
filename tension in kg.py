import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

mut = 0.0083 / 0.96

def solve_catenary(L, T0, x1, y1, x2, y2):
    g = 9.811  # Gravitational acceleration (m/s²)

    # System of equations to solve for c1, c2, lambda, and mu
    def equations(vars):
        c1, c2, lambd, mu = vars
        return [
            (c1 / (mu * g)) * np.cosh((mu * g / c1) * c2) - (lambd / (mu * g)) - y1,
            (c1 / (mu * g)) * np.cosh((mu * g / c1) * (x2 + c2)) - (lambd / (mu * g)) - y2,
            (c1 / (mu * g)) * (np.sinh((mu * g / c1) * (x2 + c2)) - np.sinh((mu * g / c1) * c2)) - L,
        ]

    # Refined initial guesses
    initial_guess = [0.01, 0.01, 0.01, 0.01]

    # Solve the system of equations with a more relaxed tolerance
    solution = fsolve(equations, initial_guess, xtol=1e-6)

    return solution

def plot_catenary(c1, c2, mu, x1, y1, x2, y2):
    g = 9.811  # Gravitational acceleration (m/s²)
    x_vals = np.linspace(x1, x2, 500)  # Generate x values between boundary points
    y_vals = (c1 / (mu * g)) * np.cosh((mu * g / c1) * (x_vals + c2)) - (c1 / (mu * g)) * np.cosh((mu * g / c2))
    
    # Plotting the catenary curve
    plt.plot(x_vals, y_vals, color='saddlebrown', label = 'Catenary Curve')
    plt.scatter([x1, x2], [y1, y2], color='peru', label ='Boundary Points')
   
    # Labels and legend
    plt.title('Catenary Curve μ =' + str(mu.round(5))+ ' kg/m')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # User inputs
    print('This program is should be used such that the points A is at the origin, and B is the endpoint on the left side of the curve \n')
    L = float(input("Length of the string (meters): "))
    x1, y1 = 0, 0
    x2, y2 = float(input("x2 (m): ")), float(input("y2 (m): "))
    
    # Get the weight in kilograms and calculate T0 as g * weight
    weight_kg = float(input("Enter the weight at the lowest point (kg): "))
    T0 = 9.811 * weight_kg  # Calculate horizontal tension

    # Solve for parameters
    c1, c2, lambd, mu = solve_catenary(L, x1, y1, x2, y2)

    # Display the solution
    print(f"Solution:\n c1 = {c1}\n c2 = {c2}\n lambda = {lambd}\n mu = {mu}")

    # Plot the catenary curve
    plot_catenary(c1, c2, mu, x1, y1, x2, y2)
    
