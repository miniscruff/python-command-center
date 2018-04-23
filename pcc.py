import subprocess
import sys
import os
import json
from tkinter import Tk, Button


def load_scripts():
    if os.path.isfile('pcc.json'):
        with open('pcc.json') as f:
            return json.load(f)

    if os.path.isfile('package.json'):
        with open('package.json') as f:
            return json.load(f)['scripts']


SCRIPTS = load_scripts()
settings = {}
# convert --arg=value as settings
# convert arg=value as extra scripts
for arg in sys.argv[1:]:
    split = arg.split('=')
    key = split[0]
    if key.startswith('--'):
        settings[key[2:]] = split[1]
    else:
        SCRIPTS[key] = split[1]


def print_header(lines):
    max_length = max(len(x) for x in lines) + 1
    lines = [x.ljust(max_length) for x in lines]
    bars = '\u2550' * (max_length+2)
    print(''.join(['\u2554', bars, '\u2557']))
    for line in lines:
        print(' '.join(['\u2551', line, '\u2551']))
    print(''.join(['\u255A', bars, '\u255D']))


def script_wrapper(script_key):
    def execute_script():
        script_com = SCRIPTS[script_key]
        print_header(['Running ' + script_key, '> ' + script_com])
        subprocess.Popen(script_com.split(' '))
    return execute_script


columns = int(settings['col']) if 'col' in settings else 8

root = Tk()
root.title('Python Command Center')
button_settings = dict(ipadx=5, ipady=5, padx=3, pady=3, sticky='EW')
for i, key in enumerate(SCRIPTS):
    button = Button(root, text=key, command=script_wrapper(key))
    button.grid(row=i // columns, column=i % columns, **button_settings)
root.mainloop()
