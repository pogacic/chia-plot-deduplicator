import os
import yaml

GB_CONVERSION = 1024 * 1024 * 1024
PLOT_SIZE_CHECK = 107

duplicated_plots = {}
malformed_plots = {}


def load_yaml():
    with open(r'config.yml') as file:
        cpd_yaml = yaml.load(file, Loader=yaml.FullLoader)

    return cpd_yaml


def scan_directories(plot_dir: list):
    """
    For each folder in the config.yml files, if plot name is the same in another directory add it to dictionary.
    Also checks if plot is smaller than 107GB and then appends to malformed_plots dictionary.

    Notes:
        - Digusting but it works

    :param plot_dir:
    :return:
    """

    checked_plots = []

    for directory in plot_dir:
        for (dir_path, dir_names, filenames) in os.walk(directory):
            for file in filenames:
                if file.endswith(".txt"):
                    if os.path.getsize(dir_path + "/" + file) / GB_CONVERSION < PLOT_SIZE_CHECK:
                        malformed_plots[dir_path + "/" + file] = dir_path

                    if file not in checked_plots:
                        checked_plots.append(file)
                    else:
                        duplicated_plots[dir_path + "/" + file] = dir_path

    inform_user()


def yes_or_no(question):
    reply = input(question + ' (y/n): ').lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Input letters y or n to decide.")


def inform_user():
    counter = 0

    if duplicated_plots:
        print("Duplicated files")
        print("--------------------------")

        for key, value in duplicated_plots.items():
            print(f"{counter}. {key}")
            counter += 1

        if yes_or_no("Delete duplicated plots?"):
            delete_plot(duplicated_plots)

    if malformed_plots:
        counter = 0
        print(f"\nMalformed files (smaller than {PLOT_SIZE_CHECK}GB)")
        print("--------------------------")
        for key, value in malformed_plots.items():
            print(f"{counter}. {key}")
            counter += 1

        if yes_or_no("Delete malformed plots?"):
            delete_plot(malformed_plots)


def delete_plot(plot_dict: dict):
    for key in plot_dict:
        if os.path.exists(key):
            os.remove(key)
        else:
            print("The file does not exist")


if __name__ == "__main__":
    scan_directories(load_yaml()['plot_directories'])
