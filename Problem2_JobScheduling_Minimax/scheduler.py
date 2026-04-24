from minimax import minimax


def find_best_schedule(jobs):
    best_cost, best_order = minimax(
        jobs,
        depth=0,
        is_max=True,
        current_time=0,
        path=[],
        best=None
    )

    return best_order, best_cost
