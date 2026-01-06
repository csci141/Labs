% CSCI 141 - Lab 7
% Scott Wehrwein
% Fall 2025

**Goals**

* Practice with lists, dictionaries, and file I/O
* Get experience processing data in a real-world context

## Introduction

In this lab, you'll write a program to read historical earthquake data from a file and plot each earthquake on a map using turtle graphics. An example output is shown here:


![The output from my solution code. ](correct_output.png)

## Setup

Create a `lab7` directory in your lab environment of choice. Download the following files from the course webpage and place them in your lab7 folder:

-   [plot_earthquakes.py](plot_earthquakes.py) - this file contains skeleton code and pseudocode

-   [earthquakes.csv](earthquakes.csv) - this file contains the data you'll be reading

-   [earth.png](earth.png) - this will be set as the background image in the turtle graphics canvas (this is done for you by the `turtle_setup` function given in the skeleton code).

## Approach and Guidelines

Your main tasks are as follows. Follow the same coding style conventions we've been using up to this point: comment at the top, good variable naming, and so on.

* Implement the `parse_row` function to read an earthquake record into a dictionary
* Impelement the `get_max_magnitude` function to find the largest magnitude over all the earthquakes
* Implement the remainder of the `main` function according to the pseudocode included in comment

You'll find that you need many of the structures and concepts we've covered in this course to complete this task - ask your TA if you encounter any problems, and use this opportunity to take note of any topics you need to brush up on before the final exam. You may find it helpful to create some additional helper functions to handle subtasks of the main program and keep the code manageable.

Some hints:

-   The algorithm given in the pseudocode reads each line of the CSV file into a dictionary, appending each dictionary to a list. Each dictionary has the same four keys, corresponding to the column headers; its values are the values for those columns in the given row. This gets us a list of earthquake records whose properties can be accessed by name, (e.g., `quakes[3]["magnitude"]` would give the magnitude of the fourth earthquake in the CSV file, assuming you called the list `quakes`).

-   The first line of the file contains column headers, so you'll need to skip over it before starting to read data.

-   Plotting earthquakes on the map is quite simple: the map image (and turtle canvas) is 720x360 pixels, with (0,0) in the center. Longitude (the $x$ axis) goes from -180 to 180 and latitude ($y$ axis) goes from -90 to 90, so (0,0) is in the center. To get the canvas $(x, y)$ coordinates based on a given (lon, lat) coordinate, simply multiply each coordinate by 2.

-   The skeleton includes an implementation of the `teleport` function from Lab 5.

-   You can use a turtle object's `circle` method to draw a circle. See the documentation for details on how to use it.

-   The circle colors and radii depend on the magnitude relative to the maximum magnitude. For example, the the red color should be 0 if the magnitude is 0 and 255 for the largest magnitude. This means we need to scale the quake's magnitude by a factor of $\frac{255}{m_{\max}}$ where $m_{\max}$ is the largest magnitude in the dataset.

## Submission

Take a screenshot of your program's output and save it as `earthquakes.png`. Submit `earthquakes.png` and `plot_earthquakes.py` to Canvas.

## Rubric

This lab is graded out of 10 points:

* 5 points: The program reads the earthquake data into a list of dictionaries
* 2 points: The maximum magnitude is calculated correctly
* 2 points: A circle is drawn at the correct coordinates for each earthquake
* 1 points: The circle's size and color varies linearly with the earthquake's magnitude

**Possible Deductions**

* -1 point: Author, date, and program description comment at the top of the file is missing
* -1 point: inadequate or inappropriate use of comments, poor variable naming, or other coding style issues

## Challenge - Anagrams

An *anagram* of a word is a different word spelled using the same letters. For instance, "elbow" is an anagram of "below". For purposes of this problem, we'll consider only anagrams that use exactly the same letters, without leaving any out or repeating letters more times than they appear in the original word. For example, "bow" and "bellow" are not considered anagrams of "below" for purposes of this problem.

Download [words.txt](words.txt) and write a program that finds the largest set of 6-letter words that are all anagrams of each other. As an example, among 3-letter words, there are two sets that tie for largest: `[’tea’, ’eat’, ’eta’, ’ate’]` and `[’aer’, ’ear’, ’are’, ’era’]`.

My program is able to find the three-letter sets in a second or two on my laptop. Finding the 6-letter set takes a little longer - around 45 seconds. I didn't import any modules from the standard library, but you may if you'd like---`itertools` might be particularly helpful. For the sake of efficiency, you may want do some thinking and/or research into what kind of collection you store things in; lists may not always be the best choice.

Name your program `anagram.py` and submit it to Canvas for up to 2 points of extra credit. One point is awarded for a correct solution; the second point is awarded for solving it without importing any modules.
