from tsp_solver import nearest_neighbor_tsp
from data import get_sample_data
from utils import print_route
from visualization import plot_route


def main():
    # Load sample data
    cities, distance_matrix = get_sample_data()

    print("Cities:", cities)

    # Solve TSP
    route, total_distance = nearest_neighbor_tsp(distance_matrix, start=0)

    # Print results
    print_route(route, cities, total_distance)

    # Visualize
    plot_route(cities, route)


if __name__ == "__main__":
    main()
