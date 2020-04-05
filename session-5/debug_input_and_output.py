from IPython import embed
from functools import wraps


def debug_input_and_output(function):
    output = None

    def wrapper(*args, **kwargs):
        print(f'[INPUT] ARGS: {args}')
        print(f'[INPUT] KWARGS: {kwargs}')

        output = function(*args, **kwargs)
        return output

    return wrapper


@debug_input_and_output
def say_something(word):
    print(word)


def main():
    say_something('Test')


if __name__ == '__main__':
    main()
