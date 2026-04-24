import matplotlib.pyplot as plt
import random


def plot_route(cities, route):
    # Generate random coordinates for cities (for visualization)
    coords = {city: (random.randint(0, 50), random.randint(0, 50)) for city in cities}

    # Plot cities
    for city, (x, y) in coords.items():
        plt.scatter(x, y)
        plt.text(x + 0.5, y + 0.5, city)

    # Draw route lines
    for i in range(len(route) - 1):
        city1 = cities[route[i]]
        city2 = cities[route[i + 1]]

        x_values = [coords[city1][0], coords[city2][0]]
        y_values = [coords[city1][1], coords[city2][1]]

        plt.plot(x_values, y_values)

    plt.title("School Bus Route (TSP)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()
