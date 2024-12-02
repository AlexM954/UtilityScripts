import os
import csv
import time
import argparse


def rename(input):
    contents = []

    t0 = time.perf_counter()

    with open(input, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contents.append(row)

    for row in contents[1:]:
        path = row[0]
        name_old = row[1]
        name_new = row[2]
        try:
            ext = row[3]
        except IndexError:
            print("Input file is not of the correct format.")
            break

        try:
            os.rename(
                os.path.join(path, name_old + ext),
                os.path.join(path, name_new + ext)
            )
        except FileNotFoundError:
            pass

    t1 = time.perf_counter()

    print(
        f"Succesfully renamed files in {(t1 - t0):.3f} seconds."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Takes a csv file produced by list.py and renames files \
        or folders specified in the file."
    )
    parser.add_argument(
        "input", help="The input csv file.")

    args = parser.parse_args()

    rename(args.input)


if __name__ == "__main__":
    main()
