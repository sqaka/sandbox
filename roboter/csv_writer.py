import csv


def make_new_csv():
    with open("roboter/csv_dir/restaurant.csv", "w") as csv_file:
        fieldnames = ["Name", "Count"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


def restaurant_to_csv(restaurant):
    # save_row = {}

    with open("roboter/csv_dir/restaurant.csv", 'r') as csv_file:
        fieldnames = ["Name", "Count"]
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        ks = reader.fieldnames
        return_dict = {k: [] for k in ks}
        # v = list(writer.keys())[0]
        # length = len(restaurant[v])
        # for restaurant in range(length):
        for row in reader:
            for k, v in row.items():
                return_dict[k].append(v)
                print(v)

            if restaurant in return_dict["Name"]:
                keyNumber = return_dict.pop(restaurant)
                break
            else:
                keyNumber = 1

    with open("roboter/csv_dir/restaurant.csv", 'a') as csv_new:
        fieldnames = ["Name", "Count"]
        writer = csv.DictWriter(csv_new, fieldnames=fieldnames)
        print(keyNumber)
        writer.writerow({"Name": restaurant, "Count": keyNumber})



        # number = writer[str(restaurant)]
        # print(number)

        # keyNumber = list(restaurant.keys())[0]
        # length = len(restaurant[keyNumber])
        #
        # for i in range(length):
        #     for k, vs in restaurant.items():
        #         save_row[k] = vs[i]
        #
        #     writer.writerow(save_row)

    # 作成したCSVを読み込む
    # with open("roboter/csv_dir/restaurant.csv", "r") as csv_file:
    #     reader = csv.DictReader(csv_file)
    #     # ヘッダー行を飛ばす
    #     next(reader)

    # with open("roboter/csv_dir/restaurant.csv", "a") as csv_file:
    #     writer = csv.DictWriter(csv_file, fieldnames=["Name", "Count"])
    #     print(writer.keys())

            # writer.writerow(["Name", "Count"])
            # 価格を変更する
            # for line in reader:
            #     if line[1] > 1:
            #         addon_count = float(line[1]) + 1
            #     else:
            #         addon_count = 1

            # writer.writeheader()
        # writer.writerow({"Name": restaurant, "Count": + 1})
    # with open("roboter/csv_dir/restaurant.csv", "r") as csv_file:
    #     reader = csv.DictReader(csv_file)
    #     count = 0
    #     if row["Count"] > 1:
    #         count = row["Count"]

    #     for row in reader:
    #         with open("roboter/csv_dir/restaurant.csv", "a") as csv_file:
    #             fieldnames = ["Name", "Count"]
    #             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #             if restaurant in writer:
    #                 writer.remove(restaurant)
    #                 break
    #             else:
    #                 continue
        # writer.writeheader()
        #     try:
        #         count = int(writer.pop({"Name" is restaurant}))
        #         writer[restaurant] = int(count) + 1
        #     except:
        #         continue
        #   writer.writerow({"Name": restaurant, "Count": int(count) + 1})
        # if restaurant in writer.row["Name"]:
        #    writer[restaurant] = +1
        # else:

