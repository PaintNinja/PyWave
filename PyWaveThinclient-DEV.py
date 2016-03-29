VerFloat = str(0.10) # We need to convert it to a string here otherwise Python will not allow us to use this float with strings in a print command
Version = 'Pre-Alpha v' + VerFloat
Title = 'PyWave ' + Version
VerifyServ = 'https://waveapi.gadget-guy.com/auth'

print(Title)
print('''
Notice: This is a highly experimental, stipped down version of Wave made from scratch in Python. Expect a lot of bugs and missing features.
''')

import os
BINDIR = os.path.realpath('.')
# Sets a variable called BINDIR which contains the current directory of this running binary

# todo: set the window title here

# todo: set window colours to white on black here

import sys
# Remove referrer info
# First, generate an array of all the arguments
args = sys.argv

# Now remove the first argument from the array
args.pop(0)

# Set the 0th argument as arg0. If blank, set it as blank rather than Python crashing
if len(args) == 0:
    arg0 = str("")
else:
    arg0 = sys.argv[0]



#################### ProcessReq1
print("ProcessReq1")
print()

print("Processing request \""+ arg0 +"\" with args ", end="")

for eachArg in args:
    print("\"" + eachArg + "\"", end=", ")
# prints each argument and ends it with a comma and space rather than a newline, and surrounds each arg in speech marks, with the backslash character used for escaping the speechmarks so
# that they can be used within print statements

print()
# print a space after the processing request message

if arg0 == "":
    ManualMode()
# Call ManualMode if there are no arguments

if arg0 == "credits":
    Credits()
# Show the Credits if the "credits" argument is specified



#################### Auth1
print("Auth1")
print()

# Setup time-based, randomised temporary cache to prepare for authentication

staticTime = str(datetime.datetime.now().time())
# Set the current time as the variable "staticTime", converting the current time to a string to make it static

