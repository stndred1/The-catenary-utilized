
    x = np.linspace(x1, x2, 500)
    mg = mu * g
    y = (c1 / mg) * np.cosh(mg * (x + c2) / c1) - (c1 / mg) * np.cosh(mg * c2 / c1)
    0
    plt.plot(x, y, color='saddlebrown', label='Catenary Curve x(m) vs. y(m) ' + L + ' ' + mu)
    plt.scatter([x1, x2], [y1, y2], color='peru', label='Boundary Points')
    
    plt.title('Catenary Curve x(m) vs. y(m)')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Add gridlines every 0.1 meters
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)