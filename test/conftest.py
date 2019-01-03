from importlib import import_module

import pytest


@pytest.fixture
def ex4mple():
    return import_module('ex4mple')
