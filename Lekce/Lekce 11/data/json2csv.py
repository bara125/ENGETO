import os
import csv
import sys
import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--files_dir", type=str, default="data", help="Cesta k slozce s json soubory"
)


def find_all_json_files(files_dir: str | Path) -> list[str]:
    all_json_fpaths = []
    # tady pocitame s tim ze jsme v slozce "notebooks" a tak
    # vidime slozku "data"
    for fname in os.listdir(files_dir):  # JINE pro Path z pathlibu
        # fname.split(".")[-1] == "json"
        if fname.endswith(".json"):
            all_json_fpaths.append(os.path.join(files_dir, fname))
    return all_json_fpaths


def read_json(json_fpath: str) -> dict:
    with open(json_fpath, mode="r", encoding="utf-8") as f:
        return json.load(f)


def filter_keys(contents: dict, keys_to_save=("jmeno", "konkurence")) -> dict:
    filtered_contents = {}
    for key, value in contents.items():
        if key in keys_to_save:
            filtered_contents[key] = value

    # muzeme napsat pomoci dict comprehensionu
    return filtered_contents


def write_to_csv(csv_fpath: str, contents: dict) -> None:
    with open(csv_fpath, mode="w", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=contents.keys())
        csv_writer.writeheader()
        csv_writer.writerow(contents)


def main():
    # hard-coded
    # files_dir = "data"

    # jednodussi varianta pomoci sys.argv
    # if len(sys.argv) != 2:
    #     print("Spatne mnozstvi argumentu")
    #     sys.exit()
    # files_dir = sys.argv[1]

    # pokrocilejsi varianta pomoci argparse
    args = parser.parse_args()
    files_dir = args.files_dir

    # muzete vyzkouset click

    print(f"Zpracovavam cestu {files_dir}")
    all_json_files = find_all_json_files(files_dir)
    for json_fpath in all_json_files:
        contents = read_json(json_fpath)
        filtered_contents = filter_keys(contents)
        write_to_csv("test.csv", filtered_contents)


if __name__ == "__main__":
    main()
