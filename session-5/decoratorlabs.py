from time import sleep
from functools import wraps


def delay(seconds, repetition=1):
    output = None

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            print(f'[START] {function.__name__}')

            for i in range(repetition):
                print(i)
                print(f'Sleeping for {seconds} second(s)')
                sleep(seconds)

                output = function(*args, **kwargs)

            print(f'[END]')
            return output

        return wrapper

    return inner_function


@delay(seconds=2, repetition=3)
def say_something(word):
    print(word)


def main():
    say_something('Hello, world!')


if __name__ == '__main__':
    main()
