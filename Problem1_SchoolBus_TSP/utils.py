def print_route(route, cities, total_distance):
    named_route = [cities[i] for i in route]

    print("\nOptimal Route:")
    print(" -> ".join(named_route))
    print(f"Total Distance: {total_distance}")
