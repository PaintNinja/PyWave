import platform
print(platform.system())
# This will print 'Linux' for Linux, 'Windows' for Windows and 'Darwin' for Mac

import os #import the Python equivalent of batch's 'call' command.

if str(platform.system()) == "Windows" or str(platform.system()) == "Linux":
    print("You are using Windows or Linux")
    os.system('echo test') #os.system('command arg1 arg2 etc...') is equivalent to batch's 'call command arg1 arg2 etc...'
