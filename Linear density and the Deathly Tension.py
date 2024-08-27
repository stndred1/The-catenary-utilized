import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

x1, y1 = 0, 0

def solve_catenary(L, T0, x1, y1, x2, y2):
    g = 9.811  # Gravitational acceleration (m/s²)

    def equations(vars):
        c1, c2, lambd, mu = vars
        return [
            (c1 / (mu * g)) * np.cosh((mu * g / c1) * c2) - (lambd / (mu * g)) - y1,
            (c1 / (mu * g)) * np.cosh((mu * g / c1) * (x2 + c2)) - (lambd / (mu * g)) - y2,
            (c1 / (mu * g)) * (np.sinh((mu * g / c1) * (x2 + c2)) - np.sinh((mu * g / c1) * c2)) - L,
            mu * g * c1 - T0  # Horizontal tension condition
        ]

    return fsolve(equations, [0.002, 0.002, 0.002, 0.008])

def plot_catenary_and_data(c1, c2, mu, lambd, x1, y1, x2, y2, x_data, y_data):
    g = 9.811
    x = np.linspace(x1, x2, 500)
    y = (c1 / (mu * g)) * np.cosh((mu * g / c1) * (x + c2)) - (lambd / (mu * g))

    plt.plot(x, y, 'orange', label='Catenary Curve')
    plt.scatter([x1, x2], [y1, y2], color='red', label='Endpoints')
    plt.scatter(x_data, y_data, color='blue', label='Kinovea Data Points')
    
    # Generate a curve through the additional data points
    x_data_curve = np.linspace(min(x_data), max(x_data), 500)
    y_data_curve = np.interp(x_data_curve, x_data, y_data)
    plt.plot(x_data_curve, y_data_curve, 'green', linestyle='--', label='Curve through Additional Points')
    
    plt.title(f'Catenary Curve Predicted and Kinovea Data μ=' + str(mu.round(5)) )
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Start at (0, 0) with point B as the right endpoint.\n")
    L = float(input("Cable length (m): "))
    x2, y2 = float(input("x-coordinate of B (m): ")), float(input("y-coordinate of B (m): "))
    weight = float(input("Weight at lowest point (kg): "))
    T0 = 9.811 * weight


    # Solve the catenary problem
    c1, c2, lambd, mu = solve_catenary(L, T0, x1, y1, x2, y2)
    print(f"c1 = {c1}\nc2 = {c2}\nlambda = {lambd}\nμ = {mu}")

# Data from Kinovea
    x_data = [0.0000,0.0020, 0.0069, 0.0107, 0.0155, 0.0223, 0.0299, 0.0344, 0.0425, 0.0443,
                0.0495, 0.0548, 0.0636, 0.0679, 0.0772, 0.0916, 0.0990, 0.1080, 0.1111, 0.1159,
                0.1273, 0.1387, 0.1535, 0.1724, 0.1736, 0.1880, 0.2060, 0.2245, 0.2390, 0.2493,
                0.2701, 0.2867, 0.3098, 0.3138, 0.3240, 0.3450, 0.3646, 0.3652, 0.3877, 0.4090,
                0.4266, 0.4328, 0.4410, 0.4529, 0.4641, 0.4838, 0.4874, 0.4957, 0.5062, 0.5177,
                0.5196, 0.5202, 0.5205, 0.5207, 0.5213, 0.5224 
]
    y_data = [0.0003, -0.0106, -0.0250, -0.0407, -0.0577, -0.0734, -0.0899, -0.1041, -0.1245,
                -0.1293, -0.1469, -0.1657, -0.1879, -0.1967, -0.2116, -0.2409, -0.2617, -0.2805,
                -0.2850, -0.2947, -0.3125, -0.3277, -0.3494, -0.3757, -0.3771, -0.3936, -0.4099,
                -0.4277, -0.4404, -0.4457, -0.4513, -0.4564, -0.4565, -0.4582, -0.4580, -0.4585,
                -0.4551, -0.4548, -0.4463, -0.4357, -0.4227, -0.4185, -0.4120, -0.4040, -0.3886,
                -0.3667, -0.3608, -0.3522, -0.3357, -0.3130, -0.3019, -0.3027, -0.3012, -0.3012,
                -0.3012, -0.2907
]

    # Plot the catenary curve and the additional data points
    plot_catenary_and_data(c1, c2, mu, lambd, x1, y1, x2, y2, x_data, y_data)
