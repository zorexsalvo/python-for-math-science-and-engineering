import pytest


def tests_exercise_1():
    import exercise1


def tests_exercise_2():
    import exercise2


def test_exercise_3():
    import exercise3

def test_exercise_4():
    import exercise4
    expected_value = ['Spizikes', 'Air Force 1', 'Curry 2', 'Melo 5']

    for key, value in enumerate(expected_value):
        assert expected_value[key] == exercise4.shoes[key]


def test_exercise_5():
    import exercise5


def test_exercise_6():
    import exercise6

    expected_value = {
        "PoGo":
        "Slang for Pokemon Go",
        "Spange":
        "To collect spare change, either from couches, passerbys on the street or any numerous other ways and means",
        "Lie-Fi":
        "When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"
    }

    assert expected_value == exercise6.cooldictionary


def test_exercise_7():
    import exercise7

    years = [2010, 2014, 2018]
    make = ['Toyota', 'Mitsubishi', 'Ford']
    model = ['Vios', 'Montero', 'Everes']

    values = list(zip(years, make, model))

    for value in values:
        car = exercise7.Car(value[0], value[1], value[2])

        assert car.age() == 2019 - value[0]
