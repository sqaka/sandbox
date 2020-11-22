import string


def ask_name():
    with open("roboter/text_dir/ask_name.txt") as f:
        print(f.read())


def show_name(user_name):
    with open("roboter/text_dir/ask_restaurant.txt") as f:
        t = string.Template(f.read())

    contents = t.substitute(name=user_name)
    print(contents)


def show_goodbye(user_name):
    with open("roboter/text_dir/say_goodbye.txt") as f:
        t = string.Template(f.read())

    contents = t.substitute(name=user_name)
    print(contents)
