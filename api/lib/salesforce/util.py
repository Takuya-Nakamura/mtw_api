from pprint import pprint as p
import sys


def check_args(args, count):
    if len(args) <= count:
        p("invalid parameter")
        sys.exit(0)

