import pcc
import os
from unittest.mock import patch, call
from contextlib import contextmanager


@contextmanager
def temp_file(file_path, file_text):
    with open(file_path, 'w') as f:
        f.write(file_text)
    yield f
    os.remove(file_path)


def test_load_scripts_returns_none_if_no_pcc_or_package():
    assert pcc.load_scripts() is None


def test_load_scripts_returns_data_from_pcc_json():
    write_scripts = """{"demo": "pytest"}"""
    with temp_file('pcc.json', write_scripts):
        scripts = pcc.load_scripts()
    assert scripts['demo'] == 'pytest'


def test_load_scripts_returns_data_from_package_json():
    write_scripts = """{"scripts": {"demo": "pytest"}}"""
    with temp_file('package.json', write_scripts):
        scripts = pcc.load_scripts()
    assert scripts['demo'] == 'pytest'


@patch('pcc.print')
def test_print_header_contains_lines(mock_print):
    pcc.print_header(['first line', 'second line'])
    calls = [
        call('╔═════════════╗'),
        call('║ first line  ║'),
        call('║ second line ║'),
        call('╚═════════════╝'),
    ]
    assert mock_print.call_args_list == calls
