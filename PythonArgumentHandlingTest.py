VerFloat = str(0.10) # We need to convert it to a string here otherwise Python will not allow us to use this float with strings in a print command
Version = 'Pre-Alpha v' + VerFloat
Title = 'PyWave ' + Version

print(Title)
print('''
Notice: This is a highly experimental, stipped down version of Wave made from scratch in Python. Expect a lot of bugs and missing features.
''')

import sys
for eachArg in sys.argv:
    print(eachArg)

print("")
print("This is argv")
print(sys.argv)

print("")
print("This is argv[0]")
print(sys.argv[0]) # Confusingly, Python starts listing arguments from zero instead of one, so the first argument is listed as #0, whilst in batch the first is listed as #1

print("")
print("This is argv[1], if it exists")
if len(sys.argv) > 1: # Bearing in mind that Python starts at zero, check if there are more than one arguments before printing
    print(sys.argv[1]) # Print the second (system.argv[1]) argument now that we know there's more than one argument being passed
