

def sample_decorator(target_function):
    return target_function

@sample_decorator
def some_function():
    print('some_function')


def main():
    some_function()


if __name__ == '__main__':
    main()
