import os
import glob
import shutil
import argparse


def move(source, destination, pattern="*", recursive=False):
    # Check if the source folder exists.
    if os.path.isdir(source):
        # Make the destination path if it does not exist.
        os.makedirs(destination, exist_ok=True)

        # adjust the pattern to allow recursive searches.
        pattern = os.path.join(
            source, "**" if recursive else "", pattern
        )

        # List all files that match the pattern.
        filepath_list = glob.glob(pattern, recursive=recursive)

        # Move each file to the destination.
        for filepath in filepath_list:
            if os.path.isfile(filepath):
                destinationpath = os.path.join(
                    destination, os.path.basename(filepath)
                )
                shutil.move(filepath, destinationpath)
    else:
        print(
            f"The directory {source} does not exist."
        )


def main():
    parser = argparse.ArgumentParser(
        description="Move files from a source directory to a destination \
                directory with optional filtering."
    )
    parser.add_argument(
        "source", help="Source directory to move files from.")
    parser.add_argument(
        "destination", help="Destination directory to move files to.")
    parser.add_argument(
        "--pattern", "-p", default="*", help="Pattern to filter files on.")
    parser.add_argument(
        "--recursive", "-r", action="store_true", help="Recursively include \
        subdirectories.")

    args = parser.parse_args()

    move(args.source, args.destination,
         pattern=args.pattern, recursive=args.recursive)


if __name__ == "__main__":
    main()
