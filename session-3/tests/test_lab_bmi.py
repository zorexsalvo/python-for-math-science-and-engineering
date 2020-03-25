from unittest import mock

import builtins
import pytest
import random


@mock.patch.object(builtins, 'input', lambda _: '1.0')
def test_gather_info():
    from lab_bmi import gather_info

    unit_of_measurements = ['metric', 'imperial']

    with mock.patch('lab_bmi.gather_info') as mock_gather_info:
        mock_gather_info.return_value = (random.uniform(1.0, 7.0),
                                         random.uniform(20.0, 100.0),
                                         random.choice(unit_of_measurements))

        height, weight, system = gather_info()

        assert type(height) == float
        assert type(weight) == float
        assert type(system) == str
        assert type(gather_info()) == tuple


def test_calculate_bmi():
    from lab_bmi import calculate_bmi

    expected_payload = [{
        'height': 1.65,
        'weight': 65.5,
        'system': 'metric',
        'bmi': 65.5 / 1.65**2
    }, {
        'height': 5.6,
        'weight': 140.0,
        'system': 'imperial',
        'bmi': 703 * (140.0 / 5.6**2)
    }]

    for payload in expected_payload:
        bmi = calculate_bmi(**payload)
        assert payload['bmi'] == bmi


def test_main():
    from lab_bmi import main

    unit_of_measurements = ['metric', 'imperial']

    for system in unit_of_measurements:
        with mock.patch('lab_bmi.gather_info') as mock_gather_info:
            mock_gather_info.return_value = (random.uniform(1.0, 7.0),
                                             random.uniform(20.0,
                                                            100.0), system)
            main()
