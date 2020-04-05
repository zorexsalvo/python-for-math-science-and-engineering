from time import sleep
import random


def get_random_number():
    return random.randint(1, 5)


def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def main():

    for i in range(5):
        seconds = get_random_number()
        delay(seconds)
        print('OK!')


if __name__ == '__main__':
    main()
