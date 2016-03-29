VerFloat = str(0.10) # We need to convert it to a string here otherwise Python will not allow us to use this float with strings in a print command
Version = 'Pre-Alpha v' + VerFloat
Title = 'PyWave ' + Version
VerifyServ = 'https://waveapi.gadget-guy.com/auth'
WebappCaching = True

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

# NOTE: ManualMode needs to be made as a function ( def ManualMode() ) here.



#################### Auth1
print("Auth1")
print()

# Setup time-based, randomised temporary cache to prepare for authentication

import datetime
unformattedTime = datetime.datetime.now().time()
formattedTime = unformattedTime.strftime("%H%M%S")
staticTime = str(formattedTime)
# Set the current time as the variable "staticTime", converting the current time to a string to make it static. formattedTime will return the time in HoursMinutesSeconds without any colons or spaces in-between.

# Note: Apps by default are stored in /usr/bin on Linux and %ProgramFiles% on Windows
if os.path.isdir(str(BINDIR) + "\Wave\cache") == False:
    # if the directory doesn't exist, create it
	os.makedirs(str(BINDIR) + "\Wave\cache", exist_ok=True)
	# Note: exist_ok tells Python that it's okay if the directory already exists when we attempt to create it, so don't throw an error and crash because of that. However, this feature requires Python v3.4.1+
	
import platform
if str(platform.system()) == "Windows":
    # Hide the cache directory from non-pro-users once made on Windows to help prevent mistakes and mess caused by users deleting the folders.
	os.system('attrib +H /S /D ' + str(BINDIR) + "\Wave\cache")
	
# Check if WebappCaching is enabled
if WebappCaching == True:
    verifyTmp = "\\Wave\\cache\\" + str(arg0)
	# Note: Double backslashes are needed as the backslash character is the escape character in Python
else:
    import random
    verifyTmp = "\\Wave\\cache\\" + staticTime + "-" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
	# Make verifyTmp contain the captured staticTime from earlier, then a dash and 4 random numbers. The numbers have to be converted to a string with str() in order to stop Python from crashing as usual

if os.path.isdir(str(BINDIR) + str(verifyTmp)) == False:
    # make the verifyTmp directory
    os.makedirs(str(BINDIR) + str(verifyTmp), exist_ok=True)
	
if str(platform.system()) == "Windows":
    # Hide the verifyTmp directory if on Windows
	os.system('attrib +H /S /D ' + str(BINDIR) + str(verifyTmp))



#################### Auth2
print("Auth2")
print()

# Authenticate with the server
print("Authenticating...")

# Check if the webapp exists already. If not, get it with cURL.
if os.path.exists(str(BINDIR) + str(verifyTmp) + "\\" + str(arg0) + ".webapp") == False:
    # Get it on Windows using cURL.exe
	if str(platform.system()) == "Windows":
	    os.system("call " + str(BINDIR) + '\\Wave\\libs\\cURL.exe -H -http2 --tcp-nodelay -A "PyWave/v0.10 (Pre-Alpha)" -s -o ' + str(BINDIR) + str(verifyTmp) + "\\" + str(arg0) + ".webapp " + VerifyServ + "/" + str(arg0) + ".webapp")
	
	# Get it on Linux using cURL (needs testing)
	if str(platform.system()) == "Linux":
	    os.system('curl -H -http2 --tcp-nodelay -A "PyWave/v0.10 (Pre-Alpha)" -s -o ' + str(BINDIR) + str(verifyTmp) + "\\" + str(arg0) + ".webapp " + VerifyServ + "/" + str(arg0) + ".webapp")

if os.path.exists(str(BINDIR) + str(verifyTmp) + "\\" + str(arg0) + ".webapp") == False:
    # todo: change colour to red text on black background
    print()
    print("Error: Failed to authenticate.")
    print("Stacktrace:")
    print("           Auth2")
    print("              \Download webapp")
    import shutil
    shutil.rmtree(str(BINDIR) + str(verifyTmp), ignore_errors=True)
	# delete the verifyTmp directory
	
	if str(platform.system()) == "mWindows":
	    os.system("pause")
	else:
	    input("Press any key and hit enter to continue . . .")
	# todo: pause console here
	# todo: change colour back to white text on black background
	# todo: quit gracefully