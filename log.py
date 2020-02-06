#!/usr/bin/env python3

import sys, argparse, os, datetime, subprocess

log_files_path = os.path.expanduser("~/.log-files")


class Colours:

    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    END = "\033[0m"


def create_arg_parser():
    parser = argparse.ArgumentParser(description = "Add log messages to a custom log.")
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument("-l", "--list-logs", help = "list previous log files", action = "store_true")
    exclusive.add_argument("-n", "--new-log", help = "create a new log file or switch to an old one")
    exclusive.add_argument("-x", "--show-log", help = "display the current log", action = "store_true")
    exclusive.add_argument("-d", "--delete-log", help = "delete the current log", action = "store_true")
    exclusive.add_argument("-g", "--grep", help = "grep the log for a word or phrase")
    message_group = parser.add_argument_group()
    message_type_group = message_group.add_mutually_exclusive_group()
    message_type_group.add_argument("-s", "--success", help="add a success log message", action = "store_true")
    message_type_group.add_argument("-f", "--failure", help="add a fail log message", action = "store_true")
    message_type_group.add_argument("-m", "--remember", help="add a remind me message", action = "store_true")
    message_group.add_argument("message", nargs="*", help="the log message", default = "")
    return parser


def get_log_file():

    if not os.path.exists(log_files_path):
        print(f"{Colours.RED}No log file has been created yet.{Colours.END}")
        sys.exit(1)

    with open(log_files_path, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip() != ""]

        if len(lines) == 0:
            print(f"{Colours.RED}No log file has been created yet.{Colours.END}")
            sys.exit(1)

        return os.path.expanduser(lines[-1])


def main():

    parser = create_arg_parser()
    args = parser.parse_args()


    if args.list_logs:
        if not os.path.exists(log_files_path):
            print(f"{Colours.RED}No log file has been created yet.{Colours.END}")
            sys.exit(1)
        with open(log_files_path, "r") as f:
            print(f"{Colours.BLUE}[*] Log files:{Colours.END}")
            print(f.read())

    elif args.grep:
        log_file = get_log_file()
        output = subprocess.check_output(["grep", "--color=NONE", f"{args.grep}", f"{log_file}"]).decode()
        print(output)


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

        check = input(f"Are you sure you want to remove the log file: {log_file}? y/N: ")

        if check.lower() != 'y':
            print(f"{Colours.RED}Aborting...{Colours.END}")
            sys.exit(0)

        if os.path.exists(log_file):
            os.remove(log_file)

        with open(log_files_path, 'r') as f:
            lines = f.readlines()

        with open(log_files_path, 'w') as f:
            lines = lines[:-1]
            lines = [line for line in lines if line.strip() != ""]
            f.writelines(lines)

        print(f"{Colours.GREEN}[*] Log deleted: {log_file}{Colours.END}")


    elif args.message:
        log_file = get_log_file()

        with open(log_file, "a") as f:
            message = " ".join(args.message)
            time = datetime.datetime.now()

            if args.success:
                message = f"{Colours.GREEN}[{time}] [S] - {message}{Colours.END}\n"
            elif args.failure:
                message = f"{Colours.RED}[{time}] [F] - {message}{Colours.END}\n"
            elif args.remember:
                message = f"{Colours.BLUE}[{time}] [REMEMBER] - {message}{Colours.END}\n"
            else:
                message = f"{Colours.BLUE}[{time}] [*] - {message}{Colours.END}\n"

            f.write(message)
            print(f"{Colours.GREEN}[+] Log message added to {log_file}.{Colours.END}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
