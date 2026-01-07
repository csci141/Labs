import os
import re
import sys
import time
import select
import psutil
import difflib
import subprocess
from typing import List, Tuple
import pandas as pd

import shutil


RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
ENDC = "\033[0m"

TIME_EPSILON = 0.02

def test_program(shell) -> str | None:
    """Give a shell whose current working directory is in the student's submission
    directory, test that the student's code produces the correct output.

    Returns None unless there was an issue, in which case returns a string describing the problem.
    """

    result = ""

    # Grade triangle
    output = ""
    for i in range(5):
        shell.command(f"python3 triangle.py {i}")
        output += shell.read(timeout=0.5).strip() +"\n\n"
    
    expected = """

               *
               
               *
               **
               *
               
               *
               **
               ***
               **
               *
               
               *
               **
               ***
               ****
               ***
               **
               *
               
               """.replace(" ", "")

    if output != expected:
        result += f"{RED}Triangle failed:{ENDC}\n"
        result += f"\t{BLUE}Expected{ENDC}:\n\t" + expected.replace("\n", "\n\t\t")
        result += f"\n\t{BLUE}Output{ENDC}:\n\t" + output.replace("\n", "\n\t\t")
    

    # Grade turtledraw

    shell.command(f"python3 turtledraw.py")
    print("\t\tShowing turtledraw")
    issues = input("\t\tAny issues? Leave blank if none: ")
    

    if issues != "":
        result += f"{RED}Turtledraw failed:{ENDC}\n"
        result += "\t" + issues

    shell.kill_children()
    if result == "":
        return None
    else:
        return result


def grade_students(students) -> dict:
    student_notes = {}

    for student in students:
        print("\t", student)
        # student_notes[student] = grade_student(student)
        try:
            student_notes[student] = grade_student(student)
        except Exception as e:
            print(f"Error grading {RED + student + ENDC}: {e}")
            student_notes[student] = f"{RED}Error grading student{ENDC}"

    return student_notes


def grade_student(student) -> dict:
    notes = None
    with Shell(f"./sorted/{student}", wait=TIME_EPSILON) as shell:
        result = test_program(shell)
        if result:
            notes = result
        else:
            notes = "Good"
    return notes


def collect_student_names(filename: str) -> List[str]:
    """
    Collect the student names from the CSV file and prepare it for
    organize_files, so that we only make directories for the students
    we intend to grade.
    """
    df = pd.read_csv(filename)
    names = [name for name in df["Student"].tolist() if isinstance(name, str)]


    names.remove("    Points Possible")
    names.remove("Student, Test")

    new_names = []
    for name in names:
        name = name.replace(" ", "").lower()
        name = name.replace(",", "")
        if "-" in name:
            name = name.replace("-", "")
        new_names.append(name)
    
    return new_names



def organize_files(students: None):

    canvas_file_pattern = r"([a-z]+)_(?:LATE_){0,1}\d+_\d+_(.+)"

    # Clean files in sorted
    print("Creating Sorted Directory...")
    shutil.rmtree("./sorted", ignore_errors=True)
    os.mkdir("./sorted")

    # Get all files
    print("Getting all files...")
    files = os.listdir("./submissions")

    # Group files by student
    print("Grouping files by student...")
    student_files = {}
    for file in files:
        if file == "":
            continue

        match = re.match(canvas_file_pattern, file)
        if match is not None:
            name = match.group(1)
            file = match.group(0)

            if students is not None and name not in students:
                continue

            if name not in student_files.keys():
                student_files[name] = [file]
            else:
                student_files[name].append(file)

    # Copy each student's files to the sorted directory in a directory named after the student
    print("Copying/Renaming files to sorted directory...")
    for student, files in student_files.items():
        if students is not None and student not in students:
                continue
        print(f"\t{student}")
        os.mkdir(f"./sorted/{student}")
        for file in files:
            # Extract the filename
            match = re.match(canvas_file_pattern, file)
            dest_file = match.group(2)

            # Replace `-n` for canvas resubmissions
            dest_file = re.sub(r"-\d+.", ".", dest_file) 
            
            # Copy the file over
            shutil.copyfile(f"./submissions/{file}", f"./sorted/{student}/{dest_file}")
        
    if students is not None:
        return students
    
    else:
        return student_files.keys() 


class Shell:
    """A handle for interacting with a shell."""

    def __init__(self, dir="./", wait=None):
        if not os.path.exists(dir):
            raise FileNotFoundError(f'The directory "{dir}" does not exist!')

        self.process = subprocess.Popen(
            "/bin/bash",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        self.command(f"cd {dir}")

        self.default_wait = wait

    def command(self, command):
        if self.process.poll() is not None:
            raise RuntimeError("Shell process is not running.")
        self.process.stdin.write(f"{command}\n")
        self.process.stdin.flush()

    def read(self, wait=None, timeout=None):
        if wait is None and self.default_wait is not None:
            time.sleep(self.default_wait)
        elif wait is not None:
            time.sleep(wait)

        start_time = time.time()
        data = ""
        while True:
            rlist, _, _ = select.select([self.process.stdout], [], [], TIME_EPSILON)

            if rlist:
                try:
                    chunk = os.read(self.process.stdout.fileno(), 1024).decode("utf-8")
                    if not chunk:
                        break
                    data += chunk
                except BlockingIOError:
                    continue
            else:
                break
            
            if timeout is not None and  time.time() - start_time > timeout:
                    break
        return data

    def flush(self):
        self.read()

    def close(self):
        self.process.terminate()
        self.process.wait()

    def kill_children(self):
        # Terminate any child processes spawned by this shell (like Python/turtle)
        parent = psutil.Process(self.process.pid)
        for child in parent.children(recursive=True):
            child.kill()

    def kill(self):
        self.process.kill()
        self.process.wait()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def main():
    if len(sys.argv) > 1:
        students = collect_student_names(sys.argv[1])
    else:
        students = None

    students = organize_files(students)

    print("Grading Students...")
    notes = grade_students(students)

    with open("results.txt", "w+") as f:
        for student in students:
            f.write(f"{student:-^80}\n\t")
            if student in notes.keys():
                f.write(notes[student].replace("\n", "\n\t"))
            else:
                f.write(f"{RED}Error grading student{ENDC}")
            f.write("\n\n")


if __name__ == "__main__":
    main()
