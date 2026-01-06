% CSCI 141 - Lab 2
% Scott Wehrwein
% Fall 2025

##### Goals

* Become familiar with the basics of navigating the Linux command line
* Know how to run a Python program on the command line, including passing command line arguments
* Begin thinking about readability and making judicious use of comments
* Write two slightly larger, nontrivial programs

## Overview

This lab introduces you to the Linux command line, commenting and coding style, and asks you to write two slightly more involved programs. Upload your submission to Canvas before the deadline. If you have questions, be sure to ask the TA. Ask questions often. Labs are your opportunity to get personalized help!

## Linux Command Line Basics

**Important:** Follow the steps below, and feel free to explore further in the process. At the end of this section, you will show your terminal to the TA to demonstrate that you have completed these steps.

Windows, Mac OS, and Linux all provide graphical interfaces such as those you're used to using, that allow you to open programs and accomplish tasks using the mouse, icons, windows, and so on. All of these operating systems also provide another way of interacting with them, called a *Command Line Interface* (CLI). Although there is a steeper learning curve for knowing how to accomplish things using the command line, for certain tasks it can be more powerful once you know how to use it.

In this lab, you will learn the very basic elements of how to interact with the Linux command line and learn how to run Python code without the help of an IDE such as Thonny. What you will learn here is only a tiny fraction of the commands available; you can find a helpful \"cheat sheet\" of many commonly used Linux commands [here](linuxref.pdf) if you'd like to learn more.

1. Begin by opening a command line window (also called a Terminal). Click on the App icon in the lower left corner and type terminal to initiate a search; click on the Terminal icon from the results to launch a new terminal window. You can also quickly open a terminal by presing Ctrl+Alt+T.

2. In the terminal, you'll see a **prompt** that ends with a `$` sign. This is called the command line, or command prompt; you'll type commands here to interact with the system. Commands that you issue are interpreted by a program called a shell. The default shell, or command line language on the lab machines  is called `bash`; it is one of the many shells available in Linux.

3. You’ll notice that the `$` is prepended with your username and an `@` followed by the name of the computer that you are logged into. For example, `wehrwes@cf162-03:~$` specifies the user `wehrwes` logged into the `cf162-03` machine.

4. Anything you can do with the mouse when interacting with a windows environment you can also accomplish via the command line. In the following steps you will create a new directory (folder), navigate into that folder, and run a Python file, using only the command line. For these instructions, code and/or sample file content or output are displayed in code blocks like the one below. Type commands EXACTLY as they provided, and press return/enter to issue the command. For example:

   ```
   whoami
   ```

   is instructing you to type the command `whoami` on the command line and execute it by pressing return/enter. Try it out. What does this command do?

5. The terminal keeps track of a "working directory". When you open a fresh terminal, this is your home directory. You can see the current working directory with the `pwd` command (the "p" stands for "present"):

   ```
   pwd
   ```

   For me, this command outputs `/home/wehrwes`, my home directory.

6. List the files in your home directory with the `ls` (short for "list") command. Check to make sure your `csci141` folder from Lab 1 is there.

7. Commands can take arguments, similarly to how functions in Python take arguments, except here they are not surrounded by parentheses. Let's move into your `csci141` directory using the `cd` (short for "change directory") command:

   ````
   cd csci141
   ````

   You can now verify with `pwd` that you've moved into (in my case) `/home/<your_username>/csci141`.

8. Use `ls` to confirm that this directory has your `lab1` folder from Lab 1 in it.

9. Let's create a`lab2` folder. To create a directory, use the `mkdir` command with a single argument that is the name of the directory (folder) that you want to make. Create the directory `lab2`:

   ```
   mkdir lab2
   ```

10. Confirm that you have made your directory using `ls`. Now, `lab1` and, `lab2` should be there.

11. Enter the `lab2` directory:

    ```
    cd lab2
    ```

12. Use the `cp` (short for "copy") command to copy your `lab1C.py` program from your `lab1` folder into your `lab2` folder:

    ```
    cp ../lab1/lab1C.py .
    ```

    A few things to notice here:

    * `../` means "the parent directory of the current one"
    * `.` means "the current directory"

13. Moving or renaming files are done using the same command - `mv`. Let's rename the copy of `lab1C.py` in the `lab2` folder to `adder.py`:

    ```
    mv lab1C.py adder.py
    ```

14. Print out the contents of `adder.py` with the `cat` command:

    ```
    cat adder.py
    ```

15. Just as you can run a Python program using Thonny by pressing the green Run button, you can also run a program from the command line. In the terminal window (make sure you are in your `lab2` folder, which contains your Python program), run the `adder.py` program by invoking the python interpreter, with the command line arguments after the name of the program:

    ```
    python3 adder.py 10 2
    ```

    You should see the output of your program (ideally `12`) printed out to the terminal. 

16. **This step is a part of the grade for this lab.** Get your TA to confirm that you've successfully run your program from the command line. If you weren't able to do this during the lab period, take a screenshot of your terminal window and submit it with your other code files for Lab 2. You can take a screenshot using the screenshot button (camera icon) in the system menu at the top right of the screen.

## Commenting and Code Style

It's important to write code that is as **readable** as possible. Good style choices and judicious use of comments can help a reader understand your code. More often than you'd think, that reader is you! You'll get a better feel for good style as you gain experience, but here are some guidelines to get you started:

- Include a comment with the author, date, and a short description at the top of each .py file
- Don't try to accomplish too many things in a single line
- Find a balance between overly verbose code (i.e., unneccessarily long) and code that is so short as to be cryptic
- Use white space (blank lines) to chunk your code into logical sections
- Within your code, include comments when it helps with readability; for example,
  - Sometimes, it helps to have a comment for each logical section of code explaining its overall purpose
  - Sometimes, a line is particularly non-obvious and it's worth a comment explaining what it does and why

These rules are quite subjective and you'll need more experience before you can apply them well. For now, keep these things in mind, do your best, and feel free to ask for advice from more experienced programmers.

For all the labs in this course, commenting and code style is a portion of the rubric. With the exception of requiring the Author/Date/Description comment at the top, we will only take points off for fairly severe style issues.

## Broken Calculator

To help you practice your understanding of operators and operands, in this section you will solve the following programming problem: **The period key on your keyboard is broken, but you would like to multiply two numbers with a decimal digit.**

Let's look at an example of how this could work before we start writing any code. Suppose you want to calculate $20.4 \times 17.7$, but can only enter $204$ and $177$. The desired result is $361.08$. If the user inputs the values 204 and 177, how can you convert them to 20.4 and 17.7? By using the modulo and integer division operators! For example, 204 modulus 10 has a remainder of 4, which gives the decimal value .4, while 204 integer division 10 gives 20, which is the number before the decimal in 20.4.

**The Math:** Suppose that for the input values 204 and 177 you have successfully extracted the whole and decimal values (i.e., 20, 4, 17 and 7). How can you calculate the result of 20.4 x 17.7? Multiplication of decimal values requires you to sum the following four parts:

-   The first integer times the second integer

-   The first integer times the second decimal

-   The first decimal times the second integer

-   The first decimal times the second decimal

Notice that for each decimal, we also multiply in a factor of 0.1 to make sure that it is correctly weighted in the final product. In our example, the calculation looks like this: 
$$
\begin{align}
20.4 * 17.7 &=  (20*17)\\
              &+  (20 * 7 * 0.1)\\
              &+  (4 * 0.1 * 17)\\
              &+  (4 * 0.1 * 7 * 0.1)\\
              &=  340 + 14 + 6.8 + 0.28\\
              &= 361.08 
\end{align}
$$

1.  Download [broken_calculator.py](broken_calculator.py)  and save it to your `lab2` folder.

2.  That file is incomplete. Only two lines of code have been written, which you are not allowed to edit. The rest are comments. Lines of code that say `# COMPLETE THE CODE` you will need to write. Read the comments for each section to get a sense of what code you need to write. Also, the number of COMPLETE THE CODE comments in that file is how many lines of python code I wrote in my solution. It's okay if your solution uses fewer lines of code, or more, but each block of code should accomplish what the comment above it specifies.

    **For the lines of code that you write, you are only allowed to use the `print` function, the assignment operator, and the following mathematical operators. You may not use `float()`, nor `int()`, or `/`.**

    -   `//`

    -   `%`

    -   `*`

    -   $+$

3.  There are 7 parts to the code, labeled A through G. Here are hints for each of them:

    -   **A:** This requires a single use of the print function

    -   **B:** Use only the `//` and `%` operators. Follow the logic in the description above

    -   **C:** This requires a single use of the print function

    -   **D:** Do the same for the second integer as you did for the first integer (step B). Use only the `//` and `%`operators

    -   **E:** The same as step C, but for the second integer

    -   **F:** Use the Hint above for explanation on how to do this

    -   **G:** This requires a single use of the print function.

**In your python code, you CAN make use of periods, but when the program is RUN, the user CAN ONLY enter integer (non decimal) numbers.**

Here's a sample run of the completed code:

![Correct Calculator Output](fixed_calc.png)

## Mortgage Calculator

Many online real estate websites have mortgage calculator features[^1]. These calculators ask for some information, such as the price of a home, the down payment (amount of the home price you'd pay up front), and the interest rate, then calculate the amount you'd have to pay monthly on a loan for the home.

The formula used to calculate the monthly payment based on these inputs is as follows:

$$
M = (P-D) \frac{r (1 + r)^N}{(1+r)^N - 1}
$$

Where: $$\begin{aligned}
  M &= \mbox{The monthly payment}\\
  P &= \mbox{The price of the home}\\
  D &= \mbox{The down payment amount}\\
  N &= \mbox{The number of months over which the loan will be paid off}\\
  r &= R*.01/12 \mbox{, the monthly interest rate (the yearly percentage converted to a decimal and divided by 12)}\\
\end{aligned}$$

Write a program called `mortgage.py` that takes command line arguments for $P, D, N,$ and $R$ (in that order), and outputs the monthly payment amount $M$. Notice that the user enters $R$, the annual interest rate as a percentage (e.g., 3.7), but the formula uses $r$, the monthly interest rate (e.g., 0.00308).

Here's a sample invocation of the program:

![](mortgage_noninteractive.png)

#### Test Cases

You can check your program's correctness by making sure it matches the output for the test cases in the table below. For brevity, the output is truncated after 3 decimal places in the table below; your program will output more decimal places (as in the example invocation).

|     $P$   |   $D$  | $N$ |  $R$  | Output ($M$) |
| ----- | ------ | ----- | ---- | --------- |
|   100000  | 20000  | 360 |  3.7  | 368.226      |
|   1000000 | 10     | 180 |  3.4  | 7099.747     |
|   549050  | 103200 | 800 |  5.1  | 1960.773     |

## Submission

Upload the following files to Canvas:

-   `broken_calculator.py` 

-   `mortgage.py`

-   (if the TA has not checked in lab already) A screenshot showing your terminal window having run `adder.py` from your `lab2` directory using the command line.


## Rubric

This lab is graded out of a total of 10 points:

* 2 points: you successfully ran your renamed `adder.py` program from Lab 1 from the Linux command line
* 3 points: `broken_calculator.py` works as expected while only using the `%`, `//`, $+$ and $*$ operators
* 3 points: `mortgage.py` produces the correct output
* 2 points: Both files have a comment at the top and follow good coding practices

[^1]: See <https://www.zillow.com/mortgage-calculator/> for an example
