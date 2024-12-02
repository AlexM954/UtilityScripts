import os
import csv
import glob
import time
import argparse


def list_files(source, output_name, pattern="*", recursive=False,
               rename=False, folders=False):
    # Check if the source folder exists.
    if os.path.isdir(source):

        t0 = time.perf_counter()

        # adjust the pattern to allow recursive searches.
        pattern = os.path.join(
            source, "**" if recursive else "", pattern
        )

        # List all files that match the pattern.
        filepath_list = glob.glob(pattern, recursive=recursive)

        # Put all files in a csv file.
        cwd = os.getcwd()
        output = cwd + "/" + output_name + ".csv"
        with open(output, mode="w") as csvfile:
            writer = csv.writer(csvfile)
            if rename:
                writer.writerow(
                    ["Path", "Old name", "New name", "Extension"])
            else:
                writer.writerow(["Folder", "Name", "Extension"])
            for filepath in filepath_list:
                dir, filename = os.path.split(filepath)
                name, ext = os.path.splitext(filename)
                if not os.path.isfile(filepath) and folders is True:
                    if rename:
                        writer.writerow([dir, name, dir, name, ext])
                    else:
                        writer.writerow([dir, name, ext])
                elif os.path.isfile(filepath) and folders is False:
                    if rename:
                        writer.writerow([dir, name, name, ext])
                    else:
                        writer.writerow([dir, name, ext])

        t1 = time.perf_counter()

        print(
            f"Succesfully listed files in {(t1 - t0):.3f} seconds."
        )

    else:
        print(
            f"The directory {source} does not exist."
        )


def main():
    parser = argparse.ArgumentParser(
        description="List files in a source directory, optionally with \
        filtering and put the output in a csv file."
    )
    parser.add_argument(
        "source", help="Source directory to list files in.")
    parser.add_argument(
        "output", help="Name of the output file.")
    parser.add_argument(
        "--pattern", "-p", default="*", help="Pattern to filter files on.")
    parser.add_argument(
        "--recursive", "-rec", action="store_true", help="Recursively include \
        subdirectories.")
    parser.add_argument(
        "--rename", "-r", action="store_true", help="Change output to allow \
        for renaming using the rename.py script.")
    parser.add_argument(
        "--folders", "-f", action="store_true", help="Only include folders \
        in the list")

    args = parser.parse_args()

    list_files(args.source, args.output, pattern=args.pattern,
               recursive=args.recursive, rename=args.rename,
               folders=args.folders)


if __name__ == "__main__":
    main()
