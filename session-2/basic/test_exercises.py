import pytest
import sys

from contextlib import contextmanager
from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def tests_exercise_1():
    import exercise1
    expected_value = "Hi my name is Julie and I am 42 years old"
    assert expected_value == exercise1.sentence


def tests_exercise_2():

    with captured_output() as (out, err):
        import exercise2

    output = out.getvalue().strip()
    assert exercise2.uhm_hello == output


def test_exercise_3():
    import exercise3
    test_data = [('ph', 'phphph'), ('python', 'pythonpythonpython'),
                 ('5', '555')]

    for data in test_data:
        with captured_output() as (out, err):
            exercise3.tripleprint(data[0])
            output = out.getvalue().strip()
            assert data[1] == output


def test_exercise_4():
    import exercise4
    expected_value = ['Spizikes', 'Air Force 1', 'Curry 2', 'Melo 5']

    for key, value in enumerate(expected_value):
        assert expected_value[key] == exercise4.shoes[key]


def test_exercise_5():

    with captured_output() as (out, err):
        import exercise5
        output = out.getvalue().strip()

        for number in output.split('\n'):
            assert int(number) > 90


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
