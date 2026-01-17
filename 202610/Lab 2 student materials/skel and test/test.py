# Nicholas J Uhlhorn
# April 2025
# Auto grader for Lab 2, based on early POTD tests
# Updated January 2026 by Caroline Hardin to add in money translator
# Updated 1/13/26 to fix some minor typos by Joshua Kelley
# Updated 1/15/26 to fix test bugs - Eric Furukawa

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
    
    assert abs(float(out.split(' ')[-1]) - float(answer)) < .0000001


@pytest.mark.parametrize("name,net,donation,avgnet,answer", [
    ("Alice", 1, 100, 100000,"$100.00 donation for someone with a net worth of $1,000,000.00 is the same as a $8.57 donation for someone with a net worth of $100,000.00"),
    ("Old Aunt Sue", .2, 1000, 80000,"$1,000.00 donation for someone with a net worth of $200,000.00 is the same as a $349.06 donation for someone with a net worth of $80,000.00"),
    ("Jeff", 240000, 5000000, 40000,"$5,000,000.00 donation for someone with a net worth of $240,000,000,000.00 is the same as a $0.51 donation for someone with a net worth of $40,000.00"),
   
])

def test_money(name,net,donation,avgnet,answer):
    '''Tests the output of money_translator.py on different number combos'''
    out, err, code = run_file('money_translator.py', f'{name}\n{net}\n{donation}\n{avgnet}')

    assert err == ''

    assert answer in out

pytest.main(["test.py", "-vv", "--showlocals", "-p", "no:faulthandler"])
