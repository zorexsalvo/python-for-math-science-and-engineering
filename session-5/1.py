from time import sleep

def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def main():
    print('a')
    delay(seconds=3)
    print('b')


if __name__ == '__main__':
    main()
