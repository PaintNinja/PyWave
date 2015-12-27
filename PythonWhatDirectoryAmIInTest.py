VerFloat = str(0.10) # We need to convert it to a string here otherwise Python will not allow us to use this float with strings in a print command
Version = 'Pre-Alpha v' + VerFloat
Title = 'PyWave ' + Version

print(Title)
print('''
Notice: This is a highly experimental, stipped down version of Wave made from scratch in Python. Expect a lot of bugs and missing features.
''')

import os

print(os.path.abspath(__file__)) # Returns the full path of this file including the file name and file extension

print(os.path.realpath('.')) # Returns the full path of this file but NOT the file name or file extension
