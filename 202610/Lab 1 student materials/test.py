# Nicholas J Uhlhorn
# April 2025
# Auto grader for Lab 1, based on early POTD tests
# Scott Werwein | CSCI 141 | Spring 2025

import pytest
import subprocess
import sys

def run_file(file, program_input, *args):
    ''' runs an external python program:    file
        with command line arguments:        args
        then gives user input:              program_input
    '''
    execution_array = [sys.executable, file]
    if args != None:
        execution_array.extend(args)

    print("execution array:", execution_array)
    print("input:", program_input)

    process = subprocess.Popen(
        execution_array,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr, = process.communicate(input=program_input)
    return stdout.strip(), stderr, process.returncode


@pytest.mark.parametrize("name", [
    ('Scott'),
    ('Alex'),
    ('Tom'),
    ('Callie'),
    ('Greg'),
    ('Richard'),
    ('Tommy'),
    ('Wishbone')
])
def test_a(name):
    '''Tests the output of lab1A.py to see it contains the correct name and length'''
    name_length_str = ' ' + str(len(name)) + ' '
    out, err, code = run_file('lab1A.py', (name+'\n'))

    assert err == '' 

    assert name in out
    assert name_length_str in out


@pytest.mark.parametrize("num", [
    (3), (-3), (0)
])
def test_b(num):
    '''Tests the output of lab1B.py on different numbers'''
    out, err, code = run_file('lab1B.py', '', str(num))

    assert err == ''

    try:
        assert int(out) == (num + 3)
    except:
        pass

@pytest.mark.parametrize("num_a,num_b", [
    (1, 1),
    (1, -1),
    (-1, 4),
    (0, 0),
])
def test_c(num_a, num_b):
    '''Tests the output of lab1C.py on different number combos'''
    out, err, code = run_file('lab1C.py', '', str(num_a), str(num_b))

    assert err == ''

    try:
        assert int(out) == (num_a + num_b)
    except:
        pass

pytest.main(["test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])

