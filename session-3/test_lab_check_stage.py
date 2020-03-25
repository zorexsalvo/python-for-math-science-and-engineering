import os
from unittest import mock

STAGES = {
    'DEV': 'We\'re running in {}',
    'PRODUCTION': 'DANGER!!! - We\'re running in {}'
}


def test_lab_check_stage(capsys):
    stage = 'DEV'

    with mock.patch.object(os, 'getenv', lambda x, y: stage):
        import lab_check_stage
        captured = capsys.readouterr()

        assert STAGES[stage].format(stage) == captured.out.strip()
