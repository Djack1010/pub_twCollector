import settings


def print_on_file(to_print, d):
    with open(settings.LOG_FILE.format(d), "a+") as f:
        f.write(to_print + "\n")
