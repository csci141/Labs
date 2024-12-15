% CSCI 141 - Lab 3
% 

## Eligibility for Office

From Wikipedia, here are the eligibility rules for running for US Representative and US Senator. I left out the third qualification requiring residency of the state in which they are running for office - we're not testing that qualification with this program.

-   Article I, Section 2 of the Constitution, sets two qualifications for representatives:

    1.  they must be at least 25 years old

    2.  they must have been a citizen of the United States for at least seven years

-   Article I, Section 3, of the Constitution, sets two qualifications for senators:

    1.  they must be at least 30 years old

    2.  they must have been a citizen of the United States for at least nine years

You will write a program that tells the user if, based on their age and years of citizenship, they are eligible to run for each house of Congress in the United States.

1. **Nested `if`s vs Boolean Operators**

   One approach to solving the problem would be to use nested if statements. You could put an if statement inside of another if statement to test two different conditions. Consider the following code snippet that uses nested if statements.

   ```python
   x = 9
   if x < 10:
      if x > 0:
         print("you entered a single digit positive number.") 
   ```

   Notice that the print statement will execute only when $x$ is less than $10$ and $x$ is greater than $0$. Also notice that I used the word "and" in the previous sentence.

   An alternative way (that is logically equivalent) to write the code segment above is:

   ```python
   x = 9
   if x < 10 and x > 0:
         print("you entered a single digit positive number.") 
   ```

   Notice the correspondence between nesting if statements and using the Boolean operator `and`.

   Using those ideas, you're going to write a program that checks to see if you're eligible to run for office.

2. **Sample Output for one person** Here a few sample runs of my program. The numbers at the end of the first two lines are entered by the user.

       Enter the age of the person. 28
       How many years have they been a citizen? 11
       They can run for Representative
    
       Enter the age of the person. 58
       How many years have they been a citizen? 22
       They can run for Senator or Representative
    
       Enter the age of the person. 19
       How many years have they been a citizen?  18
       They are not eligible to run for either office.

   For this problem, your program's output should match the sample output **exactly**.

3. Writing pseudocode is a great way to get your ideas on paper in a semi-structured way to help guide you when you write actual code. I often write pseudocode before I write Python because it helps me think through the steps I need to take before I start thinking about the details of expressing those steps in Python.

    A lot of programmers like using a whiteboard to sketch out a flowchart of the code to make sure they understand the basic flow, then they block in the parts as comments. Finally, they gradually sketch in different parts of the code, knocking off one part at a time. If this hasn’t been your process before, try it now! Future assignments will be get increasingly difficult to complete without some process for carefully breaking down your thinking about your solution approach, so it’s good to practice it on an easier assignment. 

   Here is some pseudocode I wrote for this program:

   ```
   ask for the person's age 
   ask for the person's years of citizenship
   
   if they are eligible to run for Senator, tell them
   else if they are eligible to run for Representative, tell them
   else tell them they are not eligible for either
   ```

   Notice that each line of pseudocode is (1) precise enough to translate into code and (2) simpler and easier to translate into code than the higher-level description of the problem above.

4. **Test your code** Any time you write code you should test it thoroughly. It's more important to test code carefully than simply test a lot of random cases. This program has several different outcomes: plan some test cases which would end up in each outcome. 

   In this particular example, test the program by inputting data that falls into each of the three scenarios (i.e. (1) Senator or Representative, (2) Representative, (3) neither.) You should also take a moment to convince yourself that it's impossible (and therefore you don't need to test) for a person who is eligible to be a Senator but not a Representative.

   Similar to other assignments, the easiest way to do this is to write down a list of "test cases" for various inputs and what the resultant output should be. You can then check to see if your code matches.

5. **Add a comment to your code** As usual, make sure you have a comment to the top of your code that lists your name, the date, and a short description of the program's purpose.

6. **Turn in your code to Canvas** Submit your code in a file called `representative.py` to the Lab 3 assignment on Canvas.

You've now completed Lab 3. If you need help, you can always visit office hours after your lab time.

## Rubric


This lab is worth a total of 10 points:

* 1 point: Author, date, and program description given in a comment at the top of the file
* 1 points: Code is commented adequately and variables are appropriately named
* 2 points: Code uses at least one boolean logical operator: `and`, `or`, `not`
* 2 points: Output matches exactly for someone who is eligible to run for Representative but not Senator
* 2 points: Output matches exactly for someone who is eligible for both offices
* 2 points: Output matches exactly for someone who is eligible for neither office

# Acknowledgements 

Thanks to Dr. Perry Fizzano and Dr. Caroline Hardin for developing this lab.
