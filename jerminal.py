import pathlib
import sys

from consts import *


def main():
    """
    Main program execution
    :return:
    """
    code = 0
    journals_dir = get_journals_dir()

    show_welcome()
    while code != -1:
        code = show_main_menu(journals_dir)

    return WELCOME_COLOR + "Have a great day!"


def create_journal(journal_dir):
    """
    Prompts user for journal name and then creates new .txt file
    :param journal_dir:
    :return:
    """
    while True:
        journal_name = input(USER_INPUT_COLOR + "What would you like to call this journal? ")
        journal_name = journal_name.replace(" ", "") + ".txt"
        if type(journal_name) == str and len(journal_name) <= 50:
            new_file_path = journal_dir / pathlib.Path(journal_name)
            if not new_file_path.is_file():
                new_file_path.touch()
                break
            else:
                print(COLOR_ERROR + "A journal with that name already exists.", end="\n\n")
        else:
            print(COLOR_ERROR + "Invalid name. Name should be string no longer than 50 characters.")


def get_journals_dir():
    """
    Get the working journals directory from settings
    :return:
    """
    journal_dir = pathlib.Path(DIR)
    if not journal_dir.exists():
        journal_dir.mkdir()
    return journal_dir


def getSettings():
    pass


def get_main_menu_options(journals_dir):
    """
    Generates current main menu options
    :param journals_dir:
    :return:
    """
    return [filename.name for filename in journals_dir.iterdir() if filename.name.endswith(".txt")] + [
        "Create new journal"]


def make_selection(options, selection, journal_dir):
    """
    Takes user selection and takes the appropriate action
    :param options:
    :param selection:
    :param journal_dir:
    :return:
    """
    selection = options[int(selection) - 1]
    if selection == "Create new journal":
        create_journal(journal_dir)
    else:
        show_journal_menu(journal_dir / selection)


def print_options(options):
    """
    Print given options
    :param options:
    :return:
    """
    for index, option in enumerate(options):
        print(f"{index + 1} - {option}")
    print("_" * 20)


def show_entries_menu(journal, oldest):
    """
    Lists journal entries
    :return:
    """
    if oldest:
        pass
    pass


def show_journal_menu(journal_dir):
    """
    Lists journal options
    :param journal_dir:
    :return:
    """
    options = ["New Entry", "List Entries - Most Recent", "List Entries - Oldest"]
    while True:
        print()
        print(WELCOME_COLOR + "::: Journal: " + journal_dir.name + MENU_COLOR)
        print_options(options)
        selection = input(USER_INPUT_COLOR + "Enter your selection: ")
        break


def show_main_menu(journals_dir):
    """
    Show the main menu
    :param journals_dir:
    :return:
    """
    options = get_main_menu_options(journals_dir)

    while True:
        print()
        print(WELCOME_COLOR + "::: Make a selection (q to quit)" + MENU_COLOR)
        print_options(options)

        selection = input(USER_INPUT_COLOR + "Enter your selection: ")
        if selection.lower().strip() == "q":
            return -1
        elif not selection.isnumeric() or int(selection) > len(options) or int(selection) < 1:
            print()
            print(COLOR_ERROR + "That is not a valid option.")
        else:
            make_selection(options, selection, journals_dir)
            break

    return 1


def show_welcome():
    """
    Prints welcome text
    :return:
    """
    print(WELCOME_COLOR + "         ::: Welcome to Jerminal! :::")
    print("=============================================")
    print(ASCII_JOURNAL)


if __name__ == "__main__":
    sys.exit(main())
