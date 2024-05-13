# -*- coding: utf-8 -*-
import time
import argparse


def calculate_delay(num_lines, scroll_time):
    return scroll_time / num_lines


def main():
    parser = argparse.ArgumentParser(
        description='Scroll through text in a specified amount of time.'
    )
    parser.add_argument('filename', help='Name of the file to scroll through')
    parser.add_argument(
        '-s',
        '--scroll-time',
        type=float,
        help='Number of seconds to scroll through the text',
    )
    args = parser.parse_args()

    # Count the number of lines in the file
    num_lines = sum(1 for line in open(args.filename))

    # Calculate delay per line
    delay_per_line = calculate_delay(num_lines, args.scroll_time)

    # Read and print each line with delay
    with open(args.filename, 'r') as file:
        for line in file:
            print(line.rstrip())
            time.sleep(delay_per_line)


if __name__ == '__main__':
    main()
