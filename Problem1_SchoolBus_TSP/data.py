def get_sample_data():
    cities = ["School", "Stop A", "Stop B", "Stop C", "Stop D"]

    distance_matrix = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 17],
        [15, 35, 0, 30, 28],
        [20, 25, 30, 0, 23],
        [25, 17, 28, 23, 0],
    ]

    return cities, distance_matrix
