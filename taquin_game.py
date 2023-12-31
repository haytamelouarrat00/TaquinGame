#!/usr/bin/env python3
import time

from Solver import *



def main():
    ai_game()


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    run_time = end_time - start_time
    formatted_run_time = "{:.5f}".format(run_time)
    print(f"Total run time: {formatted_run_time} seconds")
