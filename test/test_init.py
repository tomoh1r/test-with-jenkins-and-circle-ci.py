import os

from flake8.main import cli


def test_version(ex4mple):
    assert ex4mple.__version__ == '1.0.0'


def test_flake8():
    _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for dname in ['ex4mple', 'test']:
        try:
            cli.main([os.path.join(_root, dname)])
        except SystemExit as exc:
            if exc.code != 0:
                raise
