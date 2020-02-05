#!/usr/bin/env python3

import sys, argparse, os, datetime

log_files_path = os.path.expanduser("~/.log-files")


class Colours:

    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    END = "\033[0m"


def create_arg_parser():
    parser = argparse.ArgumentParser(description = "Add log messages to a custom log")
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument("-l", "--list-logs", help = "list previous log files", action = "store_true")
    exclusive.add_argument("-n", "--new-log", help = "create a new log file")
    exclusive.add_argument("-s", "--show-log", help = "display the current log", action = "store_true")
    exclusive.add_argument("-d", "--delete-log", help = "delete the curret log", action = "store_true")
    exclusive.add_argument("message", nargs="*", help="the log message", default = "")
    return parser


def get_log_file():
    with open(log_files_path, "r") as f:
        lines = f.read().splitlines()
        return os.path.expanduser(lines[-1])


def main():

    parser = create_arg_parser()
    args = parser.parse_args()

    if args.list_logs:
        with open(log_files_path, "r") as f:
            print(f"{Colours.BLUE}[*] Log files:{Colours.END}")
            print(f.read())

    elif args.new_log:
        if not os.path.exists(log_files_path):
            first_line = True
        else:
            first_line = False

        with open(log_files_path, "a") as f:
            if not first_line:
                f.write("\n")

            f.write(args.new_log)

            if not os.path.exists(args.new_log):
                open(args.new_log, 'a').close()

            print(f"{Colours.GREEN}[+] Log file added: {args.new_log}{Colours.END}")

    elif args.show_log:
        log_file = get_log_file()

        print(f"{Colours.BLUE}[*] Showing log: {log_file}{Colours.END}")

        with open(log_file, "r") as f:
            print(f.read())


    elif args.delete_log:
        log_file = get_log_file()

        if os.path.exists(log_file):
            os.remove(log_file)

    elif args.message:
        log_file = get_log_file()

        with open(log_file, "a") as f:
            message = " ".join(args.message)
            time = datetime.datetime.now()

            f.write(f"{Colours.GREEN}[{time}] - {Colours.BLUE}{message}{Colours.END}\n")

            print(f"{Colours.GREEN}[+] Log added.{Colours.END}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
