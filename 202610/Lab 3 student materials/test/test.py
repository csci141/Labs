# Nicholas J Uhlhorn
# April 2025
# Auto grader for Lab 3, based on early POTD tests
# Scott Werwein | CSCI 141 | Spring 2025

import pytest
import fnmatch
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


@pytest.mark.parametrize("a,b,c, q1, q2", [
    (1,0,-4, "2.0", "-2.0"), 
    (1,1,-4, "1.56155", '-2.5615'),
    (1,1,1, "*no*real*roots*", ""),
    (0,1,10, "*a*is*zero*", ""),
    (-2,1,10, "-2.0", "2.5"),
])
def test_a(a,b,c,q1,q2):
    '''Tests the output of lab1A.py to see it contains the correct name and length'''
    out, err, code = run_file('quadratic.py', '', str(a), str(b), str(c))

    assert err == '' 

    assert q1 in out or fnmatch.fnmatch(out, q1)

    if q2 != '':
        assert q2 in out or fnmatch.fnmatch(out, q2)


@pytest.mark.parametrize("age, residency", [
    (28, 11),
    (58, 22),
    (19, 18),
])
def test_b(age, residency):
    '''Tests the output of lab1B.py on different numbers'''
    out, err, code = run_file('representative.py', f'{age}\n{residency}')
    out = out.lower()

    assert err == ''

    if age >= 30 and residency >= 9:
        assert "senator" in out and "representative" in out
    elif age > 25 and residency >- 7:
        assert "representative" in out
    else:
        assert "not" in out

pytest.main(["test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])
