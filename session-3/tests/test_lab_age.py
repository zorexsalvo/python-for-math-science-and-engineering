from unittest import mock
import pytest
import builtins


def test_lab_age():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        import lab_age
