def nearest_neighbor_tsp(distance_matrix, start=0):
    n = len(distance_matrix)
    visited = [False] * n
    route = [start]
    visited[start] = True
    total_distance = 0

    current = start

    for _ in range(n - 1):
        nearest = None
        min_dist = float("inf")

        for city in range(n):
            if not visited[city] and distance_matrix[current][city] < min_dist:
                min_dist = distance_matrix[current][city]
                nearest = city

        route.append(nearest)
        visited[nearest] = True
        total_distance += min_dist
        current = nearest

    # Return to start
    total_distance += distance_matrix[current][start]
    route.append(start)

    return route, total_distance
