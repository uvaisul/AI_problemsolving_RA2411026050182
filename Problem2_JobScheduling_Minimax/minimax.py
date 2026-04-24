def minimax(jobs, depth, is_max, current_time, path, best):
    # Base case: all jobs scheduled
    if len(jobs) == 0:
        return current_time, path

    if is_max:
        max_eval = float("-inf")
        best_path = []

        for i, job in enumerate(jobs):
            next_jobs = jobs[:i] + jobs[i+1:]

            eval_cost, eval_path = minimax(
                next_jobs,
                depth + 1,
                False,
                current_time + job["duration"],
                path + [job["name"]],
                best
            )

            if eval_cost > max_eval:
                max_eval = eval_cost
                best_path = eval_path

        return max_eval, best_path

    else:
        # MIN player simulates delay (worst case)
        min_eval = float("inf")
        best_path = []

        for delay in [0, 2, 5]:  # possible delays
            eval_cost, eval_path = minimax(
                jobs,
                depth + 1,
                True,
                current_time + delay,
                path,
                best
            )

            if eval_cost < min_eval:
                min_eval = eval_cost
                best_path = eval_path

        return min_eval, best_path
