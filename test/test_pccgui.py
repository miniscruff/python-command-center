import pccgui
import os
from unittest.mock import patch, call
from contextlib import contextmanager


@patch('pccgui.print')
def test_print_header_contains_lines(mock_print):
    pccgui.print_header('a simple line')
    calls = [
        call('╔═══════════════╗'),
        call('║ a simple line ║'),
        call('╚═══════════════╝'),
    ]
    assert mock_print.call_args_list == calls


@patch('pccgui.Popen')
def test_script_wrapper_would_start_process_with_a_list(mock_popen):
    wrapper = pccgui.script_wrapper('command list')
    wrapper()
    mock_popen.called_with_args(['command', 'list'])
