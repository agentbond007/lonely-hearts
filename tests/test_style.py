import subprocess


def test_flake8():
    exit_status = subprocess.call(['flake8', '--exclude=venv/*,hearts/api/__init__.py'])
    assert exit_status == 0


def test_pylint():
    exit_status = subprocess.call(['pylint', '-E', '--rcfile', '.pylintrc', 'hearts'])
    assert exit_status == 0
