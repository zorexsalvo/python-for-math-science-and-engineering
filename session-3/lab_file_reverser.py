import argparse
import sys

# create an instance of ArgumentParser without any arguments

parser = argparse.ArgumentParser()

# user the add_argumnent method to specify a positional argument called
# filename and provide some help text using help argument.

parser.add_argument('filename', help='the file to read')

# add a --limit flag
# - to specifiy that an argument is a flag, we need to place to hyphens at the
# beginning of the flags name.
# - we specified a shorter version of the flag as our second argument
# - we used the type option for add_argument to state that we want the value
# converted to an integer

parser.add_argument('--limit',
                    '-l',
                    type=int,
                    help='the number of lines to read')

# add a --version flag
# - use the action option to specify a string to print out when this flag is
# received
parser.add_argument('--version',
                    '-v',
                    action='version',
                    version='%(prog)s 1.0')

# tell the parser to parse the arguments from stdin using the parse_args method
# and store the parsed arguments as to the variable args

args = parser.parse_args()

# add the actual business logic for reversing the contents of the file

# We utitlize the try statement to denote that it's quite possible for an error
# to happen within the try block

try:
    f = open(args.filename)
    limit = args.limit

# We can handle specific types of errors using the except keyword (we can have
# more than one).
except FileNotFoundError as err:
    print(f'Error: {err}')
    # set exit status to 1 to indicate error
    sys.exit(1)

# If there isn't an error, we want to carry out the code that is in the else
# block.
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])
