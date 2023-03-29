import time
import os
import json
from subprocess import Popen, PIPE


def on_click(battmo_dict=None):
    print('######## CLICKED')
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_name = "battmo_input.json"
    new_file_path = os.path.join(current_path, file_name)

    json.dump(battmo_dict, open(new_file_path, "w"), indent=3)
    execute_matlab_script()


def execute_matlab_script():
    command_line = [
        'matlab',
        "-wait",
        '-r',
        "cd Documents/code/testBattmo/matlab ; test_script(); exit"
    ]

    start = time.time()

    process = Popen(command_line, stdout=PIPE, stderr=PIPE, shell=True)
    print("delay", round(time.time() - start, 2), "s")

    stdout, stderr = process.communicate()
    print("delay stdout", round(time.time() - start, 2), "s")

    print("\nOUT", stdout)
    print("ERR", stderr)
    print('######## END OF CLICKED\n')
