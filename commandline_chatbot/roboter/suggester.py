import csv
import os
import string

from roboter.csv_writer import make_new_csv


def suggest_checker():
    if os.path.exists("roboter/csv_dir/restaurant.csv"):
        suggest_from_csv()
        return
    else:
        make_new_csv()
        return


def suggest_from_csv():
    with open("roboter/csv_dir/restaurant.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            top_in_csv = (row["Name"])
            with open("roboter/text_dir/suggest.txt") as f:
                t = string.Template(f.read())

            contents = t.substitute(restaurant=top_in_csv)
            print(contents)

            # for i in range(int(len(row["Name"]))):
            reply = input("[Y/n]: ")
            if "y" or "Y" in str(reply):
                break
            elif "n" or "N" in str(reply):
                continue
            else:
                continue
        return