import sys, os
from pathlib import Path

import parse
from errors import InvalidParameter 

DEFAULT_DATABASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + "/logs/"

def match_args(args: list):
    args_it = iter(args)
    for arg in args_it:
        match arg:
            case "-h":
                print_help();
                sys.exit(0)
            case "--raw-save" | "-S":
                v = parse_key_arg(args_it)
                if v == None:
                    parse.add_csv_row(DEFAULT_DATABASE_DIRECTORY)
                else:
                    if os.path.isabs(v):
                        parse.add_csv_row(v)
                    else:
                        parse.add_csv_row(os.getcwd() + '/' + v)

                continue;
            case "--save":
                print("save test...")
                continue;
            case "--analyze":
                print("alalyze scpt")
                continue
            case "--save_directory" | "-d":
                k, v = arg, parse_key_arg(args_it)
                continue
            case _:
                print(f"Invalid parameter: {arg}")

def parse_key_arg(arg):
    try:
        parameter = arg.__next__()
        if parameter.startswith("-"):
            raise KeyError
        return parameter
    except KeyError:
        InvalidParameter.consume()
    except StopIteration:
        return None

def print_help():
    print(
            "-S <PATH>\traw save",
            "--raw-save <PATH>\traw save",
            sep='\n')


if __name__ == "__main__":
    match_args(sys.argv[1:])
