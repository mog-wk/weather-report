import sys, os
from pathlib import Path

import parse
from errors import InvalidParameter 

DEFAULT_DATABASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + "/logs/"

loca_save_directory = None

def match_args(args: list):
    # priority args
    args_it = iter(args)
    # arguments loop
    for arg in args_it:
        match arg:
            case "-h":
                print_help();
                sys.exit(0)
            case "--save-raw" | "--raw-save" | "-S":
                v = parse_key_arg(args_it)
                if v == None:
                    parse.save_csv(DEFAULT_DATABASE_DIRECTORY)
                else:
                    if os.path.isabs(v):
                        parse.save_csv(v)
                    else:
                        parse.save_csv(os.getcwd() + '/' + v)
                continue;
            case "--save" | "-s":
                v = parse_key_arg(args_it)
                if v == None:
                    parse.save_csv(DEFAULT_DATABASE_DIRECTORY, analyze_data=True)
                else:
                    if os.path.isabs(v):
                        parse.save_csv(v, analyze_data=True)
                    else:
                        parse.save_csv(os.getcwd() + '/' + v, analyze_data=True)
                continue;
            case "--analyze":
                print("alalyze scpt")
                continue
            case "--save_directory" | "-d":
                k, v = arg, parse_key_arg(args_it) ## TODO: Make Priority
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
