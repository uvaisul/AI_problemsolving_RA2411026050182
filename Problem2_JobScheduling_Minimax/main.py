from data import get_jobs
from scheduler import find_best_schedule
from utils import print_schedule


def main():
    jobs = get_jobs()

    best_order, best_cost = find_best_schedule(jobs)

    print_schedule(best_order, best_cost)


if __name__ == "__main__":
    main()
