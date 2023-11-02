###Algorithm Engineering Project

##Project Description:

This project aims to find an implementation for a program that will find times in which two employees/people are able to have a meeting. This is calculated based on their schedules and when they are clocked in.

The program is coded by creating a function which iterates through the schedules and finds times in which the two are able to meet. The program will prompt the user to enter schedules for different people and then the program will calculate a solution. The output is printed within the terminal as well as outputed to "Output.txt"

##Installation:

After cloning the repository, you can run the main.py file with

```bash
python3 main.py
```

This will prompt you for some inputs for a person's schedule and clock in/clock out time.
The test sample cases can be found within the Inputs.txt file, but you are free to use any input of the same format you would like.

##Documentation:

There are a few main functions
```python3
schedule_meeting(people, duration)
```
This is the main function that we use, which does the calculations and includes verifier code which makes sure that our condition(duration) is met.

```python3
output(meetings)
```
This is a simple line of code which reads the output to the "Outputs.txt file"

#Note: main.py has a function written to display the menu for application and usability purposes and does not have anything to do with the algorithm's code

##Usage:

To add a person's schedule, input 1 as your prompt answer and enter a schedule in the format of a python list e.g.

[['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00']]

Do the same for the clockin/clockout time e.g.

[['07:30', '18:00']]

The program automtically processes these strings as lists and modifies them to be useable by the code

#The duration is 30 minutes by default, but you can adjust it in the third option of the menu

Inputs are manually inputed into the program or enter "q" to quit. The output of the directed input is copied to the file "Output.txt". For ease convenience, the output will be printed to the console as well.
