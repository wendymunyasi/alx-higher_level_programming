#!/usr/bin/python3
""" Doc """
import os, sys
import subprocess


def run_command(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return "{}{}".format(output, error)


def run_unittest():
    nb_tests = 0
    is_success = False
    try:
        res = run_command("python3 -m unittest discover tests")
        for line in res.split("\\n"):
            if "Ran " in line:
                nb_tests = int(res.split("Ran ")[-1].split(" tests")[0])
            if nb_tests > 0 and "OK" in line:
                is_success = True
    except Exception:
        nb_tests = 0
        is_success = False
    return nb_tests, is_success


# validate tests are passing by default
nb_tests, passing = run_unittest()

if nb_tests <= 0:
    print("No test found")
    exit(1)
if not passing:
    print("Regular tests are not passing")
    exit(1)

file_path_to_update = "models/rectangle.py"
file_path_updated = "models/tmp_rectangle.py"
if not os.path.exists(file_path_to_update):
    print("{} not found".format(file_path_to_update))
    exit(1)

try:
    # Move file
    if os.path.exists(file_path_updated):
        os.remove(file_path_updated)
    os.rename(file_path_to_update, file_path_updated)

    # update file
    new_content = """#!/usr/bin/python3
\"\"\" Random documentation \"\"\"
from models.tmp_rectangle import Rectangle


class Rectangle(Rectangle):
    \"\"\" Random documentation \"\"\"

    def __init__(self, width, height, x=0, y=0, id=None):
        \"\"\" Random documentation \"\"\"
        if width == 0:
            width = 1
        super().__init__(width, height, x, y, id)
"""

    with open(file_path_to_update, "w") as file:
        file.write(new_content)

    # run tests
    nb_tests, passing = run_unittest()
    if nb_tests <= 0:
        print("No test found")
    if passing:
        print("No test found for this case")
except Exception:
    print("An error occured... {}".format(sys.exc_info()[0]))

# rollback file
if os.path.exists(file_path_updated):
    if os.path.exists(file_path_to_update):
        os.remove(file_path_to_update)
    os.rename(file_path_updated, file_path_to_update)

print("OK", end="")
