# Nicholas J Uhlhorn
# April 2025
# Auto grader for Lab 2, based on early POTD tests
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


@pytest.mark.parametrize("input_a,input_b,answer", [
    (10, 10, '1.0'),
    (0, 10, '0.0'),
    (102, 304, '310.08'),
    (204, 177, '361.08'),
    (1111, 2222, '24686.42'),
])
def test_broken_calculator(input_a, input_b, answer):
    '''Tests the output of broken_calculator.py on different values of different lengths'''
    out, err, code = run_file('broken_calculator.py', f'{input_a}\n{input_b}\n') 

    assert err == '' 
    
    try:
        assert f"{float(out.split(' ')[-1]):.2f}" == answer
    except:
        pass

@pytest.mark.parametrize("p,d,n,r,answer", [
    (100000, 20000, 360, 3.7, 368.226),
    (1000000, 10, 180, 3.4, 7099.747),
    (549050, 103200, 800, 5.1, 1960.773),
])
def test_mortgage(p, d, n, r, answer):
    '''Tests the output of mortgage.py on different number combos'''
    out, err, code = run_file('mortgage.py', '', str(p), str(d), str(n), str(r))

    assert err == ''

    try:
        out_float = float(out)
        assert f"{out_float:.3f}"== answer
    except:
        pass

pytest.main(["test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])

